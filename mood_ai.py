def detect_mood(text):
    text = text.lower()

    if any(word in text for word in ["sad", "depressed", "lonely", "down"]):
        return "sad"
    elif any(word in text for word in ["happy", "joy", "great", "excited"]):
        return "happy"
    elif any(word in text for word in ["bored", "tired", "nothing"]):
        return "bored"
    elif any(word in text for word in ["angry", "furious", "mad"]):
        return "excited"
    else:
        return "neutral"