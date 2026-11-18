"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")
    
    # Default pop/happy profile
    user_prefs = {
        "favorite_genre": "pop",
        "favorite_mood": "happy",
        "target_energy": 0.8,
        "likes_acoustic": False,
    }

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print(f"\nProfile: genre={user_prefs['favorite_genre']}, mood={user_prefs['favorite_mood']}, "
          f"energy={user_prefs['target_energy']}, likes_acoustic={user_prefs['likes_acoustic']}")
    print(f"\nTop {len(recommendations)} recommendations")
    print("=" * 40)

    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        print(f"{rank}. {song['title']} by {song['artist']}")
        print(f"   Score: {score:.2f} / 4.5")
        print("   Reasons:")
        for reason in explanation.split(", "):
            print(f"     - {reason}")
        print()

if __name__ == "__main__":
    main()
