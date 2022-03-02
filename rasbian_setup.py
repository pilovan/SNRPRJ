import RPi.GPIO as GPIO
import time

class Setup():
    
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        channel_list = (11,13,15,16,18,22,32)
        GPIO.setup(channel_list, GPIO.OUT)
        GPIO.output(channel_list, 0)
        GPIO.setwarnings(True)
        self.count = 0
        
        #emergency failsafe button setup
        self.emergency_gpio = 36
        GPIO.setup(self.emergency_gpio, GPIO.IN, pull_up_down=GPIO.PUD_UP)
        self.emergency_enable = True
        
    def button_pressed_callback(self, button):
        self.count = self.count + 1
        print("button pressed", self.count)
        
    def emergency(self):
#         GPIO.add_event_detect(self.emergency_gpio, GPIO.FALLING,
#                 callback=self.button_pressed_callback, bouncetime =6000)
        if GPIO.input(36) == 1:
            print("button pressed")
        else:
            print("button released")
            
    def cleanup(self):
        GPIO.cleanup()
    
