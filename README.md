# __Codyssey__E1-2
# [E 1-2] 컴퓨터에게 명령 내리는 말(파이썬) 처음 배우기

## 프로젝트 개요

Python과 Git을 이용하여, 내가 만든 프로그램이 왜 이렇게 동작하는지를 설명하고 그 과정을 기록하자.

  * 터미널에서 동작하는 나만의 퀴즈 게임을 처음부터 끝까지 구현

  * Python 기본 문법을 사용해 입력/출력 흐름을 만들고, 클래스(객체 지향)로 코드를 역할별로 구조화

  * JSON 파일 저장을 통해 프로그램을 종료해도 퀴즈와 점수가 유지되도록 "데이터 영속성"을 경험

  * Git으로 변경 이력을 관리

  * 기능 단위로 커밋, 브랜치를 나눠 작업 후 병합하며, GitHub에 저장소를 공개

---

### 1. 터미널 조작 로그 기록
 * 현재 위치 확인, 목록 확인(숨김 파일 포함), 이동, 파일 및 디렉토리 생성, 복사, 이동/이름변경, 삭제, 파일 내용 확인
```bash
***************@****** ~ % pwd                              ## 현재 위치 확인
/Users/***************

***************@****** ~ % ls -a                            ## 목록 확인(숨김 파일 포함)
.			.CFUserTextEncoding	.vscode			Desktop			Downloads		Movies			Public
..			.Trash			.zsh_sessions		Documents		Library			Music			Pictures

***************@****** ~ % mkdir mydir                      ## 디렉토리 생성
***************@****** ~ % ls                               # 목록 확인
Desktop		Documents	Downloads	Library		Movies		Music		mydir		Pictures	Public

***************@****** ~ % cd mydir                          ## 현재 위치 이동
***************@****** mydir % touch index.html              ## 파일 생성
***************@****** mydir % cp index.html index2.html     ## 복사
***************@****** mydir % ls                            # 목록 확인
index.html	index2.html
***************@****** mydir % mv index2.html indexNew.html  ## 파일 이름변경
***************@****** mydir % ls                            # 목록 확인
index.html	indexNew.html
***************@****** mydir % mv indexNew.html ~            ## 파일 이동
***************@****** mydir % ls                            # 목록 확인
index.html
***************@****** mydir % cd                            # 현재 위치 이동
***************@****** ~ % ls                                # 목록 확인
Desktop		Documents	Downloads	indexNew.html	Library		Movies		Music		mydir		Pictures	Public

***************@****** ~ % rm indexNew.html                  ## 파일 삭제
***************@****** ~ % ls                                # 목록 확인
Desktop		Documents	Downloads	Library		Movies		Music		mydir		Pictures	Public

# index.html의 내용을 vscode를 통해 "Hello, Docker!"로 수정
***************@****** ~ % cd mydir                          # 현재 위치 이동
***************@****** mydir % cat index.html                ## 파일 내용 확인
"Hello, Docker!"%
```
