# Toggle Keys Notification
A python script that shows a notification when Caps Lock or Num Lock keys are pressed. It is useful for people that don't have LEDs on their keyboards. Currently, it works for Windows only.

The code uses a modified version of the win10toast library provided as **toast.py**.    
## Steps to run
1. Install win10toast library using ```pip install win10toast``` in Command Prompt/Powershell  
2. Run **notification.pyw**  

<p align = "center">
  <img text = "Toggle Key Notification Demo" src = "/Toggle Key Notification.gif"/>
</p>  

## Setup  
If you want the file to automatically run in the background after Windows login then it can be added as a startup application.  
  1. Press Windows+R to open the “Run” dialog box.  
  2. Type “shell:startup” and then hit Enter to open the “Startup” folder.  
  3. Paste a shortcut of the **notification.pyw** file in the “Startup” folder.   
