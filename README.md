# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

Replace this paragraph with your own summary of what your version does.

---

## Sample Output

![Sample Output](Sample.png)

---

## How The System Works

Real-world music recommenders like Spotify and YouTube Music use a hybrid of two strategies:
- **collaborative filtering** (finding patterns across millions of users with similar taste)
- **content-based filtering** (matching a song's audio attributes to what you've already liked)

This simulation focuses on **content-based filtering** — the same technique that powers Spotify's audio analysis features. Given a user taste profile, each song in the catalog is scored by how closely its attributes match the user's preferences. Songs are then ranked by score and the top matches are returned as recommendations. The system rewards *closeness to preference* rather than simply favoring high or low values.

### `Song` Features

- `genre` (categorical) — broad style label (pop, lofi, rock, jazz, etc.)
- `mood` (categorical) — intended emotional tone (chill, happy, intense, moody, etc.)
- `energy` (numerical) — overall intensity and activity level (0–1)
- `valence` (numerical) — musical positivity; high = upbeat, low = somber (0–1)
- `tempo_bpm` (numerical) — speed of the track in beats per minute
- `danceability` (numerical) — how suited the track is for dancing (0–1)
- `acousticness` (numerical) — organic/acoustic vs. electronic texture (0–1)

### `UserProfile` Fields

- `preferred_genre`, `preferred_mood` — categorical preferences
- `preferred_energy`, `preferred_valence`, `preferred_tempo_bpm`, `preferred_danceability`, `preferred_acousticness` — numeric preferences (0–1 scale)

### Scoring Rule

For numeric features: `score = 1 - |user_preference - song_value|`
For categorical features (`mood`, `genre`): binary match (1 if match, 0 if not)

Weighted sum across all features — `mood` (0.25), `energy` (0.20), `valence` (0.20), `genre` (0.15), `acousticness` (0.10), `tempo_bpm` (0.05), `danceability` (0.05).

### Ranking Rule

All songs scored independently → sorted descending by total score → top N returned.

### Potential Biases

**1. Categorical weight dominance.**
`mood` and `genre` together account for 40% of the total score (0.25 + 0.15). A song that matches your preferred mood and genre can outscore a song with near-perfect numeric values across all five remaining features. Users with niche or cross-genre tastes will be consistently under-served.

**2. Binary categorical penalty.**
Genre and mood scoring is all-or-nothing. A `jazz` song and a `metal` song are penalized equally for a `pop` user, even though one may feel far closer in texture. There is no partial credit for near-miss categories.

**3. Catalog representation bias.**
The system can only recommend what is in `data/songs.csv`. If certain genres, moods, or tempos are overrepresented in the catalog — which reflects whoever curated it — those styles will dominate recommendations regardless of user preference.

**4. No feedback loop.**
The user profile is static. The system never learns that a recommended song was skipped or replayed, so it cannot correct itself. Real recommenders update weights based on behavior; this one does not.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.



## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this


---

## 7. `model_card_template.md`

Combines reflection and model card framing from the Module 3 guidance. :contentReference[oaicite:2]{index=2}  

```markdown
# 🎧 Model Card - Music Recommender Simulation

## 1. Model Name

Give your recommender a name, for example:

> VibeFinder 1.0

---

## 2. Intended Use

- What is this system trying to do
- Who is it for

Example:

> This model suggests 3 to 5 songs from a small catalog based on a user's preferred genre, mood, and energy level. It is for classroom exploration only, not for real users.

---

## 3. How It Works (Short Explanation)

Describe your scoring logic in plain language.

- What features of each song does it consider
- What information about the user does it use
- How does it turn those into a number

Try to avoid code in this section, treat it like an explanation to a non programmer.

---

## 4. Data

Describe your dataset.

- How many songs are in `data/songs.csv`
- Did you add or remove any songs
- What kinds of genres or moods are represented
- Whose taste does this data mostly reflect

---

## 5. Strengths

Where does your recommender work well

You can think about:
- Situations where the top results "felt right"
- Particular user profiles it served well
- Simplicity or transparency benefits

---

## 6. Limitations and Bias

Where does your recommender struggle

Some prompts:
- Does it ignore some genres or moods
- Does it treat all users as if they have the same taste shape
- Is it biased toward high energy or one genre by default
- How could this be unfair if used in a real product

---

## 7. Evaluation

How did you check your system

Examples:
- You tried multiple user profiles and wrote down whether the results matched your expectations
- You compared your simulation to what a real app like Spotify or YouTube tends to recommend
- You wrote tests for your scoring logic

You do not need a numeric metric, but if you used one, explain what it measures.

---

## 8. Future Work

If you had more time, how would you improve this recommender

Examples:

- Add support for multiple users and "group vibe" recommendations
- Balance diversity of songs instead of always picking the closest match
- Use more features, like tempo ranges or lyric themes

---

## 9. Personal Reflection

A few sentences about what you learned:

- What surprised you about how your system behaved
- How did building this change how you think about real music recommenders
- Where do you think human judgment still matters, even if the model seems "smart"

