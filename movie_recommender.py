def recommend_movies(genre):
    movies = {
        "action": ["Mad Max: Fury Road", "John Wick", "Die Hard"],
        "comedy": ["Superbad", "The Hangover", "Step Brothers"],
        "drama": ["The Shawshank Redemption", "Forrest Gump", "The Godfather"],
        "horror": ["The Conjuring", "It", "A Quiet Place"],
        "sci-fi": ["Interstellar", "The Matrix", "Inception"],
        "romance": ["The Notebook", "Pride & Prejudice", "La La Land"]
    }
    genre = genre.lower()
    if genre in movies:
        print(f"Here are some {genre} movies you might like:")
        for movie in movies[genre]:
            print(f"- {movie}")
    else:
        print("Sorry, we don't have recommendations for that genre.")

def main():
    print("=== Movie Recommendation ===")
    user_genre = input("Enter a movie genre (action, comedy, drama, horror, sci-fi, romance): ")
    recommend_movies(user_genre)

if __name__ == "__main__":
    main()

