# listof questions 
# store of some answers
# randomly pick questions 
# ask the questions 
# see if they are correct 
# keep track of the score 
# tell the user their score 
# --- EXAMPLE QUESTION DATA ---
# Ensure your actual list looks similar to this, with matching key names.
questions = [
    {
        "question": "What is the capital of France?",
        "option": ["A. Berlin", "B. Madrid", "C. Paris", "D. Rome"],
        "answer": "C"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "option": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    }
]

# --- GAME LOGIC ---
# initial score
score = 0

# go through each question
for i, q in enumerate(questions, start = 1):  # Corrected 'start' typo and used 'q' as loop variable
    # printing the questions headline
    print("\n")
    print(f"Question {i}")
    print(q["question"])  # This exact key "question" must match the dictionary above
    print("-------------------")
    
    # display the options
    for option in q["option"]: # This exact key "option" must match the dictionary above
        print(option)
        
    # take the user answers
    user_answer = input("Enter your answer (A/B/C/D): ").strip().upper()
    
    # Check if the answer is correct
    if user_answer == q["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Wrong! The correct answer was {q['answer']}.")

# Print final score
print("\n===================")
print(f"GAME OVER! Your final score is {score} out of {len(questions)}.")
print("===================")


