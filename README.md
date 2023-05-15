
# CircuitPython
Hello, This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [CircuitPython Distance Sensor](#CircuitPython_Distance_Sensor)
* [Motor Control](#MotorControl)
* [Temperature Sensor](#Temperature_Sensor)
* [Rotary Encoder](#Rotary_Encoder)
* [Photointerrupter](#Photointerrupter)
---
 
## Hello_CircuitPython
 
### Description & Code
make the board print a color
 
Link to [the code](https://github.com/lwhitmo/CircuitPython/blob/master/Code/friend.py)
``` py
import board
import neopixel
 
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5
 
print("Make it red!")
 
while True:
    dot.fill((255, 0, 255))
 ```
 
 
### Evidence
 
 
![Look at it go!! So many random colors...](https://github.com/jmuss07/Circuit-Python/blob/main/Images/Random_Color.gif?raw=true)
 
image credit goes to [josie muss](https://github.com/jmuss07)
 
 
 
 
 
 
### Reflection
Make sure that the brightness on the Neopixel does not exceed 0.5 or it will hurt the eyeballs. You can use a [color picker](https://htmlcolorcodes.com/) to find pleasant colors for the display.
 
 
 
## CircuitPython_Servo
 
### Description & Code
make the servo perform a sweeping mtion back and forth 180 degrees
 
link to [the code](https://github.com/lwhitmo/CircuitPython/blob/master/Code/friend.py)
```python
from adafruit_motor import servo
import board
import pwmio
import time
 
pwm = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)
 
my_servo = servo.Servo(pwm)
 
while True:
    for angle in range(0, 180, 10):  # 0 - 180 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
    for angle in range(180, 0, -10): # 180 - 0 degrees, 5 degrees at a time.
        my_servo.angle = angle
        time.sleep(0.05)
       
 
```
 
### Evidence
![servo_go_round](https://github.com/lwhitmo/CircuitPython/blob/master/Images/servo%20gif.gif)
 
 
### Wiring
![servo_wiring](https://github.com/lwhitmo/CircuitPython/blob/master/Images/servo-motor-with-arduino-uno-wiring-diagram-schematic-circuit-tutorial-featured-image.png)
 
image credit goes to internet
### Reflection
This is not the full version of the assignment. This current state signifies half of the assignment, which allows the servo motor to perform a sweeping motion back and forth 180 degrees.
 
 
 
## CircuitPython_LCD
 
### Description 
Make two inputs and use your LCD screen as an output device. Your Metro will count when one of the inputs is tripped, and the LCD will show the count. 
Your Metro should alternate between counting up and counting down when you touch the other input. The LCD should additionally show the count direction. 
### Code
 
```python
#original code credits go to Graham GS view linked code https://github.com/VeganPorkChop/CircutPython/blob/master/LCD.py
 
import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
 
# get and i2c object
i2c = board.I2C()
btn = DigitalInOut(board.D3)
btn2 = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP
# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)
cur_state = True
prev_state = True
cur_state2 = True
prev_state2 = True
buttonPress = 0
 
while True:
    while btn2.value == True:
        cur_state = btn.value
        if cur_state != prev_state:
            if not cur_state:
                buttonPress = buttonPress + 1
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
            else:
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
                print(buttonPress)
        prev_state = cur_state
    else:
        cur_state2 = btn.value
        if cur_state2 != prev_state2:
            if not cur_state2:
                buttonPress = buttonPress - 1
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
            else:
                lcd.clear()
                lcd.set_cursor_pos(0,0)
                lcd.print(str(buttonPress))
        prev_state2 = cur_state2
 
```
 
### Evidence
![toggle counter lcd](https://drive.google.com/file/d/1Kqoc5Ekqh7wrwV3bBTz1TlqLQrXzkRiQ/view)
 
### Wiring
 
### Reflection
When doing this assignment again, if the lcd is not printing, first check if the proper LCD is in place in the code. It could be
 
 
 
 
 
## CircuitPython_Distance_Sensor
 
### Description
Print out the measurement of the distance to an object in cm on your serial display or LCD using the HC-SR04. Make the neopixel turn red if your object is less than 5 cm away, blue if it is between 5 and 20 cm away, and green if it is more than 20 cm away. The on-board neopixel's color should gradually change to match the distance.

### Code
 
```python
#credit goes to Graham GS
#original code https://github.com/VeganPorkChop/CircutPython/blob/master/Sensorthing.py
 
 
# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
import digitalio
import simpleio
import time
import board
import adafruit_hcsr04
import neopixel
from board import *
 
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D3, echo_pin=board.D2)
Kaz = neopixel.NeoPixel(board.NEOPIXEL, 1)#connecting the neopixel on the board to the code
Kaz.brightness = 0.1  #setting the brightness of the light, from 0-1 brightness
KazOutput = 0
Red = 0
Green = 0
Blue = 0
 
while True:
    try:
        cm = sonar.distance
        print((sonar.distance, Red, Green, Blue))
        time.sleep(0.02)
        if cm < 5:
            Blue = 0
            Red = 255
            Kaz.fill((Red, 0, 0))#setting the color with RGB values
        if cm > 5 and cm < 10:
            Green = 0
            Red = simpleio.map_range(cm, 5.1, 10, 255, 0)
            Blue = simpleio.map_range(Red, 0, 255, 255, 0)
            Kaz.fill((Red, Green, Blue))
        else:
            Blue = simpleio.map_range(cm, 10.1, 20, 255, 0)
            Green = simpleio.map_range(Blue, 0, 255, 255, 0)
            Kaz.fill((0, Green, Blue))#setting the color with RGB values
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
 
```
 
### Evidence
![Gross Little GIF](https://github.com/inovotn04/CircuitPython/blob/main/Images/DistanceSensorEvidence.gif?raw=true)
 
image credit goes to [ian novotne](https://github.com/inovotn04/CircuitPython)
 
### Wiring
<img src="https://github.com/Jhouse53/CircuitPython/blob/main/GIF%20and%20Images/UltraSonicSensor%20wiring.PNG?raw=true" width="400">
 
Image credit goes to [Benton House](https://github.com/Jhouse53/CircuitPython)
### Reflection
when using the uultrasonic sensor it is ipmortant to not use a see through object or else the coordinates will get all wonky.
 
## MotorControl
Connect a motor and a 6-volt battery pack to this circuit. The motor can be programmed to accelerate and decelerate in response to input from a potentiometer.
### Description 

### Code
```python
# orginial code credit goes to Cyrus Wyatt
 
import time
from time import sleep
import board
import simpleio
from analogio import AnalogIn
import pwmio  
 
analog_in = AnalogIn(board.A1) #potentionmeter pin
pin_out = pwmio.PWMOut(board.D8,duty_cycle=65535,frequency=5000)
### Description
Wire up a 6v battery pack to this circuit w/ a motor.
Code something to make the motor speed up and slow down, based on input from a potentiometer.
 
### Codee
 
while True:
 
  sensor_value = analog_in.value
  # Map the sensor's range from 0<=sensor_value<=255 to 0<=sensor_value<=1023
  mapped_value = int(simpleio.map_range(sensor_value, 0, 65535, 0, 255))
 
  pin_out.duty_cycle = sensor_value
  print("mapped sensor value: ", sensor_value)
  time.sleep(0.1)
 
  ```
### Evidence
![cyrus's_gif](https://github.com/cwyatt29/Engineering_3_Notebook/blob/master/Images/ezgif.com-gif-maker.gif)
 
image credit goes to [cyrus wyatt](https://github.com/cwyatt29)
### Wiring
![wiring image motor control](https://github.com/lwhitmo/CircuitPython/blob/master/Images/Screenshot%202022-11-01%20115847.png)
### Reflection



## Temperature_Sensor

### Description
This assignment shows the temperature on an LCD using a temperature sensor.

### Code

```python
# original code credits go to my friend honklin

import board
from lcd.lcd import LCD # lcd libraries
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import analogio
import simpleio # map library
import time

i2c = board.I2C() # lcd declaration
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

tempSensor = analogio.AnalogIn(board.A0) # temperature sensor

temp = 74 # temperature
oldTemp = 0 # refresh variable
message = " "

while True:
    temp = int(simpleio.map_range(tempSensor.value,0,65535,32,212)) # maps values to Fahrenheit
    if (oldTemp != temp): # checks if needs to reprint lcd text
        if (temp <= 70): # higher than 70
         message = "Too cold!"
        elif (temp >= 78): # higher than 78
            message = "Too hot!"
        else: # 70-78
            message = "Just right"
        lcd.clear()
        lcd.set_cursor_pos(0,0)
        lcd.print(str(temp)) # prints temp
        lcd.set_cursor_pos(0,3)
        lcd.print("deg F")
        lcd.set_cursor_pos(1,0)
        lcd.print(message)
    oldTemp = temp
    time.sleep(1)
```

### Evidence

https://user-images.githubusercontent.com/121810694/225058207-99a6e2d3-5c1a-41ee-8983-57bb746485ee.mp4

Video of LCD displaying changing temperature sensor values (video credit goes to my friend Honklin)

### Wiring

![Temperature Sensor](https://user-images.githubusercontent.com/121810694/225062286-b8dbbc86-3c23-40e8-9475-0bb9638b4500.png)
Wiring for Temperature Sensor

### Reflection
Hazel has very sound facts, so I stoled it for research pourposes.

The hardest part of this assignment was finding the temperature values from the sensor. There isn't a library for the temperature sensor so I declared the sensor as an analog pin and found the values using analogio. The values I was getting were much too high so I mapped the values from 0 - 65535 to 32 - 212, which is the range for Fahrenheit. It was also important to remember that the SDA and SCL pins on the LCD screen go to the SDA and SCL pins on the Metro.





## Rotary_Encoder

### Description
This assignment changes traffic lights using a rotary encoder and displays the state on an LCD.

### Code
```python
#original code goes to Hazel Chonklin

import board
from lcd.lcd import LCD # lcd libraries
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import rotaryio # rotary encoder library
import digitalio # led library
import time

i2c = board.I2C() # lcd declaration
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

encoder = rotaryio.IncrementalEncoder(board.D3,board.D4) # rotary encoder potentiometer

button = digitalio.DigitalInOut(board.D2) # rotary encoder button
button.pull = digitalio.Pull.UP
button.direction = digitalio.Direction.INPUT

stop = digitalio.DigitalInOut(board.D13) # red led
stop.direction = digitalio.Direction.OUTPUT

caution = digitalio.DigitalInOut(board.D12) # yellow led
caution.direction = digitalio.Direction.OUTPUT

go = digitalio.DigitalInOut(board.D11) # green led
go.direction = digitalio.Direction.OUTPUT

position = 0 # modified position
states = ["stop", "caution", "go"] # states
state = " " # lcd print state
x = 0 # array selection

while True:
    prestate = state # uses for reprinting
    position = encoder.position % 20 # finds ticks from 0
    if (position < 7): # if stop
        x = 0
    elif (position > 12): # if go
        x = 2
    else: # if caution
        x = 1
    state = states[x] # sets state
    if (button.value == False): # if button is pressed
        stop.value = False
        caution.value = False
        go.value = False
        if (state == "stop"): # turns on correct light
            stop.value = True
        elif (state == "caution"):
            caution.value = True
        else:
            go.value = True
    if (state != prestate): # reprints lcd data
        lcd.clear()
        lcd.set_cursor_pos(0,0)
        lcd.print("Push for ")
        lcd.set_cursor_pos(0,9)
        lcd.print(state) # prints state
    time.sleep(0.1)
```

### Evidence

https://user-images.githubusercontent.com/121810694/226646755-eea054a9-9ec1-4bef-9fad-6f0f25bfa037.MOV

Video of rotary encoder selecting traffic states displayed on an LCD and turning on the correct LED (video credit goes to my friend Honklin)

### Wiring

![Rotary Encoder](https://user-images.githubusercontent.com/121810694/226651057-d4c9f24b-7374-41de-8f0a-3488ab28b840.png)
Wiring for Rotary Encoder (image credit goes to my friend Honklin)

### Reflection
The best facts coming from Honklin, once again.

In this assignment, it was very important to find the library for rotary encoders. Rotaryio lets the Metro communicate with both the button and the potentiometer on the rotary encoder, but they must be declared separately. The hardest part of this assignment was modifying the encoder position so that it could be used for the LEDs. I used % to find the remainder of 20 in order to fix the continuous rotation position, then I checked which third of the circle the encoder was in.




## Photointerrupter

### Description
This assignment displays the number of times a photointerrupter is interrupted on an LCD screen every 4 seconds.

### Code
```python
# OG code is hazel's

import board
from lcd.lcd import LCD # lcd liraries
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import digitalio # use photointerrupter was digital input
import time

i2c = board.I2C() # lcd declaration
lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)

photo = digitalio.DigitalInOut(board.D2) # photointerrupter
photo.direction = digitalio.Direction.INPUT

interrupts = 0
now = time.monotonic() # keeps time without sleep()
increase = False

while True:
    while (photo.value == True): # loops while being interrupted
        increase = True
    if (increase == True): # only counts one per interrupt
        interrupts += 1
        increase = False
    if (time.monotonic() - now >= 4): # prints every 4 seconds
        lcd.clear()
        lcd.set_cursor_pos(0,0)
        lcd.print("The number of")
        lcd.set_cursor_pos(1,0)
        lcd.print("interrupts is ")
        lcd.set_cursor_pos(1,14)
        lcd.print(str(interrupts)) # prints number of interrupts
        now = time.monotonic() # restarts counting
```

### Evidence

https://user-images.githubusercontent.com/121810694/227567106-54802ce9-0e27-498e-9d23-e5254b33d241.mp4

Video of LCD displaying the number of interrupts every 4 seconds (video credit goes to my friend Honklin)

### Wiring

![Photointerrupter](https://user-images.githubusercontent.com/121810694/226665078-655c64fd-0e29-41fc-a4ef-7e928f467bf7.png)
Wiring for Photointerrupter (image credit goes to my friend Honklin)

### Reflection
Honk the Conk got the FAX.

I couldn't find a library for the photointerrupter so I declared it as a digital input that would send input similar to how a button would. I also needed to use monotonic() instead of sleep() to delay reprinting the LCD because sleep() stops the code and therefore wouldn't recognize when it is interrupted. However, monotonic() records the current time, so comparing the time back to the old time throughout the code will allow it to reprint the LCD every 4 seconds and also recognize any interruptions. I also found that I needed to check the photointerrupter in a loop and only increase the total after it had turned false because if I do if interrupted, the code keeps counting until it is uninterrupted.
