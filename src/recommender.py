from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass
import csv

# Scoring weights (max total = 0.75 + 1.0 + 3.0 + 0.5 = 5.25)
GENRE_WEIGHT = 0.75   # halved from 1.5
MOOD_WEIGHT = 1.0
ENERGY_WEIGHT = 3.0   # doubled from 1.5

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Read songs.csv into a list of dicts with numeric columns converted to numbers."""
    songs = []
    with open(csv_path, newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            row["id"] = int(row["id"])
            row["energy"] = float(row["energy"])
            row["tempo_bpm"] = float(row["tempo_bpm"])
            row["valence"] = float(row["valence"])
            row["danceability"] = float(row["danceability"])
            row["acousticness"] = float(row["acousticness"])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Score one song against the user's preferences and return (score, reasons)."""
    score = 0.0
    reasons = []

    if song["genre"] == user_prefs["favorite_genre"]:
        score += GENRE_WEIGHT
        reasons.append(f"genre match (+{GENRE_WEIGHT})")
    
    if song["mood"] == user_prefs["favorite_mood"]:
        score += MOOD_WEIGHT
        reasons.append(f"mood match (+{MOOD_WEIGHT})")

    # Clamp target energy to the valid 0-1 range so scores stay within 0..5.25
    target_energy = min(1.0, max(0.0, user_prefs["target_energy"]))
    gap = abs(song["energy"] - target_energy)
    energy_points = ENERGY_WEIGHT * (1 - gap)
    score += energy_points
    reasons.append(f"energy fit (+{energy_points:.2f})")

    if user_prefs["likes_acoustic"]:
        acoustic_points = 0.5 * song["acousticness"]
    else:
        acoustic_points = 0.5 * (1 - song["acousticness"])
    score += acoustic_points
    reasons.append(f"acoustic fit (+{acoustic_points:.2f})")

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score every song, sort from highest to lowest, and return the top k as (song, score, explanation)."""
    results = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = ", ".join(reasons)
        results.append((song, score, explanation))

    ranked = sorted(results, key=lambda item: item[1], reverse=True)
    return ranked[:k]