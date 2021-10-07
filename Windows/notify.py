import ctypes
import time

try:
    from toast import ToastNotifier
except ModuleNotFoundError:
    import sys

    sys.exit(
        "Use the command \"pip install win10toast\" in Command Prompt/Powershell to use notify.py")

keyboard = ctypes.WinDLL("User32.dll")
VK_NUMLOCK = 0x90
VK_CAPITAL = 0x14


def get_capslock_state():
    """Returns the current Caps Lock State(On/Off)"""
    return "Caps Lock On" if keyboard.GetKeyState(VK_CAPITAL) else "Caps Lock Off"


def get_numlock_state():
    """Returns The current Num Lock State(On/Off)"""
    return "Num Lock On" if keyboard.GetKeyState(VK_NUMLOCK) else "Num Lock Off"


def pop_up(body, icon):
    """Generates Pop-up notification when state changes"""
    notification = ToastNotifier()
    notification.show_toast("Lock Key State", body,
                            icon_path="assets\\" + icon, duration=1.5)


caps_curr = get_capslock_state()
num_curr = get_numlock_state()

while True:
    caps_change = get_capslock_state()
    num_change = get_numlock_state()

    if caps_curr != caps_change:
        if caps_change == "Caps Lock On":
            pop_up(caps_change, "CapsLock_On.ico")
        else:
            pop_up(caps_change, "CapsLock_Off.ico")
        caps_curr = caps_change
        time.sleep(0.1)

    if num_curr != num_change:
        if num_change == "Num Lock On":
            pop_up(num_change, "NumLock_On.ico")
        else:
            pop_up(num_change, "NumLock_Off.ico")
        num_curr = num_change
    time.sleep(0.2)
