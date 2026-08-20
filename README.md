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
## 2. 실행 방법 및 기능 목록

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

 * 커밋 이력 출력하기
```bash
***************@****** __Codyssey__E1-2 % git log --graph
* commit 921d6c4938efee605e81307766fe00ff1cc5bda8 (HEAD -> fwb056-patch-1, origin/fwb056-patch-1)
| Author: fwb056 <limdh980425@gmail.com>
| Date:   Thu Aug 20 18:39:09 2026 +0900
| 
|     최종최종
| 
* commit a912d3af504414d867b239c279df6b43158e4697
| Author: fwb056 <limdh980425@gmail.com>
| Date:   Thu Aug 20 18:31:59 2026 +0900
| 
|     퀴즈 점수 확인 작성
| 
* commit 52d1277fd51767da3083854aef0233aab362c2ae
| Author: fwb056 <limdh980425@gmail.com>
| Date:   Thu Aug 20 18:31:31 2026 +0900
| 
|     퀴즈 목록 확인 작성
| 
* commit 990ddfdeadc6c2fa74eac75f700b2e6808a41f97
| Author: fwb056 <limdh980425@gmail.com>
| Date:   Thu Aug 20 18:30:56 2026 +0900
| 
|     퀴즈 추가 작성
| 
* commit b320b35d64a1f1ff4620d63dc6357613633382a0
| Author: fwb056 <limdh980425@gmail.com>
| Date:   Thu Aug 20 18:28:55 2026 +0900
| 
|     퀴즈 json 불러오기 작성
| 
* commit 5ca3cec2cb9b5107835e6b3cd7673850d696ea4b
| Author: fwb056 <limdh980425@gmail.com>
| Date:   Thu Aug 20 18:27:34 2026 +0900
| 
|     입력 예외처리, 기본 퀴즈 목록 작성
| 
* commit f2eab789e9f4124ac94c97ad69f9af609bb06245
| Author: fwb056 <limdh980425@gmail.com>
| Date:   Thu Aug 20 18:22:30 2026 +0900
| 
|     데이터 입력부 작성
| 
* commit 9704862c15827d5c73a3d2cd67f44bf8f53f4d89
| Author: fwb056 <limdh980425@gmail.com>
| Date:   Thu Aug 20 18:19:09 2026 +0900
| 
|     퀴즈결과기록 작성
| 
* commit d39d413ab3ed109db6093db6736886c85183e4c5
| Author: fwb056 <limdh980425@gmail.com>
| Date:   Thu Aug 20 18:17:36 2026 +0900
| 
|     퀴즈풀기 작성
| 
* commit acf6e6f6f97515ee45b53b1e609c001034d312c5
| Author: fwb056 <limdh980425@gmail.com>
| Date:   Thu Aug 20 18:16:10 2026 +0900
| 
|     게임 로비화면 작성
| 
* commit 2ee75a60e43dcffcb7ae7b51cd797d9078b3032c
| Author: fwb056 <limdh980425@gmail.com>
| Date:   Thu Aug 20 18:14:58 2026 +0900
| 
|     json 파일에서 불러오기용 메서드 작성
| 
* commit f358a8f998d86e935fd1680aed021d4a0521d275
| Author: fwb056 <limdh980425@gmail.com>
| Date:   Thu Aug 20 18:12:32 2026 +0900
| 
|     json 파일 문제 입력용 메서드 작성
| 
* commit 74ad3f3c26811e158b2562f22899850800565203
| Author: fwb056 <limdh980425@gmail.com>
| Date:   Thu Aug 20 18:05:20 2026 +0900
| 
|     문제, 선지, 답안 체크 작성
|
* commit 23e2ceb1afa2691ca84728f7e34ab09888c4f82e
| Author: fwb056 <limdh980425@gmail.com>
| Date:   Thu Aug 20 18:02:27 2026 +0900
| 
|     기본구조 작성
| 
* commit eb8854fc52febcdb5426bbc84b641ed3d1a190b8
| Author: fwb056 <37894045+fwb056@users.noreply.github.com>
| Date:   Thu Aug 20 15:29:58 2026 +0900
| 
|     Update README.md
|     
|     README 작성하기
| 
* commit c52de2695c4a05fd624160b96c71712b73e1463e (origin/main, origin/HEAD, main)
  Author: fwb056 <37894045+fwb056@users.noreply.github.com>
  Date:   Thu Aug 20 15:24:15 2026 +0900
  
      Initial commit
```
