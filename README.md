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

  The system compares every song to what the user likes and gives it a score. Each song is judged on four things: genre, mood, energy, and acousticness. The user profile stores a favorite genre, a favorite mood, a target energy level, and whether they like acoustic music. A genre match earns 2 points and a mood match earns 1. Energy earns up to 1 point based on how close the song is to the user’s target so songs that are too high or too low both lose points. Acousticness adds up to half a point depending on whether the user likes acoustic sounds. The points are added into a total out of 4.5, the songs are sorted from highest to lowest and the top 5 are recommended along with the reasons each one scored well.

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
| Genre | 1.5 if the song's genre matches `favorite_genre`, otherwise 0 | 1.5 |
| Mood | 1.0 if the song's mood matches `favorite_mood`, otherwise 0 | 1.0 |
| Energy | 1.5 × (1 − \|song energy − target energy\|) | 1.5 |
| Acoustic | 0.5 × acousticness if `likes_acoustic` is True, otherwise 0.5 × (1 − acousticness) | 0.5 |

**Equation 1: Total score**

score = genre points + mood points + energy points + acoustic points

The maximum score is 4.5. The energy rule rewards closeness to the target, so a song that is too energetic loses points the same way a song that is too calm does.

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

Paste a sample of your recommender's output here as a text block so a reader can see what it produces:
```
Top 5 recommendations
========================================
1. Sunrise City by Neon Echo
   Score: 4.38 / 4.5
   Reasons:
     - genre match (+1.5)
     - mood match (+1.0)
     - energy fit (+1.47)
     - acoustic fit (+0.41)

2. Gym Hero by Max Pulse
   Score: 3.28 / 4.5
   Reasons:
     - genre match (+1.5)
     - energy fit (+1.30)

3. Rooftop Lights by Indigo Parade
   Score: 2.77 / 4.5
   Reasons:
     - mood match (+1.0)
     - energy fit (+1.44)
     - acoustic fit (+0.33)

4. Concrete Crown by Kilo Verse
   Score: 1.91 / 4.5
   Reasons:
     - energy fit (+1.47)
     - acoustic fit (+0.44)

5. Fuego Lento by Los Brillantes
   Score: 1.85 / 4.5
   Reasons:
     - energy fit (+1.50)
     - acoustic fit (+0.35)
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



