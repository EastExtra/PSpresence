import re 

SEPARATORS = [" — ", " – ", " | ", " - ", ": "]

FILENAME_RE = re.compile(r"\b[\w\-. ]+\.[a-zA-Z0-9]{1,6}\b")

DISCORD_MAX_LEN = 128 
DISCORD_MIN_LEN = 2 

def _clean(text): 
    text = text.strip(" -–—|:●•\u200b")
    return text 

def _turncate(text, limit=DISCORD_MAX_LEN):
    return text if len(text) <= limit else text[: limit - 1] + "..."

def _split_title(title): 
    for sep in SEPARATORS: 
        if sep in title: 
            first, rest = title.split(sep, 1)
            return _clean(first), _clean(rest)
    return _clean(title), None 

def parse_title(app_name, window_title): 
    window_title = (window_title or "").strip() 

    if not window_title: 
        return {"details": "Using", "state": app_name or "an app"}
    
    filename_match = FILENAME_RE.search(window_title)
    first, rest = _split_title(window_title)

    if filename_match: 
        filename = filename_match.group(0)
        details = f"Editing{filename}"
        state = rest if rest and rest != filename else app_name
    elif rest: 
        details = first 
        state = f"in {app_name}" if app_name and app_name not in rest else rest
    else: 
        details = app_name or "Working"
        state = first 

    details = _turncate(_clean(details)) or "Working"
    state = _turncate(_clean(state)) or "No details"

    if len(details) < DISCORD_MIN_LEN:
        details = "Working"
    if len(state) < DISCORD_MIN_LEN:
        state = app_name or "Active"

    return {"details": details, "state": state}