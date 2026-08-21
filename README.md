# __Codyssey__E1-2
# [E 1-2] 컴퓨터에게 명령 내리는 말(파이썬) 처음 배우기

## 프로젝트 개요

Python과 Git을 이용하여, 내가 만든 프로그램이 왜 이렇게 동작하는지를 설명하고 그 과정을 기록하자.

  * 터미널에서 동작하는 나만의 퀴즈 게임을 처음부터 끝까지 구현

  * Python 기본 문법을 사용해 입력/출력 흐름을 만들고, 클래스(객체 지향)로 코드를 역할별로 구조화

  * JSON 파일 저장을 통해 프로그램을 종료해도 퀴즈와 점수가 유지되도록 "데이터 영속성"을 경험

  * Git으로 변경 이력을 관리

  * 기능 단위로 커밋, 브랜치를 나눠 작업 후 병합하며, GitHub에 저장소를 공개

커밋이력 확인 : https://github.com/fwb056/__Codyssey__E1-2/commits/main/
---

## 1. 퀴즈 주제 선정 이유
 * 퀴즈 주제: Git 명령어 퀴즈
   
   그동안 프로젝트 경험이 없어 GitHub 사용 경험이 전무했다.
## 2. 실행 방법

```bash
***************@****** __Codyssey__E1-2 % /usr/bin/python3 /Users/***************/__Codyssey__E1-2/pyGame/main.py

====================          ## 퀴즈 로비화면
 파이썬 프로그래밍 퀴즈 게임
====================
1. 퀴즈 풀기
2. 퀴즈 추가
3. 퀴즈 목록 보기
4. 점수 확인
5. 종료
메뉴를 선택하세요 (1-5):


메뉴를 선택하세요 (1-5): 1        ## 1. 퀴즈 풀기

=== 퀴즈 풀기 ===

[문제 1] 원격 저장소(GitHub)의 변경 사항을 가져와 현재 로컬 브랜치와 병합하는 명령어는?     ## 퀴즈 정답 출력
  1. git fetch
  2. git pull
  3. git push
  4. git clone
  (힌트를 원하시면 'h'를 입력하세요)
정답 번호 입력 (1-4): 2
⭕ 정답입니다!

[문제 2] Git에서 로컬 저장소를 새로 초기화하여 생성할 때 사용하는 명령어는?               ## 퀴즈 오답 출력
  1. git init
  2. git clone
  3. git push
  4. git status
  (힌트를 원하시면 'h'를 입력하세요)
정답 번호 입력 (1-4): 2
❌ 오답입니다. (정답: 1번)

[문제 3] 로컬 저장소의 커밋 내역(히스토리)을 원격 저장소로 업로드할 때 사용하는 명령어는?     ## 퀴즈 힌트 출력
  1. git fetch
  2. git pull
  3. git push
  4. git commit
  (힌트를 원하시면 'h'를 입력하세요)
정답 번호 입력 (1-4): h
💡 힌트: 서버로 밀어 넣는 동작입니다.


메뉴를 선택하세요 (1-5): 2        ## 2. 퀴즈 추가

=== 퀴즈 추가 ===
문제 내용 입력: git 명령어 중 수정 이력을 확인하는 명령어는?
선택지 1 입력: git status
선택지 2 입력: git log
선택지 3 입력: git diff
선택지 4 입력: git show
정답 번호 입력 (1-4): 2
힌트 입력 (선택사항, 없으면 Enter): 기록/이력을 뜻하는 영단어이다
✅ 퀴즈가 성공적으로 추가되었습니다.


메뉴를 선택하세요 (1-5): 3        ## 3. 퀴즈 목록 보기

=== 퀴즈 목록 ===
1. Git에서 로컬 저장소를 새로 초기화하여 생성할 때 사용하는 명령어는? (정답: 1번)
2. 작업 디렉터리의 변경 사항을 Staging Area(수정 대기 영역)에 추가하는 명령어는? (정답: 3번)
3. 원격 저장소(GitHub)의 변경 사항을 가져와 현재 로컬 브랜치와 병합하는 명령어는? (정답: 2번)
4. 현재 작업 중인 브랜치 목록을 확인하거나 새 브랜치를 만들 때 사용하는 명령어는? (정답: 1번)
5. 로컬 저장소의 커밋 내역(히스토리)을 원격 저장소로 업로드할 때 사용하는 명령어는? (정답: 3번)
6. git 명령어 중 수정 이력을 확인하는 명령어는? (정답: 2번)


메뉴를 선택하세요 (1-5): 4         ## 4. 점수 확인

=== 점수 및 기록 확인 ===
🏆 최고 점수: 5점

[최근 게임 기록]
  1. 5문제 중 5점
  2. 6문제 중 5점


메뉴를 선택하세요 (1-5): 5          ## 5. 종료
프로그램을 종료합니다. 이용해 주셔서 감사합니다!
```

