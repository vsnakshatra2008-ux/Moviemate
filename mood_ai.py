def detect_mood(text):
    text = text.lower()

    if any(word in text for word in ["happy", "joy", "excited", "fun"]):
        return "happy"
    elif any(word in text for word in ["sad", "cry", "emotional", "lonely"]):
        return "sad"
    elif any(word in text for word in ["angry", "frustrated", "mad"]):
        return "angry"
    elif any(word in text for word in ["relaxed", "calm", "peace"]):
        return "calm"
    else:
        return "neutral"