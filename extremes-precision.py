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
r.tap_height = -52
r.clearance_height = -20

def corners():
    #Moves stylus up vertically, then moves to 4 "extremes"/in a square above the screen
    #ends in position where camera can view screen
    r.go(50, 50, 50)
    time.sleep(0.5)
    r.go(50, -50)
    time.sleep(0.5)
    r.go(-50, -50)
    time.sleep(0.5)
    r.go(-50, 50)
    time.sleep(0.5)
    r.go(0, -80, 60)

if __name__ == '__main__':
    r.go(0,0,30)
    time.sleep(2)
    for x in range(5):
        corners()
        r.tap(0,0)
        time.sleep(1)