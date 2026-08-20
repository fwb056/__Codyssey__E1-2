import json
import os
import random
import sys


class Quiz:

    def __init__(self,
                 question: str,
                 choices: list,
                 answer: int,
                 hint: str = ""):
        self.question = question
        self.choices = choices
        self.answer = answer  # 1~4 번호
        self.hint = hint

    def display(self, number: int) -> None:
        print(f"\n[문제 {number}] {self.question}")
        for idx, choice in enumerate(self.choices, 1):
            print(f"  {idx}. {choice}")

    def check_answer(self, user_answer: int) -> bool:
        return self.answer == user_answer

class QuizGame:

    def __init__(self, filepath: str = "pyGame/state.json"):
        self.filepath = filepath
        self.quizzes: list[Quiz] = []
        self.best_score: int = 0
        self.history: list[dict] = []
        self._load_data()


if __name__ == "__main__":
    game = QuizGame()
    game.run()