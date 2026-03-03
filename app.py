import pandas as pd

def load_movies(csv_path):
    """
    Load movies from CSV file and return as list of dictionaries
    """
    df = pd.read_csv(csv_path)

    # Make everything lowercase for easy matching
    for col in ["mood", "genre", "language"]:
        df[col] = df[col].str.lower()

    return df.to_dict(orient="records")


def recommend_movies(movies, mood, genre, language):
    """
    Recommend top 3 movies based on mood, genre, and language
    """

    mood = mood.lower()
    genre = genre.lower()
    language = language.lower()

    strong_matches = []
    weak_matches = []

    for movie in movies:
        if (
            movie["mood"] == mood
            and movie["genre"] == genre
            and movie["language"] == language
        ):
            strong_matches.append(movie)

        elif movie["genre"] == genre and movie["language"] == language:
            weak_matches.append(movie)

    # Prefer strong matches, fallback to weak matches
    results = strong_matches if strong_matches else weak_matches

    return results[:3]