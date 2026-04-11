import csv
from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

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
    """Read a CSV of songs and return a list of dicts with numeric fields cast to float/int."""
    print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, newline='', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            row['id'] = int(row['id'])
            row['energy'] = float(row['energy'])
            row['tempo_bpm'] = float(row['tempo_bpm'])
            row['valence'] = float(row['valence'])
            row['danceability'] = float(row['danceability'])
            row['acousticness'] = float(row['acousticness'])
            songs.append(row)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Return a normalized 0–1 score and a list of reason strings for a song against user preferences."""
    WEIGHTS = {
        "mood":         0.25,
        "energy":       0.20,
        "valence":      0.20,
        "genre":        0.15,
        "acousticness": 0.10,
        "tempo_bpm":    0.05,
        "danceability": 0.05,
    }
    CATEGORICAL = {"genre", "mood"}
    TEMPO_MIN, TEMPO_MAX = 60, 200

    score = 0.0
    total_weight = 0.0
    reasons = []

    for feature, weight in WEIGHTS.items():
        if feature not in user_prefs:
            continue

        user_val = user_prefs[feature]
        song_val = song[feature]

        if isinstance(user_val, bool):
            user_val = 1.0 if user_val else 0.0

        if feature in CATEGORICAL:
            feature_score = 1.0 if user_val == song_val else 0.0
            label = "match" if feature_score == 1.0 else "no match"
        else:
            if feature == "tempo_bpm":
                user_val = (user_val - TEMPO_MIN) / (TEMPO_MAX - TEMPO_MIN)
                song_val = (song_val - TEMPO_MIN) / (TEMPO_MAX - TEMPO_MIN)
            feature_score = 1.0 - abs(user_val - song_val)
            label = "close" if feature_score >= 0.7 else "far"

        weighted = feature_score * weight
        score += weighted
        total_weight += weight
        reasons.append(f"{feature} {label} (+{weighted:.2f})")

    normalized = score / total_weight if total_weight > 0 else 0.0
    return (normalized, reasons)

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Score all songs, sort by score descending, and return the top k as (song, score, explanation) tuples."""
    scored = sorted(
        [(song, *score_song(user_prefs, song)) for song in songs],
        key=lambda x: x[1],
        reverse=True
    )
    return [(song, score, ", ".join(reasons)) for song, score, reasons in scored[:k]]
