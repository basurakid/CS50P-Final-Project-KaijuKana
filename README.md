# KaijuKana
    #### Video Demo:  <URL HERE>
    #### Description:

## Description

KaijuKana is an interactive program designed to help users learn and practice Japanese kana characters in a fun and engaging way. Ideal for beginners, it covers both hiragana and katakana, allowing users to choose which groups to focus on. The program randomly selects characters from the chosen groups for the quiz, and users must identify them. After submitting their answers, users receive a score and can review any errors. With a user-friendly GUI, KaijuKana is accessible to everyone, even those unfamiliar with terminal-based applications.

## Prerequisites
The libraries used on this program, as stated on the requirements.txt file are:

- __CustomTkinter:__ version 5.2.2
- __PIL:__ version 10.2.0
- __Pytest:__ version 8.1.1

## Usage
After downloading all files and needed libraries you can run KaijuKana in the terminal using , though I plan to make this program accessible through an exe file sometime in the near future. If using the terminal I don't recommend noVCN as it seems like it crops the window.

1. __Start the program:__

    -Run KaijuKana with the following command:

        `python project.py`

1. __Selection Menu:__

    -Choose which groups you want to be quizzed, you can select individual groups, categories(Main, Dakuten or Combination kana) or the complete Hiragana or Katakana kanas.

    -After selecting the desired groups, just click __Start__ button.

    ![example1-kana_selection](https://github.com/basurakid/CS50P-Final-Project-KaijuKana/assets/92126346/48ecbd36-534b-4b28-a957-0019840b298c)


2. __Answer Quiz:__

    -The program will display your selected kana in random order.

    -Type your answer in Romaji into the input field.

    -When you are done, click the __Submit__ button.

3. __View Results:__

    -After completing the quiz, you will receive a score showing the number of correct answers.

    -Scroll down to review any errors and understand where you made mistakes.

### Tips

- Start by learning the main kana, going one by one with each group, when you are confident enough start quizzing by groups. Practice makes perfect.

- You can change to light or dark mode by clicking the button on the top right corner.

## Project structure
### Main.py
This file contains the core logic of the program, which includes sorting the alphabets into usable structures, selecting the kana for the quiz according to the user's selection, and tracking scores.

-__Kana Sorting:__
The alphabets are stored in two separate CSV files, with groups separated by empty lines. The main function calls sort_csv_structure, which uses the helper create_populate_dictionary by providing it with a file path string. This function opens the CSV using csv.reader and toggles a variable when it encounters an empty line. The next row creates a new key and list in the dictionary. Subsequent rows are added to the list until another empty line is found, indicating a new group.

- __Selection Sorting:__
This function takes the dictionaries created earlier and the window object, using attributes like selected_tab and selected_kana. It searches the dictionary with the appropriate key and adds the list to the quiz_kana, which is already shuffled.

- __Quiz Results:__
This function is called when the submit button is pressed in the GUI. It compares the user's answers to the correct kana, adding 1 to the score for correct answers or adding the wrong answer inputted by the user to a list, so they can review their mistakes.

- __Function Checks:__
Both check_selection and check_answers work similarly. They check if the corresponding window attributes have been assigned values, then call the function that processes those values.

### Class_gui.py

- __Window Class:__
This class is the root of the entire interface. It contains the program's name and a button to switch between light and dark modes. The button's function, change_mode, checks a string and changes the self.mode of the window. It also includes the function that switches frames when an action is performed, by destroying the current frame and creating a new one with the next frame class.

- __Selection Frame:__
This frame is divided into two tabs, each containing a number of checkboxes. Helper functions handle the layout creation, allowing for reusability:

    - __Create_selection_layout__ and __create_checkboxes:__ the first one takes care of the parts of the interface that are shared between both tabs, while the latter is in charge of creating the checkboxes depending on which tab it is with the needed text.

    Also there´s the functions that are binded to buttons like:

    - __Toggle_group__ and __toggle_all:__ the first one makes use of the frames and the .winfo_children to toggle all of the checkboxes after checking the state of the group checkbox. The second one actually calls the group one to toggle all of the tab at the same time.

    - __Start_quiz:__ this function iterates over the given frames and checks their state, adding the text in them to the appropriate window attributes.

- __Quiz Frame:__
The structure on this one is very similar to that of selection frame, with a scrollable_frame in case there are a lot of kanas in the quiz. The creation of the entries and the arranging is very similar to that of create_checkboxes, making use of divmod to order them. However if there are less than 10 they are assigned quite easily by iterating over them and assigning the values of i in the for loop.

    The submit quiz button on the bottom of the frame works almost exactly the same as start_quiz by checking the frame and passes it on to the window.

- __Score Frame:__
The main focus on this frame is for the user to check their score and see their errors, so this takes most of the screen space. The score is output both in fraction and percentage. The label on the upper part is interactive, reacting to user score. The godzilla is there to encourage the user when he doesn't do too well and to congratulate him when he gets a good score. The errors can be checked at the bottom of the page and uses the same structure as the entries and labels in quiz frame.


## Development and Creation
### Motivation
In the beginning I didn't quite have a clear idea about what the project would be centered about. However I had two very clear guidelines this project would have to follow:

- __A new skill:__ whatever the project was had to challenge me to learn something new, I wanted to learn something that the CS50P course didn't necesarily teach.

- __Practical Use:__ from the get go I wanted to do something that interested me, something that I would make use of myself, and if possible, a project that could be of use to others.

After a little while of pondering and discarding projects that I thought wouldn't be very practical, either too difficult, or not challenging enough, the project that would be finally came to mind.

I wanted to make a Kana quiz so that I could learn japanese characters myself, as not long ago, I started learning japanese. I wanted to make a GUI for my project, which would mean learning a new skill.

### Planning
Before starting development, I researched popular interface creation libraries for Python. CustomTkinter seemed like one of the most popular and modern GUI creation tools.

With this in mind, I began planning the interface, considering what features to include and what the user would be able to do. I also planned the color palette and overall design.

### Development Process
The first step was creating the basic interface to allow the user to select values to create the quiz. Initially, progress was slow as I had to learn CustomTkinter syntax along the way, dealing with many unexpected outcomes, tracebacks, and moments of frustration.

However, after some time, everything started to make sense. Creating the selection interface took much longer than expected, but I eventually moved on to developing the main function's logic, which involved sorting the CSV files containing the alphabet into usable structures.

One significant challenge was my initial misunderstanding of how difficult it is to return values in CustomTkinter without using classes. This realization forced me to restructure the entire interface into a class-based format, which required learning more about how classes work in Python. This proved to be the best decision I made, as it greatly simplified the remaining work.

Once I transitioned to a class-based structure, I was able to return the user selection and sort it for the quiz, using .after to periodically check when the user started the quiz. This part of the project progressed quickly, and before I knew it, I had completed the quiz answers and scoring functionality.

### Learning Outcomes
Through this project, I learned how to create a GUI using CustomTkinter, which also enhanced my understanding of Tkinter. I improved my problem-solving skills by debugging complex issues and learned how to search for and interpret library documentation and information from other users. Additionally, this project gave me valuable experience in creating educational software.

## Acknowledgments

- **Inspiration:** This project was inspired by [Tofugu](https://www.tofugu.com/), which provides excellent resources for learning Japanese.

- **Tutorials and Guides:** I learned how to use the CustomTkinter library from [Tkinter.com](https://www.youtube.com/@TkinterPython), [Atlas](https://www.youtube.com/watch?v=MvzK9Oguxcg&t=966s) and most of all, [Tom Schimansky](https://customtkinter.tomschimansky.com/), the official CustomTkinter documentation.


