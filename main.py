import json
import os

def load_questions(filename="quiz.json"):
    """
    Loads quiz questions from a JSON file.
    Returns a list of question dictionaries.
    """
    try:
        with open(filename, 'r') as file:
            questions = json.load(file)
        return questions
    except FileNotFoundError:
        print(f"Error: The file {filename} was not found.")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode the JSON from {filename}.")
        return []

def run_quiz(questions):
    """
    Runs the quiz, tracks the score, and prints the final result.
    """
    if not questions:
        print("No questions loaded. Exiting quiz.")
        return

    score = 0
    total_questions = len(questions)

    # Clear the screen for a clean start
    os.system('cls' if os.name == 'nt' else 'clear')
    
    print("Welcome to the Command-Line Quiz Engine!")
    print(f"You will be asked {total_questions} questions.\n")
    
    # Use enumerate to get both the index (for question number) and the question object
    for index, q in enumerate(questions):
        print(f"--- Question {index + 1} of {total_questions} ---")
        print(q["question"])
        
        # Print all the options
        for i, option in enumerate(q["options"]):
            print(f"  {i + 1}. {option}")
        
        # Loop for valid user input
        while True:
            try:
                user_input = input(f"Your choice (1-{len(q['options'])}): ")
                # Convert user's 1-based answer to a 0-based index
                user_choice_index = int(user_input) - 1
                
                # Check if the choice is in the valid range
                if 0 <= user_choice_index < len(q["options"]):
                    break  # Valid input, exit loop
                else:
                    print("Invalid choice. Please enter a number from the list.")
            except ValueError:
                print("Invalid input. Please enter a number.")
        
        # Check the answer
        if user_choice_index == q["correct_answer_index"]:
            print("Correct!\n")
            score += 1
        else:
            correct_answer_text = q["options"][q["correct_answer_index"]]
            print(f"Sorry, that's incorrect. The correct answer was: {correct_answer_text}\n")

    # After the loop, show the final score
    print("--- Quiz Complete! ---")
    print(f"Your final score: {score} / {total_questions}")

# --- This is the entry point of our script ---
if __name__ == "__main__":
    quiz_questions = load_questions("quiz.json")
    run_quiz(quiz_questions)
