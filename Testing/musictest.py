import subprocess 
import time

VIDEO_APPS = {"VLC", "Spotify"}
VIDEO_SITES = {"youtube"}
BROWSERS = {"Helium"}



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

while True: 

    app = get_active_app() 
    title = get_active_window_title()

    found = False
    for site in VIDEO_SITES:
        if site in title.lower(): 
            found = True 
            break

    if app in VIDEO_APPS: 
        print("Video: yes(video app)")
    elif app in BROWSERS and found: 
        print("Video: yes (video site in browser)")
    else: 
        print("Video: no")

    time.sleep(2) 


