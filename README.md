# CFT_scripts
Scripts to help with EMIT's software

"Emit clicker.py"
Python script made to click repetetively through warning popup messages in Emit's reconstruction software for the Xerra.
Hopefully they have fixed this issue in future versions, or added an "ok to all" option.  But in the version I have, I had to click 'ok' to warnings for every image in a 700 image stack, so I wrote this instead.

Dependencies:
mouse, time, argparse

Usage:
python3 "Emit clicker.py" [clicks] [time] [disp_x] [disp_y]
Descriptive usage:
python3 "Emit clicker.py" [number of clicks] [time delay between clicks] [x location in pixels on your display] [y location in pixels on your display]

Optional arguments
clicks - number of clicks you want the program to enact
  Default is 10 clicks
time - time delay between clicks.  On some of the errors, it would take 0.5s-1s to load the next warning message so having a delay avoids the program clicking on nothing. 
  Defaults is 0s
disp_x - x location of where you want it to click on your display in pixels
  Defaults to 1168 (because that's where it is on the display I use)
disp_y - y location of where you want it to click on your display in pixels
  Defaults to 603 (because that's where it is on the display I use)
