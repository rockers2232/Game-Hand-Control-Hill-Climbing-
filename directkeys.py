import subprocess
import time

right_pressed = "Right"
left_pressed = "Left"

def PressKey(key):
    subprocess.run(["xdotool", "keydown", key])

def ReleaseKey(key):
    subprocess.run(["xdotool", "keyup", key])

if __name__ == '__main__':
    while True:
        PressKey(right_pressed)
        time.sleep(1)
        ReleaseKey(right_pressed)
        time.sleep(1)
