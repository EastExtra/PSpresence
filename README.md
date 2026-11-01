# PSpresence
## A Rich Presence for Productivity

A background script for macOS that reads the app and window you have active
and shows it on your Discord profile as a custom status.

## Status: early WIP

Working:
- Detects the active app name and window title (via AppleScript)
- Parses window titles into friendlier text (e.g. "Editing main.py")
- Sends it to Discord as Rich Presence, updating only when something changes
- Reconnects automatically if Discord isn't running yet or the connection drops
- Experimental: terminal-only video detection test (not connected to Discord)

Known issues:
- Filename detection is too eager in browsers (a title like "Python 3.14 notes"
  can show as "Editing Python 3.14")
- No rate limiting; Discord only accepts presence updates about every 15 seconds
- Window titles are sent as-is (see the privacy warning below)

Not built yet:
- Music detection (Spotify / Apple Music)
- Showing video activity on Discord
- Idle detection
- App allowlist / privacy filtering

## Requirements

- macOS
- Discord desktop app, running
- Python 3.14 and [uv](https://docs.astral.sh/uv/)
- Accessibility permission for your terminal (System Settings → Privacy &
  Security → Accessibility), otherwise window titles come back empty

## Setup

```bash
uv sync
uv run presence.py
```

Switch between apps and your Discord status should update. The terminal prints
what is being sent. Stop it with Ctrl+C.

The Discord client ID in `presence.py` is public, not a secret. To use your own
Discord app, create one in the Discord Developer Portal and replace `CLIENT_ID`.

## Privacy warning

Window titles are shown publicly on your Discord profile. Browser tabs, email
subjects and chat names can all appear. Don't run this while viewing anything
private until app filtering is added.

## Files

- `presence.py`: main script (detect the active window and send it to Discord)
- `par.py`: turns raw window titles into the text shown on Discord
- Rest are scripts for testing purposes 

## Why

Most Discord presence tools only track games or Spotify. This tracks
creative/dev tools instead, so friends and collaborators can see what you're
actually working on.