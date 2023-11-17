class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer

class Quiz:
    def __init__(self, quiz_questions=None):
        self.quizQuestions = quiz_questions if quiz_questions else []
        self.currentScore = 0
        self.topScores = {}
        self.currentPlayerName = ""

    def playQuestion(self, question):
        print(question.question)
        user_answer = input("Your answer: ").strip().lower()
        if user_answer == question.answer.lower():
            print("Correct!\n")
            self.currentScore += 1
        else:
            print(f"Wrong! The correct answer is {question.answer}\n")

    def displayScore(self):
        print(f"Your final score is: {self.currentScore}")

    def addQuestion(self, question):
        self.quizQuestions.append(question)

    def startGame(self):
        self.currentPlayerName = input("Enter your name: ")
        self.currentScore = 0

        for question in self.quizQuestions:
            self.playQuestion(question)

        self.displayScore()
        self.topScores[self.currentPlayerName] = self.currentScore
        print("Top Scores:")
        for name, score in self.topScores.items():
            print(f"{name}: {score}")


question1 = Question("Is 7 a prime number?", "yes")
question2 = Question("Which of these is a prime number?\nA. 4\nB. 7\nC. 9\nD. 10", "B")

quiz = Quiz([question1, question2])

quiz.startGame()
