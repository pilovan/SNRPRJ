import math
import RPi.GPIO as GPIO
import time

class ActuatorControl:
        
    def __init__(self):
        self.stepper_sequence = [1,1,0,0]
        self.channel_list = (11,13,15,16,18,22)
        self.steps = 0
        self.seconds = 0.005
        self.speed = 1
        self.num_parts = 0
        self.steptime = self.seconds
        self.pausetime = 1
        self.stopped_value = False
        self.pwm = GPIO.PWM(32,50)
        self.pwm.start(0)
        
        self.init_stepper_pos()
       
    def forward(self):
         for step in range(int(self.steps)):
            GPIO.output(18,0) 
            GPIO.output(11,1) 
            GPIO.output(13,1) 
            GPIO.output(15,1)
            time.sleep(self.seconds)

            GPIO.output(11,0)
            GPIO.output(18,1)
            GPIO.output(16,1) 
            GPIO.output(22,1)
            time.sleep(self.seconds)
         
            GPIO.output(18,0)
            GPIO.output(11,1)
            GPIO.output(13,0)
            GPIO.output(15,0)
            time.sleep(self.seconds)
        
            GPIO.output(11,0)
            GPIO.output(18,1)
            GPIO.output(16,0)
            GPIO.output(22,0)
            time.sleep(self.seconds)                 
    
    def reverse(self):
        for step in range(int(self.steps)):
            #D
            GPIO.output(11,0)
            GPIO.output(18,1)
            GPIO.output(16,0)
            GPIO.output(22,0)
            time.sleep(self.seconds)
            #B
            GPIO.output(18,0)
            GPIO.output(11,1)
            GPIO.output(13,0)
            GPIO.output(15,0)
            time.sleep(self.seconds)
            #C
            GPIO.output(11,0)
            GPIO.output(18,1)
            GPIO.output(16,1) 
            GPIO.output(22,1)
            time.sleep(self.seconds)
            #A          
            GPIO.output(18,0) 
            GPIO.output(11,1) 
            GPIO.output(13,1) 
            GPIO.output(15,1)
            time.sleep(self.seconds)
                
    def automation_mode(self):
        x = 1
        for part in range(int(self.num_parts)):
            time.sleep(self.pausetime)
            for step in range(int(self.steps)):
                if self.stopped_value == True:
                    return
                
  
                        
                GPIO.output(18,0) 
                GPIO.output(11,1) 
                GPIO.output(13,1) 
                GPIO.output(15,1)
                time.sleep(self.steptime)

                GPIO.output(11,0)
                GPIO.output(18,1)
                GPIO.output(16,1) 
                GPIO.output(22,1)
                time.sleep(self.steptime)
             
                GPIO.output(18,0)
                GPIO.output(11,1)
                GPIO.output(13,0)
                GPIO.output(15,0)
                time.sleep(self.steptime)
            
                GPIO.output(11,0)
                GPIO.output(18,1)
                GPIO.output(16,0)
                GPIO.output(22,0)
                time.sleep(self.steptime)
                
    def init_stepper_pos(self):
        #set initial
        GPIO.output(11,0)
        GPIO.output(18,1)
        GPIO.output(16,0)
        GPIO.output(22,0)
        
        time.sleep(.5)
        #turn off channels
        GPIO.output(11,0)
        GPIO.output(18,0)

    def stepper_disable_GPIO(self):
        GPIO.output(11, 0)
        GPIO.output(18, 0)
                    
    def calculate_steps(self, distance):
        radius = float(30) # radius of roller
        distance = float(distance) #distance inquired
        angle_size = 1.8
        theta = float( (distance * 360) / (2 * math.pi * radius ))
        self.steps = float(round( theta / ( angle_size )))
        #print("Moved {} mm ({} steps) forward".format(distance, self.steps))
        
    def getspeed(self, speed):
        self.speed = (speed/100) + 1
        self.steptime = self.seconds/self.speed
        self.pausetime = (self.seconds*200)/self.speed
        print(self.pausetime)
        
    def getparts(self, num):
        self.num_parts = num
        
    def stoppedValue(self):
        self.stopped_value = True
        
    def resetStoppedValue(self):
        self.stopped_value = False

    def servo_up(self):     
        self.pwm.ChangeDutyCycle(5.5) #9.5

    def servo_down(self):
        self.pwm.ChangeDutyCycle(8.5) #3.5

    def servo_stop(self):
        self.pwm.ChangeDutyCycle(0)
        
    def servo_off(self):
        self.pwm.stop()