# KaijuKana
    #### Video Demo:  <URL HERE>
    #### Description:

## Description

KaijuKana is an interactive program designed to help users learn and practice Japanese kana characters in a fun and engaging way. Ideal for beginners, it covers both hiragana and katakana, allowing users to choose which groups to focus on. The program randomly selects characters from the chosen groups for the quiz, and users must identify them. After submitting their answers, users receive a score and can review any errors. With a user-friendly GUI, KaijuKana is accessible to everyone, even those unfamiliar with terminal-based applications.

## Prerequisites
The libraries used on this program, as stated on the requirements.txt file are:

- __CustomTkinter__: version 5.2.2
- __PIL__: version 10.2.0
- __Pytest__: version 8.1.1

## Usage
After downloading all files and needed libraries you can run KaijuKana in the terminal using , though I plan to make this program accessible through an .exe file sometime in the near future.
### Running the program
1. __Start the program__:

    -Run KaijuKana with the following command:

        `python project.py`

1. __Selection Menu__:

    -Choose which groups you want to be quizzed, you can select individual groups, categories(Main, Dakuten or Combination kana) or the complete Hiragana or Katakana kanas.

    -After selecting the desired groups, just click __Start__ button.

2. __Answer Quiz__:

    -The program will display your selected kana in random order.

    -Type your answer in Romaji into the input field.

    -When you are done, click the __Submit__ button.

3. __View Results__:

    -After completing the quiz, you will receive a score showing the number of correct answers.

    -Scroll down to review any errors and understand where you made mistakes.

### Example Session
1. __Start the Program__:

    `python kaijukana.py`

2. __Select Kana Groups__:

    -Choose "あ/a" to be quizzed about these kana.

    -Select "Start Quiz"



3. __Answer Quiz Questions__:

    -The program shows: "あ"

    -Type "a" and press "Submit".

4. __View Results__:

    -After submitting all answers, the program displays your score.

    -Example Output: "Score: 1/5. 20.0%"

    -Errors: "あ -> a (Correct), お -> "e" (Incorrect, correct answer: o)"

### Tips

- Start by learning the main kana, going one by one with each group, when you are confident enough start quizzing by groups. Practice makes perfect.

- You can change to light or dark mode by clicking the button on the top right corner.

## CustomTkinter
I wanted to create a project that would allow me to learn a new skill, so when I decided on doing a quiz program
