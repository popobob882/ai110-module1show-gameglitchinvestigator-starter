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
|  50   |    guess higher( The secret number was 77)   |   guess lower   |      No error shown     |
| pressed new game button | Make a new game |  Kept exact same screen |   No error shown   |      
| 50     |    guess lower(The secret number was 24)  |       guess higher |        No error show |         

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?

The only AI tool I used is Claude for this project

- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).

An example of an AI suggestion that was correct was when the AI suggested that I needed to add a line that tells the computer the status of the game before the st.rerun activates. This was a suggestion I decided to keep as I realized that the AI was right in the fact that the previous code only reset the amount of attempts and picjed a new secret number, but the game status was never changed and still stuck on the "lost" or "won" screen. So by adding this line of code, it will allow the new game button to actually work. I was able to verify this first by asking the AI to help me write a pytest for this line. Once I verified that everything seemed to be correct, I tested the test case and it returned true so it gave me the confidence to try the actual game. Then where I tried the actual game, the new game button worked which verified that the new code added worked in my favor.

- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

One example of an AI suggestion that was incorrect was when I tried to fix the number ranges for the different difficulties. I realized that the hard difficulty was less than that of normal and that no matter what difficulty you chose in the game, the range of numbers was always from 1 - 100. So I asked the AI to help me change it. The error happened when it imported the get_range_for_difficulty function into logic_utils.py. I realized that while the rest of the code did seem to work, the main issue of the number range for the hard difficulty did not change at all and was still kept at 1 - 50. As a result, I had to change that myself. I tried verifying it by writing the test cases with AI and thosed worked. However, when I tried to play the actual game, the game was actually broken. I was then unable to figure out the reason behind the game breaking even with AI and as a result, I decided the best case for me in this case would be to revert everything back as to not break the game.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
The first step I did was to have AI help me write the test cases to see if the change would theoretically work. Once all the test cases passed, I played the game myself at least 3 times to make sure that the bug did not appear in the game.
- Describe at least one test you ran (manual or using pytest) and what it showed you about your code.
One test that I ran was the difficulty ranges and seeing if it actually changed the ranges when selecting the different difficulty options. Those passed but when I tested it manually, I realized that the game broke. This made me realize that just test cases by itself is not actually a surefire way to see if the code actually worked.
- Did AI help you design or understand any tests? How?
Yes, I did us AI to help me design and understand the different test cases. I first asked AI to help me write the test cases. Then I looked over the test cases and anything I did not understand, I asked AI what that line actually represents and why its added in the code. If I found that the logic of the test case was wrong, I told AI to fix that specific part of the logic.Once I fully understood everything and I verified everything is correct. I then allowed AI to actually make changes to the code.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
