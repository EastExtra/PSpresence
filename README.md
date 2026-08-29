# Discord Rich Presence for Creative Apps

A background script that reads what app/window you have active on macOS 
and (eventually) sends that info to Discord as a custom status.

## Status: early WIP

Currently working:
- Detects the active app name (via AppleScript)
- Detects the active window title (via AppleScript)

Not built yet:
- Parsing window titles into useful info (filename, canvas size, etc.)
- Sending anything to Discord
- Idle detection

## Setup

```bash
uv sync
uv run mainwindow.py
```

Switch between apps/windows while it's running — it prints the active 
app and window title every 2 seconds.

## Why

Most Discord presence tools only track games or Spotify. This tracks 
creative/dev tools instead — what file you're working on, what app 
you're in — mainly so friends/collaborators can see what you're 
actually doing.