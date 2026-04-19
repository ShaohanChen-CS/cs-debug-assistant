from data import ERROR_DB

def debug_error(msg):
    msg = msg.lower()
    
    for key in ERROR_DB:
        if key in msg or any(word in msg for word in key.split()):
            return ERROR_DB[key]
    
    return {
    "explanation": "I'm not fully sure about this error yet, but it might be related to syntax or logic issues.",
    "fix": "Try checking your code structure or searching the full error message online."
}