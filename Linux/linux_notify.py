# Use "pip install pynput" for detecting Caps or Num lock key pressed
from pynput.keyboard import Key, Listener
# Use "pip install py-notifier" for notification
from pynotifier import Notification
import subprocess
import os

PATH = os.path.abspath(os.path.dirname(__file__)) + '/assets/'
state = {48: (0, 0), 49: (1, 0), 50: (0, 1), 51: (1, 1)}
NUM = 0
CAPS = 0
# Gets the state of caps and num lock
x = subprocess.check_output('xset q | grep LED', shell=True)[65]
if x in state.keys():
    CAPS, NUM = state[x]


def pop_up(message, my_icon):
    Notification(
        title='Lock Key State',
        description=f'{message}',
        icon_path=PATH + my_icon,
        duration=1,
        urgency='normal'
    ).send()


def run(key):
    global CAPS, NUM
    if key == Key.caps_lock:
        if CAPS == 0:
            pop_up("Caps Lock On", 'CapsLock_On.png')
            CAPS = 1
        else:
            pop_up("Caps Lock Off", 'CapsLock_Off.png')
            CAPS = 0

    if key == Key.num_lock:
        if NUM == 0:
            pop_up("Num Lock On", 'NumLock_On.png')
            NUM = 1
        else:
            pop_up("Num Lock Off", 'NumLock_Off.png')
            NUM = 0


with Listener(on_press=run) as listener:
    listener.join()
