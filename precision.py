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

if __name__ == '__main__':
    r.go(0,0,0)
    for x in range(10):
        r.tap(0,0)
        time.sleep(1)