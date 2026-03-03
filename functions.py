rom functions import load_movies, recommend_movies
from mood_ai import detect_mood

def main():
    print("🎬 Welcome to MovieMate 🎬")

    movies = load_movies("data/movies.csv")

    choice = input("Do you want to speak your mood? (yes/no): ").strip().lower()

    if choice == "yes":
        print("🎤 Voice mode (simulated)")
        text = input("Type a sentence describing your mood: ")
        mood = detect_mood(text)
        print("🧠 Detected mood:", mood)
    else:
        mood = input("Enter your mood (happy, sad, excited, etc): ")
