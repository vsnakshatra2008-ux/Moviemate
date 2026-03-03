from functions import load_movies, recommend_movies, mood_message

def detect_mood(text):
    text = text.lower()
    if "sad" in text or "down" in text:
        return "sad"
    if "happy" in text or "excited" in text:
        return "happy"
    if "bored" in text:
        return "bored"
    return "neutral"


def main():
    print("🎬 Welcome to MovieMate – AI Movie Recommender 🎬\n")

    movies = load_movies("data/movies.csv")

    choice = input("Do you want to speak your mood? (yes/no): ").strip().lower()

    if choice == "yes":
        print("🎤 Voice mode (simulated)")
        text = input("Type a sentence describing your mood: ")
        mood = detect_mood(text)
        print(f"🧠 Detected mood: {mood}")
    else:
        mood = input("Enter your mood (happy, sad, excited, etc): ").lower()

    genre = input("Enter genre (Action, Comedy, Drama, etc): ").lower()
    language = input("Enter language (English, Tamil, Hindi, etc): ").lower()

    print("\n" + mood_message(mood, genre) + "\n")

    recommendations = recommend_movies(movies, mood, genre, language)

    if not recommendations:
        print("😔 No movies found. Try different options.")
        return

    print("🎥 Recommended Movies for You:\n")

    for i, movie in enumerate(recommendations, 1):
        print(f"{i}. 🎬 {movie['title']}")
        print(f"   ⭐ Rating: {movie['rating']}")
        print(f"   ⏱ Duration: {movie['duration']}")
        print(f"   📺 OTT: {movie['ott']}")
        print(f"   📝 {movie['description']}\n")


if __name__ == "__main__":
    main()