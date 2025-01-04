# Python Script to automatically click through Emit reconstruction excessive warning redundencies
# @author: Andrew Davis
# 12/23/2024

import mouse, time, argparse

parser = argparse.ArgumentParser("Emit_clicker")
parser.add_argument("clicks", help="the number of times you want it to click")
parser.add_argument("time", help="The time in between clicks in seconds.  Some of the prompts take longer to load than others")
parser.add_argument("disp_x", help="The x location on your display (in pixels) of where you want it to click")
parser.add_argument("disp_y", help="The y location on your display (in pixels) of wher you want it to click")
args = parser.parse_args()

def multiclick_left(clicks, t=0, disp_x=1168, disp_y=603):
    for i in range(0,clicks):
        mouse.move(disp_x, disp_y)
        mouse.click('left')
        time.sleep(t)

#print(mouse.get_position())

multiclick_left(int(args.clicks),float(args.time), int(args.disp_x), int(args.disp_y))
