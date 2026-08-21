import json
import os
import random
import sys


class Quiz:
    """
    개별 퀴즈 데이터를 표현하는 클래스.
    문제, 선택지, 정답, 힌트를 관리하고 퀴즈 출력 및 정답 확인 기능을 제공합니다.
    """

    def __init__(self,
                 question: str,
                 choices: list,
                 answer: int,
                 hint: str = ""):
        # 퀴즈의 기본 속성 초기화
        self.question = question  # 질문 내용 (str)
        self.choices = choices    # 4지선다 선택지 목록 (list)
        self.answer = answer      # 정답 번호 (1~4 int)
        self.hint = hint          # 힌트 내용 (str, 선택사항)

    def display(self, number: int) -> None:
        """문제 번호와 함께 질문 및 선택지 4개를 콘솔에 출력합니다."""
        print(f"\n[문제 {number}] {self.question}")
        for idx, choice in enumerate(self.choices, 1):
            print(f"  {idx}. {choice}")

    def check_answer(self, user_answer: int) -> bool:
        """사용자가 입력한 정답 번호와 실제 정답을 비교하여 일치 여부를 반환합니다."""
        return self.answer == user_answer

    def to_dict(self) -> dict:
        """Quiz 객체를 state.json에 저장할 수 있도록 딕셔너리 형태로 변환합니다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint,
        }

    @classmethod
    def from_dict(cls, data: dict):
        """JSON에서 읽어온 딕셔너리 데이터를 기반으로 Quiz 객체를 복원/생성합니다."""
        return cls(
            question=data.get("question", ""),
            choices=data.get("choices", []),
            answer=data.get("answer", 1),
            hint=data.get("hint", ""),
        )


class QuizGame:
    """
    퀴즈 게임의 전체 흐름, 파일 입출력, 사용자 입력 예외 처리 등을 총괄하는 클래스.
    """

    def __init__(self, filepath: str = "pyGame/state.json"):
        # 게임 관리 기본 속성 및 데이터 로드
        self.filepath = filepath      # 저장 파일 경로
        self.quizzes: list[Quiz] = [] # 등록된 퀴즈 객체 목록
        self.best_score: int = 0     # 역대 최고 점수
        self.history: list[dict] = [] # 게임 플레이 기록 히스토리
        self._load_data()            # 초기화 시 데이터 자동 불러오기

    def _get_default_quizzes(self) -> list[Quiz]:
        """state.json 파일이 없거나 손상되었을 때 사용할 기본 Git 퀴즈 5개를 제공합니다."""
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
        """
        filepath 위치의 state.json 데이터를 불러옵니다.
        파일이 없거나 JSON 형식 손상 시 기본 퀴즈 데이터로 자동 복구합니다.
        """
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
        """
        현재 퀴즈 목록, 최고 점수, 히스토리를 state.json에 UTF-8 인코딩으로 저장합니다.
        디렉터리가 없으면 os.makedirs로 자동 생성합니다.
        """
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score,
            "history": self.history,
        }
        try:
            dir_name = os.path.dirname(self.filepath)
            if dir_name and not os.path.exists(dir_name):
                os.makedirs(dir_name, exist_ok=True)

            with open(self.filepath, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"\n[!] 데이터 저장 중 오류 발생: {e}")

    def safe_input(self, prompt: str) -> str:
        """
        사용자 입력 도중 Ctrl+C(KeyboardInterrupt) 또는 EOFError 발생 시 
        비정상 종료하지 않고 안전하게 데이터를 저장 후 프로그램을 종료합니다.
        """
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
        """
        범위 내 정수 입력을 검증합니다. 
        문자열, 빈 값, 범위 벗어남 등의 예외 발생 시 안내 메시지 후 재입력을 유도합니다.
        allow_hint=True일 때 'h' 입력 시 -1을 반환합니다.
        """
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
        """
        등록된 퀴즈들을 무작위 순서로 출제하고 점수를 계산합니다.
        풀이 중 'h' 입력 시 힌트를 제공하며, 종료 후 최고 점수 갱신 및 히스토리를 저장합니다.
        """
        if not self.quizzes:
            print("\n[!] 등록된 퀴즈가 없습니다.")
            return

        print("\n=== 퀴즈 풀기 ===")
        shuffled = self.quizzes.copy()
        random.shuffle(shuffled)  # 무작위 순서 출제

        score = 0
        total = len(shuffled)

        for idx, quiz in enumerate(shuffled, 1):
            quiz.display(idx)
            print("  (힌트를 원하시면 'h'를 입력하세요)")
            user_ans = self.get_valid_int("정답 번호 입력 (1-4): ",
                                          1,
                                          4,
                                          allow_hint=True)

            # 힌트 처리 로직
            if user_ans == -1:
                print(f"💡 힌트: {quiz.hint if quiz.hint else '힌트가 없습니다.'}")
                user_ans = self.get_valid_int("정답 번호 입력 (1-4): ", 1, 4)

            # 정답 판정
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
        """사용자로부터 문제, 4개 선택지, 정답, 힌트를 입력받아 새 퀴즈를 등록 및 저장합니다."""
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

    def list_quizzes(self) -> None:
        """현재 등록되어 있는 모든 퀴즈의 질문 목록과 정답 번호를 출력합니다."""
        print("\n=== 퀴즈 목록 ===")
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for idx, q in enumerate(self.quizzes, 1):
            print(f"{idx}. {q.question} (정답: {q.answer}번)")

    def show_score(self) -> None:
        """역대 최고 점수와 최근 5회의 플레이 결과 기록을 보여줍니다."""
        print("\n=== 점수 및 기록 확인 ===")
        print(f"🏆 최고 점수: {self.best_score}점")
        if not self.history:
            print("아직 실행된 게임 기록이 없습니다.")
            return

        print("\n[최근 게임 기록]")
        for idx, h in enumerate(self.history[-5:], 1):
            print(f"  {idx}. {h['total']}문제 중 {h['score']}점")

    def run(self) -> None:
        """메인 메뉴 루프를 실행하며 사용자 입력 선택에 따라 각 기능을 호출합니다."""
        while True:
            print("\n====================")
            print(" Git 기초 퀴즈 게임")
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
    # 게임 인스턴스 생성 및 실행
    game = QuizGame()
    game.run()