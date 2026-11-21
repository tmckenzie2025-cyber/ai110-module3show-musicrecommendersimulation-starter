"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from recommender import load_songs, recommend_songs


# --- Standard profiles ---
HIGH_ENERGY_POP = {
    "favorite_genre": "pop", "favorite_mood": "happy",
    "target_energy": 0.9, "likes_acoustic": False,
}
CHILL_LOFI = {
    "favorite_genre": "lofi", "favorite_mood": "chill",
    "target_energy": 0.35, "likes_acoustic": True,
}
DEEP_INTENSE_ROCK = {
    "favorite_genre": "rock", "favorite_mood": "intense",
    "target_energy": 0.92, "likes_acoustic": False,
}

# --- Adversarial / edge-case profiles ---
# Conflicting: sad mood but maximum energy (the only "sad" song is low-energy blues).
CONFLICTING_SAD_HIGH_ENERGY = {
    "favorite_genre": "blues", "favorite_mood": "sad",
    "target_energy": 0.9, "likes_acoustic": False,
}
# Genre/mood that don't exist in the catalog: only energy + acoustic can score.
GHOST_GENRE = {
    "favorite_genre": "k-pop", "favorite_mood": "euphoric",
    "target_energy": 0.5, "likes_acoustic": True,
}
# Dead-center energy: every song is within ~0.5 of 0.5, so energy barely discriminates.
FENCE_SITTER = {
    "favorite_genre": "jazz", "favorite_mood": "relaxed",
    "target_energy": 0.5, "likes_acoustic": False,
}
# Out-of-range energy (>1.0): the gap formula can go negative-ish / reward nothing.
OUT_OF_RANGE_ENERGY = {
    "favorite_genre": "edm", "favorite_mood": "energetic",
    "target_energy": 5.0, "likes_acoustic": False,
}
# Genre says calm, energy says loud: does genre weight (1.5) beat energy fit?
GENRE_VS_ENERGY = {
    "favorite_genre": "classical", "favorite_mood": "peaceful",
    "target_energy": 1.0, "likes_acoustic": False,
}

PROFILES = {
    "High-Energy Pop": HIGH_ENERGY_POP,
    "Chill Lofi": CHILL_LOFI,
    "Deep Intense Rock": DEEP_INTENSE_ROCK,
    "ADVERSARIAL: Sad but max energy": CONFLICTING_SAD_HIGH_ENERGY,
    "ADVERSARIAL: Genre/mood not in catalog": GHOST_GENRE,
    "ADVERSARIAL: Energy fence-sitter": FENCE_SITTER,
    "ADVERSARIAL: Out-of-range energy (5.0)": OUT_OF_RANGE_ENERGY,
    "ADVERSARIAL: Calm genre, loud energy": GENRE_VS_ENERGY,
}


def run_profile(name: str, user_prefs: dict, songs: list, k: int = 5) -> None:
    recommendations = recommend_songs(user_prefs, songs, k=k)

    print(f"\n== {name} ==")
    print(f"   genre={user_prefs['favorite_genre']}, mood={user_prefs['favorite_mood']}, "
          f"energy={user_prefs['target_energy']}, acoustic={user_prefs['likes_acoustic']}")
    for rank, (song, score, _explanation) in enumerate(recommendations, start=1):
        print(f"   {rank}. {song['title']:<24} {score:5.2f}  ({song['genre']}/{song['mood']}, e={song['energy']})")


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded songs: {len(songs)}")

    for name, prefs in PROFILES.items():
        run_profile(name, prefs, songs)


if __name__ == "__main__":
    main()
