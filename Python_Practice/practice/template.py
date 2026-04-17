#관리 프로그램형
class 관리프로그램:
    def __init__(self):
        self.data = {}

    def 추가(self):
        pass

    def 조회(self):
        pass

    def 수정(self):
        pass

    def 삭제(self):
        pass

    def 목록(self):
        pass

    def 실행(self):
        while True:
            menu = input("1.추가 2.조회 3.수정 4.삭제 5.목록 0.종료 >> ")
            if menu == "1":
                self.추가()
            elif menu == "2":
                self.조회()
            elif menu == "3":
                self.수정()
            elif menu == "4":
                self.삭제()
            elif menu == "5":
                self.목록()
            elif menu == "0":
                break

#게임형
import random

class 게임:
    def __init__(self):
        self.user_score = 0
        self.com_score = 0

    def 한판하기(self):
        pass

    def 실행(self):
        while True:
            menu = input("1.게임시작 2.점수보기 0.종료 >> ")
            if menu == "1":
                self.한판하기()
            elif menu == "2":
                print(self.user_score, self.com_score)
            elif menu == "0":
                break
#파일 저장형
import json

class 저장프로그램:
    def __init__(self):
        self.data = {}
        self.파일불러오기()

    def 파일저장(self):
        with open("data.json", "w", encoding="utf-8") as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)

    def 파일불러오기(self):
        try:
            with open("data.json", "r", encoding="utf-8") as f:
                self.data = json.load(f)
        except FileNotFoundError:
            self.data = {}