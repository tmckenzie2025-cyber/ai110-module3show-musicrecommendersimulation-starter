# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

**EnergyMatch 1.0**

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

It suggests the top 5 songs from a small catalog based on a listener's favorite genre, mood, energy level and whether they like acoustic music. It assumes each user has one favorite genre and one favorite mood and knows what energy level they want. It is built for classroom exploration and not for real users.

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

Every song gets a score based on how well it matches the listener. A matching genre adds a little and a matching mood adds a bit more. Energy counts the most and a song earns more points the closer its energy is to what the listener wants. Acoustic sound adds a small bonus if the listener likes it. The scores are added up and the top 5 songs are recommended with the reasons they scored well. The starter code just returned the first songs in the list. I added the scoring, cut the genre weight in half, doubled the energy weight and kept energy targets between 0 and 1 so a bad input like 5.0 can't break the scores.

---

## 4. Data  

Describe the dataset the model uses.  

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

The catalog has 20 songs. I added 10 songs to the starter file to bring in new genres and moods. It covers 17 genres like pop, lofi, rock, jazz, metal, country and latin and 16 moods like happy, chill, intense, sad and romantic. Most genres only have one song while lofi has three. It is missing lyrics, language, tempo preferences and any idea of what a listener has already heard.

---

## 5. Strengths  

Where does your system seem to work well  

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

It works best for listeners with a clear energy level and a well stocked genre like Chill Lofi. Opposite listeners like High-Energy Pop and Chill Lofi get completely different lists which matches my intuition. When a song matches genre, mood and energy it lands at #1 every time like Library Rain for lofi and Storm Runner for rock.

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

Weakness: The energy gap favors quiet acoustic songs and leaves mid-energy listeners with very few real matches. Energy and acousticness were almost perfect opposites in the catalog (correlation −0.98) so the acoustic rule mostly repeated the energy rule. Across 2,720 synthetic profiles quiet songs like Spacewalk Thoughts made the top 5 about 42% of the time while loud songs like Iron Verdict only made it 13% of the time. Only three of the 20 songs fall between 0.45 and 0.70 energy so a listener targeting 0.5 mostly gets filler. A single target_energy also can’t handle someone who wants calm music for sleep and intense music for the gym because the averaged target sends them to the middle songs they like least.

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

#	Profile	    Genre	  Mood	 Target energy	 Likes acoustic
1	High-Energy Pop	pop	 happy	 0.9	            No
2	Chill Lofi	lofi	 chill	 0.35	            Yes
3	Deep Intense Rock	rock	 intense	 0.92	            No


**Profile comparisons (current weights: genre 0.75, mood 1.0, energy 3.0, acoustic 0.5)**

*High-Energy Pop vs Chill Lofi:* These two lists share zero songs because one listener wants loud music and the other wants quiet music. Energy counts the most in the score so it pulls the two lists far apart right away. The lofi listener also wants acoustic songs and the pop listener does not. The lofi list stays strong further down because the catalog has more songs labeled lofi or chill. The pop list runs out of good matches by the 4th and 5th spot and fills them with songs that are just loud.

*High-Energy Pop vs Deep Intense Rock:* Both listeners want loud music so their lists share four of the same songs and the genre and mood labels decide the order. Gym Hero is a good example of why a workout song keeps showing up for someone who just wants happy pop. It is labeled pop and it is very loud so it gets the genre point and the big energy points even though its mood is intense instead of happy. Energy is weighted so heavily that matching loudness matters more than matching the mood. Rock has only one song in the catalog so the rock list fills its last three spots with loud songs that have nothing to do with rock.

*Chill Lofi vs Deep Intense Rock:* These listeners are opposites in both energy and acoustic preference so their lists share no songs. Four of the lofi listener's five songs match lofi or chill. The rock listener only gets one real match and the rest is just loud filler. This shows the catalog is uneven since a lofi fan gets four relevant songs and a rock fan gets one.



Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  ---A song with the wrong energy still won. 
The system gave confident-looking scores with no real match. 
- Any simple tests or comparisons you ran  

I tested the three standard profiles above plus five edge cases: sad but max energy, a genre and mood not in the catalog, a middle energy jazz listener, an out of range energy of 5.0 and a calm genre with loud energy. I looked at whether the top songs actually fit the listener or were only there because of energy. I compared the profiles side by side and ran 2,720 synthetic profiles to see which songs showed up the most.

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

Let users pick more than one genre or mood and give partial credit for close labels like indie pop for a pop fan. Add more songs so every genre has more than one option. Stop the same few songs from filling every list by mixing in something new. Use tempo and valence which are already in the data but not scored.

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
A recommender is really just a scoring rule and the weights decide almost everything. One small weight change can reshuffle the whole top 5.
- Something unexpected or interesting you discovered  The types of filtering companies use. 
- How this changed the way you think about music recommendation apps  - It didn't really change my view because I already felt this way about music apps. I can't stand Apple Music because when I search for a song the recommendations that follow drift away from what I was actually looking for. Building this system showed me why that happens. A few features like energy end up outweighing everything else so the app keeps pushing songs that match on paper but don't feel like the song I started with.
