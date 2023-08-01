import sys
sys.path.append("..")

import time
import robot
import random

if len(sys.argv) > 1:
    PORT = sys.argv[1]
else:
    print("Please specify a port.")
    sys.exit()
# '/dev/cu.usbserial-10'
r = robot.Robot(PORT)
r.send("G1 F13000")
r.go(0,0,0)
r.tap_height = -35
# -48 for t3, -35 fr t3+
r.clearance_height = -20

'''
  1| 2 | 3
___|___|___
 4 | 5 | 6
___|___|___
 7 | 8 | 9
   |   |
sectors
width - 130 mm
height - 130 (it is taller, but the browser ui is in the way)
'''

def one(): 
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    time.sleep(1)
    r.tap(-65,65)
    time.sleep(1)

def two():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    time.sleep(1)
    r.tap(0,65)
    time.sleep(1)

def three():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    time.sleep(1)
    r.tap(65,65)
    time.sleep(1)

def four():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    time.sleep(1)
    r.tap(-65,0)
    time.sleep(1)

def five():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    time.sleep(1)
    r.tap(0,0)
    time.sleep(1)

def six():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    time.sleep(1)
    r.tap(65,0)
    time.sleep(1)

def seven():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    time.sleep(1)
    r.tap(-65,-65)
    time.sleep(1)

def eight():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    time.sleep(1)
    r.tap(0,-65)
    time.sleep(1)

def nine():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    time.sleep(1)
    r.tap(65,-65)
    time.sleep(1)

def calibrate():
    #Goes to e
    one()
    two()
    three()
    four()
    five()
    six()
    seven()
    eight()
    nine()
    
if __name__ == '__main__':
    x = 0
    random.seed()
    r.go(0,0,30)
    time.sleep(1)
    for x in range(30):
        nine()
        
    r.go(0,0,30)
