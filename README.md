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

## How The System Works

Explain your design in plain language.

  The system compares every song to what the user likes and gives it a score. Each song is judged on four things: genre, mood, energy, and acousticness. The user profile stores a favorite genre, a favorite mood, a target energy level, and whether they like acoustic music. A genre match earns 0.75 points and a mood match earns 1. Energy earns up to 3 points based on how close the song is to the user’s target so songs that are too high or too low both lose points. Acousticness adds up to half a point depending on whether the user likes acoustic sounds. The points are added into a total out of 5.25, the songs are sorted from highest to lowest and the top 5 are recommended along with the reasons each one scored well.

Some prompts to answer:

- What features does each `Song` use in your system
  - For example: genre, mood, energy, tempo
- What information does your `UserProfile` store
- How does your `Recommender` compute a score for each song
- How do you choose which songs to recommend

You can include a simple diagram or bullet list if helpful.

Updated design and Finalized Algorithm Recipe
  ### Algorithm Recipe

**Inputs**
- `songs.csv`: 20 songs, each with genre, mood, energy, and acousticness used for scoring
- User profile: `favorite_genre`, `favorite_mood`, `target_energy`, `likes_acoustic`
- `k`: number of songs to recommend, default 5

**Scoring rules for one song**

| Rule | Calculation | Max points |
|---|---|---|
| Genre | 0.75 if the song's genre matches `favorite_genre`, otherwise 0 | 0.75 |
| Mood | 1.0 if the song's mood matches `favorite_mood`, otherwise 0 | 1.0 |
| Energy | 3.0 × (1 − \|song energy − target energy\|) | 3.0 |
| Acoustic | 0.5 × acousticness if `likes_acoustic` is True, otherwise 0.5 × (1 − acousticness) | 0.5 |

**Equation 1: Total score**

score = genre points + mood points + energy points + acoustic points

The maximum score is 5.25. The energy rule rewards closeness to the target, so a song that is too energetic loses points the same way a song that is too calm does.

**Steps**
1. Load every song from `songs.csv`.
2. Score each song using the four rules and save a reason for each rule that added points.
3. Sort all songs from highest score to lowest. Ties keep their order from the CSV.
4. Return the top `k` songs with their scores and reasons.


### Potential Biases

- **Exact matching:** genre and mood only score when the words match exactly. "indie pop" earns nothing for a pop fan, and "relaxed" earns nothing for a chill listener, even though both are close.
- **Genre still dominates:** a song outside the favorite genre can earn at most 3.0 points. For a lofi listener, every lofi song still outranks every non-lofi song, even ones that fit the mood and energy better.
- **Uneven catalog:** lofi has 3 songs while most genres have only 1. Listeners of smaller genres get one strong match, and the rest of their list is filled by energy alone.
- **Double counting energy:** acousticness and energy are strongly linked in this dataset, so the acoustic rule partly rewards the same trait twice.
- **One taste per user:** the profile holds one genre and one mood, so a listener who enjoys both rock and jazz cannot be represented.
- **No variety:** the same profile always gets the same top 5, so the system never suggests something new to explore.

---

## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python3 -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Top 5 results from running `python3 src/main.py` with the current weights (genre 0.75, mood 1.0, energy 3.0, acoustic 0.5; max 5.25), one block per profile. The first three are standard profiles; the rest are adversarial edge cases.

### High-Energy Pop

```
== High-Energy Pop ==
   genre=pop, mood=happy, energy=0.9, acoustic=False
   1. Sunrise City              4.92  (pop/happy, e=0.82)
   2. Gym Hero                  4.13  (pop/intense, e=0.93)
   3. Rooftop Lights            3.91  (indie pop/happy, e=0.76)
   4. Storm Runner              3.42  (rock/intense, e=0.91)
   5. Bassline Riot             3.31  (edm/energetic, e=0.96)
```

### Chill Lofi

