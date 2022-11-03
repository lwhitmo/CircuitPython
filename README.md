
# CircuitPython
Hello, This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [CircuitPython Distance Sensor](#CircuitPython_Distance_Sensor)
* [Motor Control](#MotorControl)
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

### Description & Code

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

### Description & Code

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

### Description & Code

### Evidence
![cyrus's_gif](https://github.com/cwyatt29/Engineering_3_Notebook/blob/master/Images/ezgif.com-gif-maker.gif)

image credit goes to [cyrus wyatt](https://github.com/cwyatt29) 
### Wiring
![wiring image motor control](https://github.com/lwhitmo/CircuitPython/blob/master/Images/Screenshot%202022-11-01%20115847.png)
### Reflection

