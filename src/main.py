"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

import textwrap

from tabulate import tabulate

from recommender import load_songs, recommend_songs


PROFILES = {
    # --- Normal profiles ---
    "gym_session": {
        "label": "Gym Session",
        "prefs": {"genre": "pop", "mood": "intense", "energy": 0.9, "acousticness": False},
    },
    "late_night_study": {
        "label": "Late-Night Study",
        "prefs": {"genre": "lofi", "mood": "chill", "energy": 0.35, "acousticness": True},
    },
    "evening_unwind": {
        "label": "Evening Unwind",
        "prefs": {"genre": "r&b", "mood": "romantic", "energy": 0.55},
    },
    # --- Adversarial / edge-case profiles ---
    "mood_only": {
        "label": "Mood Only (edge case)",
        "prefs": {"mood": "happy"},
    },
    "contradictory_chill_high_energy": {
        "label": "Contradictory: Chill Mood + High Energy",
        "prefs": {"mood": "chill", "energy": 0.95},
    },
    "unknown_genre": {
        "label": "Unknown Genre: country",
        "prefs": {"genre": "country", "mood": "happy", "energy": 0.8, "acousticness": False},
    },
}


def run_profile(name: str, songs: list, k: int = 3) -> None:
    profile = PROFILES[name]
    print(f"\n  {profile['label']}")
    print(f"  Preferences: {profile['prefs']}\n")

    recommendations = recommend_songs(profile["prefs"], songs, k=k)

    rows = []
    for rank, (song, score, explanation) in enumerate(recommendations, start=1):
        wrapped_reasons = "\n".join(textwrap.wrap(explanation, width=48))
        rows.append([rank, song["title"], song["artist"], song["genre"], song["mood"], f"{score:.2f}", wrapped_reasons])

    headers = ["#", "Title", "Artist", "Genre", "Mood", "Score", "Reasons"]
    print(tabulate(rows, headers=headers, tablefmt="rounded_outline"))
    print()


def main() -> None:
    songs = load_songs("data/songs.csv")
    print(f"Loaded {len(songs)} songs\n")

    for name in PROFILES:
        run_profile(name, songs,5)


if __name__ == "__main__":
    main()
