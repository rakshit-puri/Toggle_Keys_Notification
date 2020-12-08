# Toggle Keys Notification
A python script that shows a notification when Caps Lock or Num Lock keys are pressed. It is useful for people that don't have LEDs on their keyboards. Currently, it works for Windows only.

The code uses a modified version of the win10toast library provided as **toast.py**.    
Use the command, ```pip install win10toast``` to use the **toast.py** file with **notification.pyw** file    

## Setup  
If you want the file to automatically run in the background after Windows login then it can be added as a startup application.  
  1. Press Windows+R to open the “Run” dialog box.  
  2. Type “shell:startup” and then hit Enter to open the “Startup” folder.  
  3. Create a shortcut in the “Startup” folder for the **notification.pyw** file and the “assets” folder.   
     
Project Demonstration: https://youtu.be/HdYMui99Fxw


