# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'feeder_system_main.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1281, 696)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setUnderline(False)
        MainWindow.setFont(font)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setIconSize(QtCore.QSize(10, 10))
        MainWindow.setToolButtonStyle(QtCore.Qt.ToolButtonIconOnly)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Triangular)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.centralwidget.sizePolicy().hasHeightForWidth())
        self.centralwidget.setSizePolicy(sizePolicy)
        self.centralwidget.setMouseTracking(True)
        self.centralwidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.centralwidget.setAutoFillBackground(False)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSizeConstraint(QtWidgets.QLayout.SetNoConstraint)
        self.horizontalLayout.setContentsMargins(9, -1, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tab = QtWidgets.QTabWidget(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tab.sizePolicy().hasHeightForWidth())
        self.tab.setSizePolicy(sizePolicy)
        self.tab.setMouseTracking(True)
        self.tab.setFocusPolicy(QtCore.Qt.TabFocus)
        self.tab.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tab.setAutoFillBackground(True)
        self.tab.setTabPosition(QtWidgets.QTabWidget.West)
        self.tab.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tab.setIconSize(QtCore.QSize(16, 16))
        self.tab.setElideMode(QtCore.Qt.ElideNone)
        self.tab.setDocumentMode(False)
        self.tab.setTabsClosable(False)
        self.tab.setMovable(False)
        self.tab.setObjectName("tab")
        self.tab_manual = QtWidgets.QWidget()
        self.tab_manual.setObjectName("tab_manual")
        self.button_forward = QtWidgets.QPushButton(self.tab_manual)
        self.button_forward.setGeometry(QtCore.QRect(950, 220, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_forward.setFont(font)
        self.button_forward.setObjectName("button_forward")
        self.button_down = QtWidgets.QPushButton(self.tab_manual)
        self.button_down.setGeometry(QtCore.QRect(750, 420, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_down.setFont(font)
        self.button_down.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.button_down.setIconSize(QtCore.QSize(24, 24))
        self.button_down.setAutoRepeatDelay(0)
        self.button_down.setObjectName("button_down")
        self.button_up = QtWidgets.QPushButton(self.tab_manual)
        self.button_up.setGeometry(QtCore.QRect(750, 20, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_up.setFont(font)
        self.button_up.setObjectName("button_up")
        self.button_reverse = QtWidgets.QPushButton(self.tab_manual)
        self.button_reverse.setGeometry(QtCore.QRect(550, 220, 200, 200))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.button_reverse.setFont(font)
        self.button_reverse.setObjectName("button_reverse")
        self.doubleSpinBox_increment = QtWidgets.QDoubleSpinBox(self.tab_manual)
        self.doubleSpinBox_increment.setGeometry(QtCore.QRect(290, 249, 151, 141))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(False)
        font.setWeight(50)
        font.setKerning(True)
        self.doubleSpinBox_increment.setFont(font)
        self.doubleSpinBox_increment.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.doubleSpinBox_increment.setReadOnly(False)
        self.doubleSpinBox_increment.setButtonSymbols(QtWidgets.QAbstractSpinBox.PlusMinus)
        self.doubleSpinBox_increment.setDecimals(2)
        self.doubleSpinBox_increment.setSingleStep(1.0)
        self.doubleSpinBox_increment.setObjectName("doubleSpinBox_increment")
        self.label_increment = QtWidgets.QLabel(self.tab_manual)
        self.label_increment.setGeometry(QtCore.QRect(60, 250, 221, 131))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_increment.setFont(font)
        self.label_increment.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_increment.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_increment.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_increment.setWordWrap(True)
        self.label_increment.setObjectName("label_increment")
        self.tab.addTab(self.tab_manual, "")
        self.tab_automatic = QtWidgets.QWidget()
        self.tab_automatic.setObjectName("tab_automatic")
        self.label_speed = QtWidgets.QLabel(self.tab_automatic)
        self.label_speed.setGeometry(QtCore.QRect(70, 350, 261, 101))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_speed.setFont(font)
        self.label_speed.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_speed.setWordWrap(True)
        self.label_speed.setObjectName("label_speed")
        self.horizontalScrollBar_speed = QtWidgets.QScrollBar(self.tab_automatic)
        self.horizontalScrollBar_speed.setGeometry(QtCore.QRect(350, 350, 731, 100))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(185, 185, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 194, 194))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 199, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 185, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(194, 194, 194))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 199, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.HighlightedText, brush)
        brush = QtGui.QBrush(QtGui.QColor(185, 185, 185))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 199, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(199, 199, 199))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(195, 195, 195))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.HighlightedText, brush)
        self.horizontalScrollBar_speed.setPalette(palette)
        self.horizontalScrollBar_speed.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalScrollBar_speed.setObjectName("horizontalScrollBar_speed")
        self.widget_part_dimension = QtWidgets.QWidget(self.tab_automatic)
        self.widget_part_dimension.setGeometry(QtCore.QRect(40, 20, 1150, 291))
        self.widget_part_dimension.setObjectName("widget_part_dimension")
        self.doubleSpinBox_length = QtWidgets.QDoubleSpinBox(self.widget_part_dimension)
        self.doubleSpinBox_length.setGeometry(QtCore.QRect(310, 100, 211, 140))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.doubleSpinBox_length.setFont(font)
        self.doubleSpinBox_length.setObjectName("doubleSpinBox_length")
        self.doubleSpinBox_parts = QtWidgets.QDoubleSpinBox(self.widget_part_dimension)
        self.doubleSpinBox_parts.setGeometry(QtCore.QRect(829, 100, 211, 140))
        font = QtGui.QFont()
        font.setPointSize(30)
        self.doubleSpinBox_parts.setFont(font)
        self.doubleSpinBox_parts.setDecimals(0)
        self.doubleSpinBox_parts.setObjectName("doubleSpinBox_parts")
        self.label_length = QtWidgets.QLabel(self.widget_part_dimension)
        self.label_length.setGeometry(QtCore.QRect(70, 100, 221, 140))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_length.setFont(font)
        self.label_length.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_length.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_length.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_length.setWordWrap(True)
        self.label_length.setObjectName("label_length")
        self.label_parts = QtWidgets.QLabel(self.widget_part_dimension)
        self.label_parts.setGeometry(QtCore.QRect(620, 100, 191, 140))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label_parts.setFont(font)
        self.label_parts.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label_parts.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label_parts.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_parts.setWordWrap(True)
        self.label_parts.setObjectName("label_parts")
        self.label_dimension = QtWidgets.QLabel(self.widget_part_dimension)
        self.label_dimension.setGeometry(QtCore.QRect(450, 10, 431, 71))
        font = QtGui.QFont()
        font.setPointSize(36)
        font.setBold(True)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(75)
        self.label_dimension.setFont(font)
        self.label_dimension.setObjectName("label_dimension")
        self.label_emergency = QtWidgets.QLabel(self.widget_part_dimension)
        self.label_emergency.setGeometry(QtCore.QRect(0, 0, 411, 111))
        font = QtGui.QFont()
        font.setPointSize(30)
        font.setBold(True)
        font.setWeight(75)
        self.label_emergency.setFont(font)
        self.label_emergency.setObjectName("label_emergency")
        self.pushButton_start = QtWidgets.QPushButton(self.tab_automatic)
        self.pushButton_start.setGeometry(QtCore.QRect(350, 520, 200, 80))
        self.pushButton_start.setObjectName("pushButton_start")
        self.pushButton_stop = QtWidgets.QPushButton(self.tab_automatic)
        self.pushButton_stop.setGeometry(QtCore.QRect(660, 520, 200, 80))
        self.pushButton_stop.setObjectName("pushButton_stop")
        self.tab.addTab(self.tab_automatic, "")
        self.horizontalLayout.addWidget(self.tab)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionNew = QtWidgets.QAction(MainWindow)
        self.actionNew.setObjectName("actionNew")
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionCopy = QtWidgets.QAction(MainWindow)
        self.actionCopy.setObjectName("actionCopy")
        self.actionPaste = QtWidgets.QAction(MainWindow)
        self.actionPaste.setObjectName("actionPaste")

        self.retranslateUi(MainWindow)
        self.tab.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Feeder UI"))
        self.button_forward.setText(_translate("MainWindow", "Forward"))
        self.button_down.setText(_translate("MainWindow", "Press"))
        self.button_up.setText(_translate("MainWindow", "Lift"))
        self.button_reverse.setText(_translate("MainWindow", "Reverse"))
        self.label_increment.setText(_translate("MainWindow", "Increment Size (mm)"))
        self.tab.setTabText(self.tab.indexOf(self.tab_manual), _translate("MainWindow", "Manual Mode"))
        self.label_speed.setText(_translate("MainWindow", "Feeding Speed (step/second)"))
        self.label_length.setText(_translate("MainWindow", "Part Length (mm)"))
        self.label_parts.setText(_translate("MainWindow", "Number of parts"))
        self.label_dimension.setText(_translate("MainWindow", "Job Scheduling"))
        self.label_emergency.setText(_translate("MainWindow", "EMERGENCY"))
        self.pushButton_start.setText(_translate("MainWindow", "Start"))
        self.pushButton_stop.setText(_translate("MainWindow", "Stop"))
        self.tab.setTabText(self.tab.indexOf(self.tab_automatic), _translate("MainWindow", "Automatic Mode"))
        self.actionNew.setText(_translate("MainWindow", "New"))
        self.actionNew.setShortcut(_translate("MainWindow", "Ctrl+N"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionCopy.setText(_translate("MainWindow", "Copy"))
        self.actionPaste.setText(_translate("MainWindow", "Paste"))
