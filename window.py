import pygetwindow as gw 
import time 

print("Script started! Switch to another window now!!")

while True: 
    win = gw.getActiveWindow() 
    if win: 
        print(f"Active Window: {win.title()}", flush=True)
    else:
        print("No active window detected :(!", flush=True)
    time.sleep(2) 