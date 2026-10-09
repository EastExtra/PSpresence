import subprocess 
import time 
from pypresence import Presence 


CLIENT_ID = '1542244771790323823'



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

def connect():
    rpc = Presence(CLIENT_ID)
    rpc.connect()     
    return rpc 

def main():
    rpc = None 
    last_state = None 
    start_time = time.time() 

    print("Script started!! Switch to another window now!!")


    while True:
        app = get_active_app() 
        title = get_active_window_title()
        current_state = (app, title) 

        if rpc is None:
            try: 
                rpc = connect() 
                print("Connected to Discord.")
            except Exception as e: 
                print(f"Discord not available yet ({e}), retrying in 5s...")
                time.sleep(5)
                continue
        
        if current_state != last_state:
            try:
                rpc.update(
                    details= app or "Unkown app",
                    state=title or "No window title",
                    start=start_time,
                )
                print(f"Updated presence: {app} - {title}")
                last_state = current_state
            except Exception as w:
                print(f"Lost connection to Discord({w}), will reconnect...")
                rpc = None 
                last_state = None 
        
        time.sleep(2) 

if __name__ == "__main__":
    main() 