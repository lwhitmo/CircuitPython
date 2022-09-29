# Table of Contents
* [Neopixel](#Neopixel)
* [Servo](#Servo)

## Neopixel

### Description
make the board print a color
### Code
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


![image text](image link)
### Reflection



## Servo 

### Description 
Move servo 180 in a sweeping motion back and forth

### Code

link to [the code](https://github.com/lwhitmo/CircuitPython/blob/master/Code/friend.py)
``` py
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

### Every new project:
1. Make a GitHub account if you don't have one with your normal school credentials and sign into it.
2. Click the big green Use This Template button at the top of this page.
3. Name the new repository something appropriate to the purpose of your project (Your first one should probably be named `CircuitPython`).
4. Hit "Create repository from template." (The default settings should be fine.)
5. Open VS Code on your machine. Click Clone Repository.
6. Paste in the link to the new repository you've just created from the template and hit enter.
7. For the location, select the "STUDENT" drive if you have it or the document folder if you don't.
8. Hit "Open Cloned Directory."
9. Install the reccomended extensions when you get that popup in the lower right corner.
### To commit from VS Code:
1. Go to the little branch icon in the left bar of VS Code.
2. Click the + icon next  to the files you want to commit.
3. Write a message that descibes your changes in the "Message" box and hit commit.
4. If you get an error about user.name and user.email, see the next section.
5. Click the "Sync changes" button.
### If you get an error about user.name and user.email
1. In VS Code, hit `` Ctrl+Shift+` ``
2. Filling in your actual information, run the following commands one line at a time. The paste shortcut is `Ctrl+V` or you can right click then hit paste. Spelling must match exactly:
```
git config --global user.name YOURUSERNAME
git config --global user.email YOURSCHOOLEMAIL
```
3. Return to step 3 of the previous section.










# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
make the board print a color

Here's how you make code look like code:

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


![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


And here is how you should give image credit to someone, if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code

```python
Code goes here

```

### Evidence
![servo_go_round](https://github.com/lwhitmo/CircuitPython/blob/master/Images/servo%20gif.gif)

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection




## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





## NextAssignment

### Description & Code

```python
Code goes here

```

### Evidence
