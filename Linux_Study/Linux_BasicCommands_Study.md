Linux 학습 정리 (26-05-15)
1. 파일 아카이브 및 압축
tar로 파일 묶기 (아카이브 생성)

여러 파일을 하나의 파일로 묶을 때 사용.

tar -cvf archive.tar file1.txt file2.txt

옵션 설명:

c : 새로운 아카이브 생성
v : 과정 출력
f : 파일 이름 지정

예시:

tar -cvf project.tar main.cpp README.md
tar 파일 확인
tar -tvf archive.tar
tar 파일 풀기
tar -xvf archive.tar

옵션:

x : 압축 해제
2. zip 파일 만들기
zip 압축
zip archive.zip file1.txt file2.txt

예시:

zip source.zip main.cpp Makefile
zip 압축 해제
unzip archive.zip
3. vi 편집기 기본 사용법

리눅스에서 자주 사용하는 텍스트 편집기.

파일 열기
vi filename.txt
입력 모드 진입
i
i 누르면 INSERT 모드 진입
저장 후 종료

ESC 누른 뒤:

:wq
저장하지 않고 종료
:q!
4. Makefile 기초

컴파일 과정을 자동화할 때 사용.

Makefile 예시
all:
	g++ main.cpp -o app

실행:

make

결과:

app 실행파일 생성
5. useradd 명령어

새 사용자 계정 생성 명령어.

sudo useradd username

예시:

sudo useradd testuser

비밀번호 설정:

sudo passwd testuser
useradd vs adduser 차이
useradd
저수준(low-level) 명령어
기본 리눅스 명령
옵션 직접 설정 필요
adduser
useradd를 기반으로 만든 편의 스크립트
Ubuntu 계열에서 많이 사용
홈 디렉토리 등을 자동 생성

즉,

useradd → 기본 시스템 명령
adduser → 사용 편의 기능 추가 버전

둘 다 사용하지만,
리눅스 기초/시스템 관리 공부에서는 useradd를 더 자주 배우는 편.

오늘 배운 핵심 키워드
tar
zip / unzip
vi editor
Makefile
make
useradd
passwd

리눅스 기본 명령어와 개발 환경 구성 과정을 실습하며 정리한 학습 기록입니다.