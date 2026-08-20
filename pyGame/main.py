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

    def _get_default_quizzes(self) -> list[Quiz]:
        return [
            Quiz("파이썬에서 가변(Mutable) 객체에 해당하는 것은?",
                 ["int", "str", "list", "tuple"], 3, "추가/삭제가 가능한 자료형입니다."),
            Quiz(
                "클래스 내부에서 인스턴스 자신을 가리키는 첫 번째 매개변수 이름은?",
                ["self", "cls", "this", "super"], 1,
                "관례적으로 '자기 자신'을 뜻합니다."),
            Quiz("JSON 형식으로 데이터를 파일에 쓸 때 사용하는 함수는?",
                 ["json.loads()", "json.dump()", "json.load()", "json.dumps()"],
                 2, "파일(File)에 쓰므로 짧은 이름의 함수입니다."),
            Quiz(
                "Git에서 로컬 저장소를 새로 생성할 때 사용하는 명령어는?",
                ["git init", "git clone", "git push", "git commit"], 1,
                "Initialization의 약자입니다."),
            Quiz("파이썬에서 예외 처리를 위해 사용하는 키워드는?",
                 ["try / catch", "try / except", "do / except", "if / error"],
                 2, "파이썬은 catch 대신 이 단어를 사용합니다."),
        ]


    def _save_data(self) -> None:
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
            "history": self.history,
        }
        try:
            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"\n[!] 데이터 저장 중 오류 발생: {e}")


    def play_quiz(self) -> None:
        if not self.quizzes:
            print("\n[!] 등록된 퀴즈가 없습니다.")
            return

        print("\n=== 퀴즈 풀기 ===")
        shuffled = self.quizzes.copy()
        random.shuffle(shuffled)

        score = 0
        total = len(shuffled)

        for idx, quiz in enumerate(shuffled, 1):
            quiz.display(idx)
            print("  (힌트를 원하시면 'h'를 입력하세요)")
            user_ans = self.get_valid_int("정답 번호 입력 (1-4): ",
                                          1,
                                          4,
                                          allow_hint=True)

            if user_ans == -1:
                print(f"💡 힌트: {quiz.hint if quiz.hint else '힌트가 없습니다.'}")
                user_ans = self.get_valid_int("정답 번호 입력 (1-4): ", 1, 4)

            if quiz.check_answer(user_ans):
                print("⭕ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다. (정답: {quiz.answer}번)")

        print(f"\n[결과] {total}문제 중 {score}개를 맞히셨습니다!")
        if score > self.best_score:
            print(f"🎉 축하합니다! 최고 점수를 갱신했습니다 ({self.best_score} -> {score})")
            self.best_score = score

        self.history.append({"score": score, "total": total})
        self._save_data()



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