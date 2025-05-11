from quiz import Quiz


def main():
    print("🎉 Welcome to the Terminal Quiz Game! 🎉")
    quiz = Quiz('questions.json')
    quiz.run()


if __name__ == '__main__':
    main()