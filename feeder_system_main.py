import sys
import time
import concurrent.futures
import RPi.GPIO as GPIO
from PyQt5 import QtWidgets as qtw # contains any widgets, classes
from PyQt5 import QtCore as qtc # signal and slots, low level
from PyQt5.QtCore import QObject, QThread, pyqtSignal, QTimer
from PyQt5 import QtGui as qtg # styling, font, color
from PyQt5.QtWidgets import QMessageBox

from feeder_system_gui import Ui_MainWindow
from rasbian_setup import Setup
from actuator_functions import ActuatorControl

RS = Setup() 
Actuator = ActuatorControl()


class Worker(QObject):
    finished = pyqtSignal()
    
    def run(self):
        Actuator.automation_mode()
        Actuator.resetStoppedValue()
        Actuator.servo_stop()
        self.finished.emit()
        
class WorkerFailsafe(QObject):
    finished = pyqtSignal()
    emergency = pyqtSignal()
    noEmergency = pyqtSignal()
    
    def run(self):
        GPIO.setmode(GPIO.BOARD)
        while (True):
            if GPIO.input(36) == 1:
                self.emergency.emit()
            else:
                self.noEmergency.emit()
            time.sleep(1)

class MainWindow(qtw.QMainWindow):
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
      
        # call main window UI
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        
        #failsafe interrupt
        self.failsafe_thread()

        # button characteristic setup
        self.ui.button_forward.setAutoRepeat(True)
        self.ui.button_reverse.setAutoRepeat(True)
        self.ui.button_up.setAutoRepeat(True)
        self.ui.button_down.setAutoRepeat(True)
        
        # manual mode button actions                   
        self.ui.doubleSpinBox_increment.valueChanged.connect(lambda: Actuator.calculate_steps(self.ui.doubleSpinBox_increment.text()))
        self.ui.button_forward.pressed.connect(lambda: Actuator.forward()) 
        self.ui.button_reverse.pressed.connect(lambda: Actuator.reverse())
        self.ui.button_up.pressed.connect(lambda: Actuator.servo_up())
        self.ui.button_up.released.connect(lambda: Actuator.servo_stop())
        self.ui.button_down.pressed.connect(lambda: Actuator.servo_down())
        self.ui.button_down.released.connect(lambda: Actuator.servo_stop())
        
        #automatic mode button actions
        self.ui.horizontalScrollBar_speed.valueChanged.connect(lambda: Actuator.getspeed(self.ui.horizontalScrollBar_speed.value()))
        self.ui.doubleSpinBox_length.valueChanged.connect(lambda: Actuator.calculate_steps(self.ui.doubleSpinBox_length.text()))
        self.ui.doubleSpinBox_parts.valueChanged.connect(lambda: Actuator.getparts(self.ui.doubleSpinBox_parts.text()))
        self.ui.pushButton_start.clicked.connect(lambda: self.automation_thread())
        self.ui.pushButton_stop.clicked.connect(lambda: Actuator.stoppedValue())
        self.ui.pushButton_stop.clicked.connect(lambda: Actuator.stepper_disable_GPIO())
        self.show()
    
    def closeEvent(self, event):
        quit_message = """Closing application and reseting GPIO connections!"""
        QMessageBox.information(self, 'Message', quit_message)
        RS.cleanup()
    
    def automation_thread(self):
        self.thread = QThread()
        self.worker = Worker()
        self.worker.moveToThread(self.thread)
        self.thread.started.connect(self.worker.run)
        self.worker.finished.connect(self.thread.quit)
        self.worker.finished.connect(self.worker.deleteLater)
        self.thread.finished.connect(self.thread.deleteLater)
        self.thread.start()  
        
        self.ui.pushButton_start.setEnabled(False)
        self.ui.tab_manual.setEnabled(False)
        self.thread.finished.connect(lambda: self.ui.pushButton_start.setEnabled(True))
        self.thread.finished.connect(lambda: self.ui.tab_manual.setEnabled(True))
        self.thread.finished.connect(lambda: Actuator.stepper_disable_GPIO())
        
    def failsafe_thread(self):
        self.thread_2 = QThread()
        self.worker_2 = WorkerFailsafe()
        self.worker_2.moveToThread(self.thread_2)
        self.thread_2.started.connect(self.worker_2.run)
        self.worker_2.finished.connect(self.thread_2.quit)
        self.worker_2.finished.connect(self.worker_2.deleteLater)
        self.thread_2.finished.connect(self.thread_2.deleteLater)
        
        self.worker_2.emergency.connect(lambda: self.ui.label_emergency.setStyleSheet("color: red"))
        self.worker_2.emergency.connect(lambda: self.ui.label_emergency.setText("EMERGENCY"))
        self.worker_2.emergency.connect(lambda: Actuator.stoppedValue())
        self.worker_2.emergency.connect(lambda: self.ui.pushButton_start.setEnabled(False))
        self.worker_2.emergency.connect(lambda: Actuator.stepper_disable_GPIO())
        
        self.worker_2.noEmergency.connect(lambda: self.ui.label_emergency.setText(""))
        self.worker_2.noEmergency.connect(lambda: self.ui.pushButton_start.setEnabled(True))
        self.worker_2.noEmergency.connect(lambda: Actuator.resetStoppedValue())        
        
        
        self.thread_2.start()
        
        

       
if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    app.setStyle("plastique")
    w = MainWindow()    
    sys.exit(app.exec_())
    