## 3. 기능 목록

### 클래스 Quiz

```python
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
```

 * 메서드 display
   
```python
    def display(self, number: int) -> None:
        """문제 번호와 함께 질문 및 선택지 4개를 콘솔에 출력합니다."""
        print(f"\n[문제 {number}] {self.question}")
        for idx, choice in enumerate(self.choices, 1):
            print(f"  {idx}. {choice}")
```

 * 메서드 check_answer
   
```python
    def check_answer(self, user_answer: int) -> bool:
        """사용자가 입력한 정답 번호와 실제 정답을 비교하여 일치 여부를 반환합니다."""
        return self.answer == user_answer
```

 * 메서드 to_dict
   
```python
    def to_dict(self) -> dict:
        """Quiz 객체를 state.json에 저장할 수 있도록 딕셔너리 형태로 변환합니다."""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "hint": self.hint,
        }
```

 * 클래스 메서드 from_dict
   
```python
    @classmethod
    def from_dict(cls, data: dict):
        """JSON에서 읽어온 딕셔너리 데이터를 기반으로 Quiz 객체를 복원/생성합니다."""
        return cls(
            question=data.get("question", ""),
            choices=data.get("choices", []),
            answer=data.get("answer", 1),
            hint=data.get("hint", ""),
        )
```

### 클래스 QuizGame
```python
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
```

 * 메서드 _get_default_quizzes
   
```python
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
```

 * 메서드 _load_data
   
```python
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
```

 * 메서드 _save_data
   
```python
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
```

 * 메서드 safe_input
   
```python
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
```

 * 메서드 get_valid_int
   
```python
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
```

 * 메서드 play_quiz
   
```python
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
```

 * 메서드 add_quiz
   
```python
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
```

 * 메서드 list_quizzes
   
```python
    def list_quizzes(self) -> None:
        """현재 등록되어 있는 모든 퀴즈의 질문 목록과 정답 번호를 출력합니다."""
        print("\n=== 퀴즈 목록 ===")
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for idx, q in enumerate(self.quizzes, 1):
            print(f"{idx}. {q.question} (정답: {q.answer}번)")
```

 * 메서드 show_score
   
```python
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
```

 * 메서드 run
   
```python
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
```

## 4. 파일 구조
```
__Codyssey__E1-2/
├── .gitignore
├── README.md
├── Docs/
│   ├── game_play.png       # 프로그램 실행 결과 스크린샷 (퀴즈 추가, 목록, 플레이 등)
│   └── git_graph.png       # git log --oneline --graph 결과 스크린샷
└── pyGame/
    ├── main.py
    └── state.json          # 프로그램 실행 시 pyGame 폴더 내에 자동 생성됨
```

## 5. state.json 필드 설명

| 필드명 | 데이터 타입 | 설명 |
| :--- | :--- | :--- |
| **`quizzes`** | `Array (List)` | 등록된 전체 퀴즈 객체 목록 |
| `quizzes[].question` | `String` | 퀴즈의 질문/문제 내용 |
| `quizzes[].choices` | `Array (List)` | 4지선다 보기 항목 목록 (문자열 4개) |
| `quizzes[].answer` | `Integer` | 정답 선택지 번호 (`1` ~ `4`) |
| `quizzes[].hint` | `String` | 힌트 내용 (미입력 시 빈 문자열 `""`) |
| **`best_score`** | `Integer` | 역대 게임 플레이 중 달성한 최고 점수 (맞힌 개수) |
| **`history`** | `Array (List)` | 과거 게임 플레이 결과 기록 목록 |
| `history[].score` | `Integer` | 해당 판에서 맞힌 문제 수 |
| `history[].total` | `Integer` | 해당 판의 전체 출제 문제 수 |


## 6. 트러블 슈팅

### remote에 이미 새로 커밋된 내용이 있어 로컬에서 푸쉬가 불가능한 오류

