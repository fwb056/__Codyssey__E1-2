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

    def to_dict(self) -> dict:
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint,
        }

    @classmethod
    def from_dict(cls, data: dict):
        return cls(
            question=data.get("question", ""),
            choices=data.get("choices", []),
            answer=data.get("answer", 1),
            hint=data.get("hint", ""),
        )


class QuizGame:

    def __init__(self, filepath: str = "pyGame/state.json"):
        self.filepath = filepath
        self.quizzes: list[Quiz] = []
        self.best_score: int = 0
        self.history: list[dict] = []
        self._load_data()


    def run(self) -> None:
        while True:
            print("\n====================")
            print(" 파이썬 프로그래밍 퀴즈 게임")
            print("====================")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록 보기")
            print("4. 점수 확인")
            print("5. 종료")

            choice = self.get_valid_int("메뉴를 선택하세요 (1-5): ", 1, 5)

            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.list_quizzes()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                print("프로그램을 종료합니다. 이용해 주셔서 감사합니다!")
                self._save_data()
                break


if __name__ == "__main__":
    game = QuizGame()
    game.run()