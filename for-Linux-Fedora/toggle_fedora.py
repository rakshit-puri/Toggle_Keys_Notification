# pip install pynput...for detecting Caps or Num lock key pressed
from pynput.keyboard import Key, Listener
import subprocess  # To check the state of caps and num lock
from pynotifier import Notification
# pip install py-notifier...for notification
import os


def pop_up(message, my_icon):
    Notification(
        title='Lock key state:',
        description=f'{message}',
        icon_path=os.path.abspath(os.path.dirname(__file__)) + '/' + my_icon,
        duration=1,
        urgency='normal'
    ).send()


num = 0
caps = 0
x = subprocess.check_output('xset q | grep LED', shell=True)[
    65]  # gets the state of caps and num lock
if x == 48:															# caps adds 1 and num adds 2
    caps = 0
    num = 0
elif x == 49:
    caps = 1
    num = 0
elif x == 50:
    caps = 0
    num = 1
elif x == 51:
    caps = 1
    num = 1


def run(key):
    global caps
    global num
    if key == Key.caps_lock:
        if caps == 0:
            pop_up("Caps Lock is ON!", 'CapsLock_On.png')
            caps = 1
        elif caps == 1:
            pop_up("Caps lock off.", 'CapsLock_Off.png')
            caps = 0

    if key == Key.num_lock:
        if num == 0:
            pop_up("Num Lock is ON!", 'NumLock_On.png')
            num = 1
        elif num == 1:
            pop_up("Num lock off.", 'NumLock_Off.png')
            num = 0


with Listener(on_press=run) as listener:
    listener.join()
