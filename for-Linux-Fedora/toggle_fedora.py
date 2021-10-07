from pynput.keyboard import Key, Listener		#pip install pynput...for detecting Caps or Num lock key pressed
import subprocess								#To check the state of caps and num lock
from pynotifier import Notification				#pip install py-notifier...for notification

def pop_up(message):
	Notification(
		title='Lock key state:',
		description=f'{message}',
		duration=1,
		urgency='normal'
	).send()

num = 0
caps = 0
x = subprocess.check_output('xset q | grep LED', shell=True)[65]	# gets the state of caps and num lock
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
			pop_up("Caps Lock is ON!")
			caps = 1
		elif caps == 1:
			pop_up("Caps lock off.")
			caps = 0

	if key == Key.num_lock:
		if num == 0:
			pop_up("Num Lock is ON!")
			num = 1
		elif num == 1:
			pop_up("Num lock off.")
			num = 0

with Listener(on_press = run) as listener:
	listener.join()