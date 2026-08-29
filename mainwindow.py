import subprocess 
import time 


def get_active_app(): 
    script = 'tell application "System Events" to get name of first application process whose frontmost is true' 
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return result.stdout.strip() 


def get_active_window_title():
    script = '''
    tell application "System Events"
        set frontApp to first application process whose frontmost is true
        tell frontApp
            try
                return name of front window
            on error
                return ""
            end try
        end tell
    end tell
    '''
    result = subprocess.run(["osascript", "-e", script], capture_output=True, text=True)
    return result.stdout.strip()


print("Script started!! Switch to another window now!!")

while True:
    app = get_active_app() 
    print(f"Active App: {app}", flush=True)
    title = get_active_window_title()
    print(f"Active Window: {title}", flush=True)
    time.sleep(2)