```
== Chill Lofi ==
   genre=lofi, mood=chill, energy=0.35, acoustic=True
   1. Library Rain              5.18  (lofi/chill, e=0.35)
   2. Midnight Coding           4.89  (lofi/chill, e=0.42)
   3. Spacewalk Thoughts        4.25  (ambient/chill, e=0.28)
   4. Focus Flow                3.99  (lofi/focused, e=0.4)
   5. Coffee Shop Stories       3.38  (jazz/relaxed, e=0.37)
```

### Deep Intense Rock

```
== Deep Intense Rock ==
   genre=rock, mood=intense, energy=0.92, acoustic=False
   1. Storm Runner              5.17  (rock/intense, e=0.91)
   2. Gym Hero                  4.44  (pop/intense, e=0.93)
   3. Bassline Riot             3.37  (edm/energetic, e=0.96)
   4. Iron Verdict              3.33  (metal/angry, e=0.97)
   5. Sunrise City              3.11  (pop/happy, e=0.82)
```

### ADVERSARIAL: Sad but max energy

```
== ADVERSARIAL: Sad but max energy ==
   genre=blues, mood=sad, energy=0.9, acoustic=False
   1. Storm Runner              3.42  (rock/intense, e=0.91)
   2. Gym Hero                  3.39  (pop/intense, e=0.93)
   3. Empty Barstool            3.31  (blues/sad, e=0.38)
   4. Bassline Riot             3.31  (edm/energetic, e=0.96)
   5. Iron Verdict              3.27  (metal/angry, e=0.97)
```

### ADVERSARIAL: Genre/mood not in catalog

```
== ADVERSARIAL: Genre/mood not in catalog ==
   genre=k-pop, mood=euphoric, energy=0.5, acoustic=True
   1. Velvet Hours              3.20  (r&b/romantic, e=0.5)
   2. Dirt Road Letters         3.17  (country/nostalgic, e=0.55)
   3. Midnight Coding           3.11  (lofi/chill, e=0.42)
   4. Focus Flow                3.09  (lofi/focused, e=0.4)
   5. Coffee Shop Stories       3.05  (jazz/relaxed, e=0.37)
```

### ADVERSARIAL: Energy fence-sitter

```
== ADVERSARIAL: Energy fence-sitter ==
   genre=jazz, mood=relaxed, energy=0.5, acoustic=False
   1. Coffee Shop Stories       4.41  (jazz/relaxed, e=0.37)
   2. Velvet Hours              3.30  (r&b/romantic, e=0.5)
   3. Dirt Road Letters         3.02  (country/nostalgic, e=0.55)
   4. Island Morning            2.95  (reggae/playful, e=0.6)
   5. Midnight Coding           2.90  (lofi/chill, e=0.42)
```

### ADVERSARIAL: Out-of-range energy (5.0)

Target energy is clamped to 0–1, so 5.0 behaves like 1.0.

```
== ADVERSARIAL: Out-of-range energy (5.0) ==
   genre=edm, mood=energetic, energy=5.0, acoustic=False
   1. Bassline Riot             5.12  (edm/energetic, e=0.96)
   2. Iron Verdict              3.39  (metal/angry, e=0.97)
   3. Gym Hero                  3.27  (pop/intense, e=0.93)
   4. Storm Runner              3.18  (rock/intense, e=0.91)
   5. Sunrise City              2.87  (pop/happy, e=0.82)
```

### ADVERSARIAL: Calm genre, loud energy

```
== ADVERSARIAL: Calm genre, loud energy ==
   genre=classical, mood=peaceful, energy=1.0, acoustic=False
   1. Iron Verdict              3.39  (metal/angry, e=0.97)
   2. Bassline Riot             3.36  (edm/energetic, e=0.96)
   3. Gym Hero                  3.27  (pop/intense, e=0.93)
   4. Storm Runner              3.18  (rock/intense, e=0.91)
   5. Sunrise City              2.87  (pop/happy, e=0.82)
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

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



