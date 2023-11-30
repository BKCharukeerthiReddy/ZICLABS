class Question:
    def __init__(self, question, choices, correct_choice):
        self.question = question
        self.choices = choices
        self.correct_choice = correct_choice

    def ask_question(self):
        print(self.question)
        for i, choice in enumerate(self.choices, start=1):
            print(f"{i}. {choice}")

        user_choice = int(input("Enter the number of your choice: "))
        if user_choice == self.correct_choice:
            print("Correct!\n")
            return 1
        else:
            print("Incorrect!\n")
            return 0

def main():
    questions = [
        Question("What is the capital of Australia?", ["Sydney", "Melbourne", "Canberra", "Perth"], 3),
        Question("Which gas do plants absorb during photosynthesis?", ["Oxygen", "Carbon Dioxide", "Nitrogen", "Hydrogen"], 2),
        Question("Who painted the Mona Lisa?", ["Vincent van Gogh", "Leonardo da Vinci", "Pablo Picasso", "Claude Monet"], 2),
        Question("In what year did the Titanic sink?", ["1912", "1920", "1905", "1935"], 1),
        Question("What is the currency of Japan?", ["Yen", "Won", "Ringgit", "Baht"], 1)
    ]

    score = sum(question.ask_question() for question in questions)

    print(f"You scored {score}/{len(questions)}!")

if __name__ == "__main__":
    main()