```bash
***************@****** __Codyssey__E1-2 % git push origin main
To https://github.com/fwb056/__Codyssey__E1-2.git
 ! [rejected]        main -> main (fetch first)
error: 레퍼런스를 'https://github.com/fwb056/__Codyssey__E1-2.git'에 푸시하는데 실패했습니다
hint: Updates were rejected because the remote contains work that you do not
hint: have locally. This is usually caused by another repository pushing to
hint: the same ref. If you want to integrate the remote changes, use
hint: 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

 * __remote에서 갱신된 커밋을 내려받아서 병합한 후, 다시 remote로 푸쉬한다__

```bash
***************@****** __Codyssey__E1-2 % git pull origin main
remote: Enumerating objects: 5, done.
remote: Counting objects: 100% (5/5), done.
remote: Compressing objects: 100% (3/3), done.
remote: Total 3 (delta 2), reused 0 (delta 0), pack-reused 0 (from 0)
오브젝트 묶음 푸는 중: 100% (3/3), 1.34 KiB | 684.00 KiB/s, 완료.
https://github.com/fwb056/__Codyssey__E1-2 URL에서
 * branch            main       -> FETCH_HEAD
   7daf2dc..b4fc027  main       -> origin/main
hint: You have divergent branches and need to specify how to reconcile them.
hint: You can do so by running one of the following commands sometime before
hint: your next pull:
hint:
hint:   git config pull.rebase false  # merge
hint:   git config pull.rebase true   # rebase
hint:   git config pull.ff only       # fast-forward only
hint:
hint: You can replace "git config" with "git config --global" to set a default
hint: preference for all repositories. You can also pass --rebase, --no-rebase,
hint: or --ff-only on the command line to override the configured default per
hint: invocation.
fatal: Need to specify how to reconcile divergent branches.
```

### main 브랜치에 서로 다른 커밋 이력이 있어 브랜치가 갈라진 오류
```bash
***************@****** __Codyssey__E1-2 % git commit -m "fix: update"                    
현재 브랜치 main
현재 브랜치와 'origin/main'이(가) 갈라졌습니다,
다른 커밋이 각각 2개와 1개 있습니다.

커밋할 사항 없음, 작업 폴더 깨끗함
***************@****** __Codyssey__E1-2 % git push origin main       
To https://github.com/fwb056/__Codyssey__E1-2.git
 ! [rejected]        main -> main (non-fast-forward)
error: 레퍼런스를 'https://github.com/fwb056/__Codyssey__E1-2.git'에 푸시하는데 실패했습니다
hint: Updates were rejected because the tip of your current branch is behind
hint: its remote counterpart. If you want to integrate the remote changes,
hint: use 'git pull' before pushing again.
hint: See the 'Note about fast-forwards' in 'git push --help' for details.
```

 * __rebase를 통해 커밋을 병합하고 나서 다시 push__

```bash
***************@****** __Codyssey__E1-2 % git rebase origin/main
Successfully rebased and updated refs/heads/main.
***************@****** __Codyssey__E1-2 % git push origin main
오브젝트 나열하는 중: 13, 완료.
오브젝트 개수 세는 중: 100% (13/13), 완료.
Delta compression using up to 6 threads
오브젝트 압축하는 중: 100% (9/9), 완료.
오브젝트 쓰는 중: 100% (9/9), 2.72 KiB | 2.72 MiB/s, 완료.
Total 9 (delta 5), reused 0 (delta 0), pack-reused 0 (from 0)
remote: Resolving deltas: 100% (5/5), completed with 3 local objects.
To https://github.com/fwb056/__Codyssey__E1-2.git
   b4fc027..1ec5472  main -> main
```


 * 커밋 이력 출력하기
```bash
* 7daf2dc (HEAD -> main, origin/main, origin/HEAD, fwb056-patch-1) Update README.md
*   3afada9 Merge pull request #1 from fwb056/fwb056-patch-1
|\  
| * 921d6c4 (origin/fwb056-patch-1) 최종최종
| * a912d3a 퀴즈 점수 확인 작성
| * 52d1277 퀴즈 목록 확인 작성
| * 990ddfd 퀴즈 추가 작성
| * b320b35 퀴즈 json 불러오기 작성
| * 5ca3cec 입력 예외처리, 기본 퀴즈 목록 작성
| * f2eab78 데이터 입력부 작성
| * 9704862 퀴즈결과기록 작성
| * d39d413 퀴즈풀기 작성
| * acf6e6f 게임 로비화면 작성
| * 2ee75a6 json 파일에서 불러오기용 메서드 작성
| * f358a8f json 파일 문제 입력용 메서드 작성
| * 74ad3f3 문제, 선지, 답안 체크 작성
| * 23e2ceb 기본구조 작성
| * eb8854f Update README.md
|/  
* c52de26 Initial commit
  
      Initial commit
```
