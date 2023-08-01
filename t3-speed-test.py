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
# PORT = "/dev/cu.usbserial-10"
r = robot.Robot(PORT)
r.send("G0")
r.go(0,0,-20)
time.sleep(1)

def backForward(x):
    r.go(0, x)
    time.sleep(1)
    r.go(0, -x)
    time.sleep(1)

if __name__ == '__main__':
    
    for x in range(5):
        backForward(100)