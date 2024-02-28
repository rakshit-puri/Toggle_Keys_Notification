# Toggle Keys Notification for Linux
   
## Steps to run
1. Install pynput and pynotifier using ```pip install pynput``` and ```pip install py-notifier``` in the Terminal.
2. Run **linux_notify.py**

<p align = "center">
  <img text = "Linux Toggle Key Notification Demo" src = "/Linux Toggle Key Notification.gif"/>
</p> 

## Setup  
If you want the file to automatically run in the background after Linux login then it can be added as a startup application.  
 1. Search "Startup Application Preference" or the equivalent startup manager of your linux  distribution in the search bar and open it.
 2. Select the "Add" option and fill out the discription boxes.
 3. In terminal search "which python" and copy the path.
 4. Paste this path into the "Command" dialogue box  in the Add window followed by " /path/to/the/linux_notify.py".
 5. Click on add.