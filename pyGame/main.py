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
            Quiz(
                "Git에서 로컬 저장소를 새로 초기화하여 생성할 때 사용하는 명령어는?",
                ["git init", "git clone", "git push", "git status"],
                1,
                "Initialization의 약자입니다."
            ),
            Quiz(
                "작업 디렉터리의 변경 사항을 Staging Area(수정 대기 영역)에 추가하는 명령어는?",
                ["git commit", "git status", "git add", "git checkout"],
                3,
                "파일을 '추가'한다는 의미의 영단어입니다."
            ),
            Quiz(
                "원격 저장소(GitHub)의 변경 사항을 가져와 현재 로컬 브랜치와 병합하는 명령어는?",
                ["git fetch", "git pull", "git push", "git clone"],
                2,
                "가져와서 끌어당긴다(pull)는 의미입니다."
            ),
            Quiz(
                "현재 작업 중인 브랜치 목록을 확인하거나 새 브랜치를 만들 때 사용하는 명령어는?",
                ["git branch", "git merge", "git log", "git diff"],
                1,
                "'가지/나뭇가지'라는 뜻을 가진 영단어입니다."
            ),
            Quiz(
                "로컬 저장소의 커밋 내역(히스토리)을 원격 저장소로 업로드할 때 사용하는 명령어는?",
                ["git fetch", "git pull", "git push", "git commit"],
                3,
                "서버로 밀어 넣는(push) 동작입니다."
            )
        ]

    def _load_data(self) -> None:
        if not os.path.exists(self.filepath):
            self.quizzes = self._get_default_quizzes()
            self._save_data()
            return

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.quizzes = [
                    Quiz.from_dict(q) for q in data.get("quizzes", [])
                ]
                self.best_score = data.get("best_score", 0)
                self.history = data.get("history", [])
                if not self.quizzes:
                    self.quizzes = self._get_default_quizzes()
        except Exception:
            print("\n[!] state.json 파일이 손상되어 기본 퀴즈 데이터로 복구합니다.")
            self.quizzes = self._get_default_quizzes()
            self.best_score = 0
            self.history = []
            self._save_data()

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

    def safe_input(self, prompt: str) -> str:
        try:
            return input(prompt).strip()
        except (KeyboardInterrupt, EOFError):
            print("\n\n[!] 입력이 중단되었습니다. 데이터를 저장하고 안전하게 종료합니다.")
            self._save_data()
            sys.exit(0)

    def get_valid_int(self,
                      prompt: str,
                      min_val: int,
                      max_val: int,
                      allow_hint: bool = False) -> int:
        while True:
            val_str = self.safe_input(prompt)
            if allow_hint and val_str.lower() == "h":
                return -1
            if not val_str:
                print("입력값이 비어 있습니다. 다시 입력해주세요.")
                continue
            try:
                val = int(val_str)
                if min_val <= val <= max_val:
                    return val
                print(f"{min_val}~{max_val} 사이의 숫자만 입력 가능합니다.")
            except ValueError:
                print("올바른 숫자를 입력해주세요.")

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

    def add_quiz(self) -> None:
        print("\n=== 퀴즈 추가 ===")
        question = self.safe_input("문제 내용 입력: ")
        while not question:
            print("문제 내용은 필수입니다.")
            question = self.safe_input("문제 내용 입력: ")

        choices = []
        for i in range(1, 5):
            c = self.safe_input(f"선택지 {i} 입력: ")
            while not c:
                print("선택지는 필수입니다.")
                c = self.safe_input(f"선택지 {i} 입력: ")
            choices.append(c)

        answer = self.get_valid_int("정답 번호 입력 (1-4): ", 1, 4)
        hint = self.safe_input("힌트 입력 (선택사항, 없으면 Enter): ")

        new_quiz = Quiz(question, choices, answer, hint)
        self.quizzes.append(new_quiz)
        self._save_data()
        print("✅ 퀴즈가 성공적으로 추가되었습니다.")


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