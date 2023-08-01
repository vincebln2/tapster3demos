import sys
sys.path.append("..")

import time
import robot

if len(sys.argv) > 1:
    PORT = sys.argv[1]
else:
    print("Please specify a port.")
    sys.exit()

r = robot.Robot(PORT)
r.send("G1 F13000")
r.go(0,0,0)
r.tap_height = -53
r.clearance_height = -40

def box():
    r.go(-50, 50)
    time.sleep(1)
    r.go(50, 50)
    time.sleep(1)
    r.go(50, -50)
    time.sleep(1)
    r.go(-50, -50)
    time.sleep(1)

#functions for each key on calculator
#test: 123 - 45 - 67 + 89 = 100
#added 1 ms bufer time after each number to ensure robot is finished pressing button before tapping again
#previously, without the buffer time, the robot would sometimes fail to move the stylus up before going to the next number

def zero():
    r.tap(-15, -45)
    time.sleep(0.001)
    
def one():
    r.tap(-15, -34)
    time.sleep(0.001)

def two():
    r.tap(-2, -34)
    time.sleep(0.001)

def three():
    r.tap(11, -34)
    time.sleep(0.001)

def four():
    r.tap(-15, -22)
    time.sleep(0.001)

def five():
    r.tap(-2, -22)
    time.sleep(0.001)

def six():
    r.tap(11, -22)
    time.sleep(0.001)

def seven():
    r.tap(-15, -10)
    time.sleep(0.001)

def eight():
    r.tap(-2, -10)
    time.sleep(0.001)

def nine():
    r.tap(11,-10)
    time.sleep(0.001)

def on():
    r.tap(-28, -45)
    time.sleep(0.001)

def clear():
    r.tap(-28, -45)
    time.sleep(0.001)

def plus():
    r.tap(22, -34)
    time.sleep(0.001)

def minus():
    r.tap(22, -22)
    time.sleep(0.001)

def mult():
    r.tap(22,-10)
    time.sleep(0.001)

def div():
    r.tap(22, 2)
    time.sleep(0.001)

def equals():
    r.tap(11, -45)
    time.sleep(0.001)

def demo():
    r.go(0,0,30)
    clear()
    one()
    two()
    three()
    minus()
    four()
    five()
    minus()
    six()
    seven()
    plus()
    eight()
    nine()
    equals()
    r.go(0,0,30)

def sizzle():
    clear()
    three()
    seven()
    two()
    two()
    one()
    five()
    r.go(0,0,30)
    #move back up at the end of each word so screen is visible

def boobies():
    clear()
    five()
    three()
    one()
    eight()
    zero()
    zero()
    eight()
    r.go(0,0,30)
    
def obsess():
    clear()
    five()
    five()
    three()
    five()
    eight()
    zero()
    r.go(0,0,30)

def eggshell():
    clear()
    seven()
    seven()
    three()
    four()
    five()
    six()
    six()
    three()
    r.go(0,0,30)

def giggle():
    clear()
    three()
    seven()
    six()
    six()
    one()
    six()
    r.go(0,0,30)

def google():
    clear()
    three()
    seven()
    six()
    zero()
    zero()
    six()
    r.go(0,0,30)

def longDemo():
    #make the calculator say: "sizzle", "google", etc. with buffer time inbetween to see words
    #i wanted it to say "hello" but leading zeroes do not show on this calculator
    #list of words you can type on a calculator: http://blog.presentandcorrect.com/250-words-you-can-spell-with-a-calculator
    r.go(0,0,30)
    google()
    time.sleep(5)
    obsess()
    time.sleep(5)
    eggshell()
    time.sleep(5)
    giggle()
    time.sleep(5)
    sizzle()

#goes to a point above calculator, clears, types the equation, presses equal, then goes back to original position
if __name__ == '__main__':
    longDemo()