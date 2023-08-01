# tapster3demos
Contains demos I wrote for the Tapster 3/3+ robot summer of 2023.

## vinceCalc
This program makes the Tapster 3 tap buttons on a calculator. 

demo() makes it type 123 - 45 + 67 + 89 then the equals button.
There are also functions to type various words on the calculator such as sizzle, obsess, eggshell, google, and boobies (I was not allowed to use this one in the video demo).

## precision
precision.py was the first version of our repeatability tests. It taps a certain amount of times in the same spot at the center of the robot's movement range.

## extremes-precision
This program was the second version of the repeatability tests. It also taps the same spot at the robot's movement range, but moves to 4 "extremes", or corners of the robot's movement range, between each tap.

## precision_randomized
This is another version of the repeatability tests. Does the same thing as extremes-precision, but adds an extra movement to a random spot above the screen after moving to the 4 "extremes" to simulate regular use of the robot.

## sectored_precision and max-sectored-precision
The last version of the repeatability tests builds upon the previous versions to test multiple parts of the touch screen. sectored_precision is for the t3, while max-sectored-precision is for the t3+.

## t3-speed-test
This is the code we used to run our speed tests on the t3/3+. It moves the end effector from one end of the robot's movement range, waits 2 seconds, moves to the other end, waits, then repeats that several times.
