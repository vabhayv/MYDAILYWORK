import random

def run_quiz():
    print("===================================")
    print("      Welcome to the Quiz Game!    ")
    print("===================================")
    print("Rules:")
    print("1. Type the correct option (A/B/C/D) for multiple choice.")
    print("2. Type your answer for fill-in-the-blank questions.")
    print("3. Each correct answer gives you 1 point.\n")


    questions = [

    {
        "type": "mcq",
        "question": "Who created Python?",
        "options": ["A. Dennis Ritchie", "B. Guido van Rossum", "C. James Gosling", "D. Bjarne Stroustrup"],
        "answer": "B"
    },
    {
        "type": "fill",
        "question": "Python was first released in the year _______.",
        "answer": "1991"
    },
    {
        "type": "mcq",
        "question": "Which keyword is used to create a function in Python?",
        "options": ["A. function", "B. def", "C. fun", "D. define"],
        "answer": "B"
    },
    {
        "type": "mcq",
        "question": "Which data type is immutable?",
        "options": ["A. list", "B. dictionary", "C. string", "D. set"],
        "answer": "C"
    },
    {
        "type": "fill",
        "question": "The symbol used for comments in Python is _______.",
        "answer": "#"
    },
    {
        "type": "mcq",
        "question": "Which function is used to get input from the user?",
        "options": ["A. get()", "B. input()", "C. scan()", "D. read()"],
        "answer": "B"
    },
    {
        "type": "fill",
        "question": "The output function in Python is called _______.",
        "answer": "print"
    },
    {
        "type": "mcq",
        "question": "Which data structure uses key-value pairs?",
        "options": ["A. List", "B. Tuple", "C. Dictionary", "D. Set"],
        "answer": "C"
    },
    {
        "type": "mcq",
        "question": "Which loop is used when the number of iterations is known?",
        "options": ["A. while loop", "B. for loop", "C. do-while loop", "D. infinite loop"],
        "answer": "B"
    },
    {
        "type": "fill",
        "question": "The correct file extension for Python files is _______.",
        "answer": ".py"
    },
    {
        "type": "mcq",
        "question": "Which operator is used for exponentiation?",
        "options": ["A. ^", "B. **", "C. //", "D. %"],
        "answer": "B"
    },
    {
        "type": "mcq",
        "question": "What is the output of type(5)?",
        "options": ["A. int", "B. float", "C. str", "D. bool"],
        "answer": "A"
    },
    {
        "type": "fill",
        "question": "A list in Python is created using _______ brackets.",
        "answer": "square"
    },
    {
        "type": "mcq",
        "question": "Which of the following is used to handle exceptions?",
        "options": ["A. try-except", "B. if-else", "C. for loop", "D. switch"],
        "answer": "A"
    },
    {
        "type": "mcq",
        "question": "Which keyword is used to create a class?",
        "options": ["A. function", "B. object", "C. class", "D. define"],
        "answer": "C"
    },
    {
        "type": "fill",
        "question": "Tuples are _______ (mutable/immutable).",
        "answer": "immutable"
    },
    {
        "type": "mcq",
        "question": "Which method adds an item to a list?",
        "options": ["A. insert()", "B. append()", "C. add()", "D. push()"],
        "answer": "B"
    },
    {
        "type": "mcq",
        "question": "What does len() function return?",
        "options": ["A. Type of variable", "B. Length of object", "C. Last element", "D. None"],
        "answer": "B"
    },
    {
        "type": "fill",
        "question": "Python supports _______ programming (object-oriented/procedural).",
        "answer": "object-oriented"
    },
    {
        "type": "mcq",
        "question": "Which keyword is used to exit a loop?",
        "options": ["A. stop", "B. break", "C. exit", "D. return"],
        "answer": "B"
    }]


    random.shuffle(questions)

    score = 0

    for q in questions:
        print("\n" + q["question"])

        if q["type"] == "mcq":
            for option in q["options"]:
                print(option)

            user_answer = input("Your answer: ").strip().upper()

            if user_answer == q["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print("❌ Incorrect.")
                print("Correct answer is:", q["answer"])

        elif q["type"] == "fill":
            user_answer = input("Your answer: ").strip().lower()

            if user_answer == q["answer"]:
                print("✅ Correct!")
                score += 1
            else:
                print("❌ Incorrect.")
                print("Correct answer is:", q["answer"])
              
    print("\n===================================")
    print("            Quiz Finished!         ")
    print("===================================")
    print("Your final score is:", score, "out of", len(questions))

    percentage = (score / len(questions)) * 100

    if percentage == 100:
        print("Outstanding performance!")
    elif percentage >= 70:
        print("Great job!")
    elif percentage >= 40:
        print("Good effort! Keep practicing!")
    else:
        print("Keep learning and try again!")

def main():
    while True:
        run_quiz()
        play_again = input("\nDo you want to play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break

main()
