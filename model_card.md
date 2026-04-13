# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**MoodMatch 1.0**

---

## 2. Intended Use  

This recommender suggests songs from a catalog based on a listener's personal preferences. It achieves this using predefined-fields from the user like genre, mood etc.

---

## 3. How the Model Works  

Every song has ten features, but the model currently uses four key ones:
- energy
- mood
- genre
- like_acousticness
Each of these features is assigned a weight by the developer, which determines its importance in the scoring process.

When a user provides their preferences, the system compares those preferences with each song’s features individually. Each comparison generates a partial score. These partial scores are then combined and averaged to produce a final score between 0 and 1.

The scoring is dynamic—if a user provides only a subset of features (e.g., two preferences), the final score is calculated using only those inputs.

Songs are then ranked based on their final scores, and the one with the highest score is recommended first.

---

## 4. Data  

The catalog has 18 songs with ten feature i.e id,title,artist,genre,mood,energy,tempo_bpm,valence,danceability,acousticness.
There are 15 genres (e.g pop, lofi, rock, jazz, hip-hop) and 13 moods (e.g happy, chill, intense, melancholic, romantic). The catalog is self and randomly made, and it skews toward calm and intense moods, with little coverage of feelings like nostalgic or bittersweet.

---

## 5. Strengths  

The system works best when a user's preferences match something clearly in the catalog. A gym-goer wanting intense pop gets a strong top result. A late-night lofi listener does too. The system also handles missing preferences well; if a user skips a field, the scoring adjusts without breaking.

---

## 6. Limitations and Bias 

The most significant limitation in this systme is that the user profile is static. The system never learns that a recommended song was skipped or replayed, so it cannot correct itself.
Also there's bias in the system in how mood is scored. Mood carries the highest weight (25%), but matching is all-or-nothing — a song either matches or contributes nothing, even when moods are semantically close like "relaxed" and "chill." This is compounded by the catalog: most moods appear in only one or two of the eighteen songs, so users with niche preferences will almost always lose a quarter of their total score. A "chill" listener benefits from three matching songs, while a "nostalgic" or "romantic" listener has exactly one option before the score collapses. The system therefore creates a quiet filter bubble — not by blocking content, but by quietly rewarding users whose tastes happen to align with the catalog's dominant moods.

---

## 7. Evaluation  

I tested six listener profiles: 
- a gym-goer wanting intense pop
- a late-night study session with calm lofi
- an evening unwind with r&b, 
plus three edge cases:
- a mood-only preference
- a contradictory request
- a genre (country) that doesn't exist in my catalog. For each profile, I looked for whether the top result was an obvious fit and whether the remaining picks felt like reasonable alternatives or just filler. The everyday profiles — gym session and late-night study — passed easily, but the evening unwind profile had only one truly matching song, so I watched whether the rest of the list held up or fell apart after it.
The mood only profile was revealing in that it shows how the systems reacts when it has little to not information both from the user and it's own data. The recommender perfectly matched the two happy songs in the catalog with perfect scores and ranked them first, but every other song scored exactly zero. The remaining three spots were filled by whichever songs appeared first in the data file, not because they were a good fit. This showed how fragile the recommendations become when a user gives too little information or when the data file is limited.

---

## 8. Future Work  

The biggest improvement would be partial mood matching. Right now "relaxed" and "chill" are treated as completely different, which is unfair. Grouping similar moods together would fix that. The catalog also needs more songs, especially in underrepresented genres and moods, expanding it would immediately make recommendations more meaningful. Letting users rate recommendations so the system learns over time would also help. Finally, A diversity rule would prevent the top five from being dominated by one genre or artist when the user's preferences are broad. It would also be worth testing different scoring models — for example, comparing this weighted-feature approach against a collaborative one that recommends based on what similar listeners enjoyed.

---

## 9. Personal Reflection  

Building this made me realize how many invisible decisions go into a recommender. Choosing how much weight to give mood versus energy is already a design choice that quietly favors some users over others. That made me think differently about how apps like Spotify shape what music people discover without them ever noticing.
