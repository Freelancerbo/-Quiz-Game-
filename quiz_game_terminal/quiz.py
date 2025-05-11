import json
import random

class Quiz:
    def __init__(self, filename):
        with open(filename, 'r') as f:
            self.questions = json.load(f)
        random.shuffle(self.questions)

    def run(self):
        score = 0
        for item in self.questions:
            print(f"\n{item['prompt']}")
            options = item['options'][:]  # copy
            random.shuffle(options)
            for idx, opt in enumerate(options, 1):
                print(f"  {idx}. {opt}")
            try:
                choice = int(input("Your answer (1-4): "))
                selected = options[choice - 1]
                if selected.lower() == item['answer'].lower():
                    print(" Correct!")
                    score += 1
                else:
                    print(f" Wrong! Correct answer: {item['answer']}")
            except (ValueError, IndexError):
                print(f" Invalid! Correct answer: {item['answer']}")
        print(f"\n🏁 Quiz finished! You scored {score}/{len(self.questions)}.")