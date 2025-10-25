Command-Line Quiz Engine

This project is a simple, effective command-line quiz application built in Python.

It demonstrates a core software design concept: the separation of code (logic) from data (content). The Python script (main.py) acts as the "engine," and all quiz questions, options, and answers are stored in a simple quiz.json file.

Concept & Workflow

The tool demonstrates an AI/automation concept through its data workflow:

Data: A structured quiz.json file holds all the quiz content.

Logic: The main.py script contains all the application logic.

Execution: When run, the Python script reads the JSON file, dynamically builds the quiz, asks the user questions, and tabulates a final score.

The "intelligent" part is the design: you can add, remove, or edit questions in the quiz.json file without ever needing to change a single line of Python code. The engine adapts automatically.

Features

Dynamic Content: Reads all questions from quiz.json.

Clean Interface: Clears the terminal screen for a clean user experience.

Input Validation: Robustly checks for invalid user input (e.g., text instead of numbers, or numbers out of range).

Instant Feedback: Tells the user if they were correct or incorrect after each question.

Final Scoring: Provides a total score upon quiz completion.

Zero Dependencies: Runs on any machine with Python 3. No pip install required.

How to Run

Ensure you have Python 3 installed.

Clone this repository (or download the files).

Open your terminal or command prompt.

Navigate to the quiz-engine project folder.

Run the following command:

python main.py


(Note: You may need to use python3 main.py on some systems)

How to Add Questions

Open the quiz.json file.

Copy and paste an existing question block (from { to }).

Add a comma , after the last question block.

Paste the new block and edit the "question", "options", and "correct_answer_index" (remembering that the index starts at 0).

Save the file and run main.py again. Your new question will automatically appear.
