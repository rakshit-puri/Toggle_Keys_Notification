import ctypes
import time
import tkinter as tk
try:
    from PIL import Image,ImageTk
except:
    import os
    os.system("pip install pillow -i https://pypi.douban.com/simple/")#this mirror is faster than the official one in China
    from PIL import Image,ImageTk

keyboard = ctypes.WinDLL("User32.dll")
VK_NUMLOCK = 0x90
VK_CAPITAL = 0x14


def get_capslock_state():
    #Returns the current Caps Lock State(On/Off)
    return 'Caps Lock On' if keyboard.GetKeyState(VK_CAPITAL) else 'Caps Lock Off'


def get_numlock_state():
    #Returns The current Num Lock State(On/Off)
    return 'Num Lock On' if keyboard.GetKeyState(VK_NUMLOCK) else 'Num Lock Off'


def fade():
    global twin
    for i in range(1,20):
        twin.wm_attributes('-alpha',1-5*i/100)
        twin.update()
        time.sleep(0.03)
    twin.destroy()


def pop_up(body, icon):
    global twin
    #Show a notification on the top-left corner
    #creat a window
    twin=tk.Tk()
    twin.geometry('128x128+50+60')
    twin.overrideredirect(True)
    twin.wm_attributes('-topmost',True)
    twin.wm_attributes('-alpha',0.95)
    twin.configure(background='#000000')
    #show image on the window
    imgf=Image.open('./assets/'+str(icon))
    imgf.thumbnail((128, 128))
    img=ImageTk.PhotoImage(imgf)
    tk.Label(twin,image=img).pack()
    #the window will disapair after 1500ms
    twin.after(1500,fade)
    twin.mainloop()


caps_curr = get_capslock_state()
num_curr = get_numlock_state()

#pop_up('Ready','READY.ico')
#If this runs, all the other things won't work. And I don't know why...
#Personally, I think this is useful, but more funny!
#I'll still upload "READY.ico" because I hope someone can make it run correctly.
#In fact, it worked for one time, but only one time...

while True:
    caps_change = get_capslock_state()
    num_change = get_numlock_state()

    if caps_curr != caps_change:
        if caps_change == 'Caps Lock On':
            pop_up(caps_change, "CapsLock_On.ico")
        else:
            pop_up(caps_change, "CapsLock_Off.ico")
        caps_curr = caps_change
        time.sleep(0.1)

    if num_curr != num_change:
        if num_change == 'Num Lock On':
            pop_up(num_change, "NumLock_On.ico")
        else:
            pop_up(num_change, "NumLock_Off.ico")
        num_curr = num_change
    time.sleep(0.2)

#    O
#   /--|   ← Praying
# __>

#I hope these can run with no bugs...
#In fact, there's no bugs 4 now. (But it's a bit slow)
