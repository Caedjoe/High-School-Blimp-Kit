from machine import Pin, PWM
import time
import network
import socket
import config

#Pin numbers for motors
# config.up_down_motor_pin_number = 7
# config.left_motor_pin_number = 8
# config.right_motor_pin_number = 9

#Pin objects
updown_motor_pin = Pin(config.up_down_motor_pin_number, Pin.OUT)
left_motor_pin = Pin(config.left_motor_pin_number, Pin.OUT)
right_motor_pin = Pin(config.right_motor_pin_number, Pin.OUT)

#PWM objects
up_down_motor_pwm = PWM(updown_motor_pin, freq=50, duty=77)
left_motor_pwm = PWM(left_motor_pin, freq=50,duty=77)
right_motor_pwm = PWM(right_motor_pin, freq=50,duty=77)

ap = network.WLAN(network.AP_IF) # create access-point interface (Wifi Network)
ap.active(False)
ap.config(ssid='iudtr') # set the SSID of the access point
ap.config(max_clients=5)
ap.active(True)
print('network up')

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('192.168.4.1', 80))  # The IP address for the AP is typically 192.168.4.1
sock.listen(1)  # Listen for incoming connections
print(f'listening on {ap.ifconfig()}')

message = ''
datachar = ''

#Values of 77 are roughly "centered", and the duty cycle function can be set from 40 to 114, with 40 being full reverse
# and 114 being full forward. These extreme values are never officially sent, since this would pull too much current from 
#the battery.

time.sleep(1)
up_down_motor_pwm.duty(80) 
time.sleep(.1)
up_down_motor_pwm.duty(77)

left_motor_pwm.duty(80)
time.sleep(.1)
left_motor_pwm.duty(77)

right_motor_pwm.duty(80)
time.sleep(.1)
right_motor_pwm.duty(77)

while True:
  cl, addr = sock.accept() #accepts connection
  cl.send('\r\nConnected: ')
  
  while True:
    
    message = ''
    datachar = ''
    command = cl.recv(1).decode('utf-8')
    
    if command == 'E': #E is for "END" providing a wireless "killswitch"
      up_down_motor_pwm.duty(77) 
      left_motor_pwm.duty(77)
      right_motor_pwm.duty(77)
      cl.close()
      break
    
    while datachar != '*': #read until the end of the command
      message += datachar 
      datachar = cl.recv(1).decode('utf-8')
      
    #command structure
    #L,U/D,R
    #"77,80,72*"
    left_cmd, up_cmd, right_cmd = message.split(",") #split each command into three parts, one for each motor
    
    #convert string to integer
    left_cmd = int(77 + (float(left_cmd) * 37))
    up_cmd = int(77 + (float(up_cmd) * 37))
    right_cmd = int(77 + (float(right_cmd) * 37))
    
    #set motor objects to PWM value
    up_down_motor_pwm.duty(up_cmd) 
    left_motor_pwm.duty(left_cmd)
    right_motor_pwm.duty(right_cmd)
    
    cl.send(f'Set motors to duty values: {left_cmd},{up_cmd},{right_cmd}!\r\n')
