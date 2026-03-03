import pandas as pd

def load_movies(csv_path):
    df = pd.read_csv(csv_path)

    # normalize text
    for col in ["mood", "genre", "language"]:
        df[col] = df[col].str.lower()

    return df.to_dict(orient="records")


def recommend_movies(movies, mood, genre, language):
    mood = mood.lower()
    genre = genre.lower()
    language = language.lower()

    mood_genre_map = {
        "sad": ["comedy", "romantic", "uplifting"],
        "depressed": ["comedy", "feel-good"],
        "bored": ["comedy", "action"],
        "happy": ["comedy", "adventure"],
        "excited": ["action", "thriller"],
        "emotional": ["drama"],
        "neutral": []
    }

    preferred_genres = mood_genre_map.get(mood, [])

    results = []

    # 1️⃣ strict match
    for m in movies:
        if (
            genre in m["genre"]
            and m["language"] == language
        ):
            results.append(m)

    # 2️⃣ same language + mood genres
    if not results:
        for m in movies:
            if m["language"] == language:
                for g in preferred_genres:
                    if g in m["genre"]:
                        results.append(m)
                        break

    # 3️⃣ ANY language + mood genres
    if not results:
        for m in movies:
            for g in preferred_genres:
                if g in m["genre"]:
                    results.append(m)
                    break

    # sort by rating (AI polish ⭐)
    results = sorted(results, key=lambda x: x["rating"], reverse=True)

    return results[:3]


def mood_message(mood, genre):
    messages = {
        "sad": "💛 Feeling sad? Let’s lighten your mood with some laughter!",
        "bored": "😴 Feeling bored? Let’s find something fun!",
        "happy": "😄 You’re in a great mood! Enjoy!",
        "excited": "🔥 Let’s keep the energy high!",
        "emotional": "💙 Let’s watch something meaningful.",
        "neutral": "🎬 Let’s find a great movie for you!"
    }

    return messages.get(mood, "🎥 Sit back and enjoy your movie!")