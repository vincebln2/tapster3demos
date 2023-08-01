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
phone sectors
width - 60 mm
height - 100
column lines = -10,10
row lines = -16,16
middle of columns = -21, 0, 21 
middle of rows = 35,0,-35
'''

def one(): 
        r.go(random.randint(-70,70), random.randint(-70,70), 10)
        r.tap(-21,35)
def two():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    r.tap(0,35)

def three():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    r.tap(21,35)

def four():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    r.tap(-21,0)

def five():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    r.tap(0,0)

def six():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    r.tap(21,0)

def seven():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    r.tap(-21,-35)

def eight():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    r.tap(0,-35)

def nine():
    r.go(random.randint(-70,70), random.randint(-70,70), 10)
    r.tap(21,-35)

def calibrate():
    #Goes to 4 extreme corners then taps centers of each sector
    r.tap(-30,50)
    time.sleep(1)
    r.tap(30,  50)
    time.sleep(1)
    r.tap(-30,-50)
    time.sleep(1)
    r.tap(30,-50)
    time.sleep(1)
    one()
    time.sleep(1)
    two()
    time.sleep(1)
    three()
    time.sleep(1)
    four()
    time.sleep(1)
    five()
    time.sleep(1)
    six()
    time.sleep(1)
    seven()
    time.sleep(1)
    eight()
    time.sleep(1)
    nine()
    time.sleep(1)
    
if __name__ == '__main__':
    x = 0
    random.seed()
    r.go(0,0,30)
    time.sleep(1)
    for x in range(30):
        nine()
        time.sleep(1)
        
    r.go(0,0,30)
