# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
The first time I ran it, I thought that it was supposed to be a number guessing game where it gave me hints on whether I had to guess higher or lower than my previous guess. However, as I finished the game, I realized there were bugs in the code that made the game not work.
- List at least two concrete bugs you noticed at the start  
The "new game" button does not result in a new game. When I pressed it, I expected it to start a new game but it stayed on the screen that showed I failed the challenge. The 2nd bug I noticed was that the hints were backwards. The hints showed that I had to guess a higher number when in reality, I had to guess a lower number.
  (for example: "the hints were backwards").

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|  50   |    guess higher   |     guess lower         No error shown         The secret number was 77
| pressed|   
| new game|  Make a new game       Kept exact        No error shown
| button  |     to play           same screen
| 50     |    guess lower         guess higher        No error show          The secret number was 24

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
Claude
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
