import json

class 전화번호부:
    def __init__(self):
        self.번호부 = {}
        self.즐겨찾기 = []
        self.차단 = []

    def 저장하기(self, 이름, 전화번호,이메일,회사명,메모):
        if 이름 in self.번호부:
            return "이미 존재하는 이름입니다"
        self.번호부[이름] = {
            "전화번호": 전화번호,
            "이메일": 이메일,
            "회사명": 회사명,
            "메모": 메모
        }
        return "저장 완료"
    def 검색하기(self, 이름):
        if 이름 in self.차단:
            return "차단된 번호입니다"
        if 이름 in self.번호부:
            return self.번호부.get(이름)
        else:
            return "번호가 없습니다"
    def 전체출력(self):
        return self.번호부
    def 즐겨찾기추가(self, 이름):
        self.즐겨찾기.append(이름)
    def 즐겨찾기삭제(self, 이름):
        if 이름 in self.즐겨찾기:
            self.즐겨찾기.remove(이름)
    def 즐겨찾기목록(self):
        return self.즐겨찾기
    def 차단추가(self, 이름):
        self.차단.append(이름)
    def 차단해제(self, 이름):
        if 이름 in self.차단:
            self.차단.remove(이름)
            return "차단 해제 완료"
        else:
            return "차단 해제 할 번호가 없습니다"
    def 차단목록(self):
        return self.차단
    def 삭제하기(self, 이름):
        if 이름 in self.번호부:
            del self.번호부[이름]
            return "삭제 되었습니다"
        else:
            return "삭제할 번호가 없습니다"
    def 파일저장(self):
        with open("phonebook.json", "w", encoding="utf-8") as f:
            data = {
                "번호부": self.번호부,
                "즐겨찾기": self.즐겨찾기,
                "차단": self.차단
            }
            json.dump(data, f, ensure_ascii=False)
        return "파일 저장 완료"

    def 파일불러오기(self):
        try:
            with open("phonebook.json", "r", encoding="utf-8") as f:
                data = json.load(f)
                self.번호부 = data.get("번호부", {})
                self.즐겨찾기 = data.get("즐겨찾기", [])
                self.차단 = data.get("차단", [])
            return "파일 불러오기 완료"
        except FileNotFoundError:
            return "저장된 파일이 없습니다"
    

class 전화번호부프로그램:
    def __init__(self):
        self.book = 전화번호부()
    def 실행하기(self):
        while True:
            메뉴 = input(
                "1:저장 2:검색 3:전체출력 4:즐겨찾기추가 5:즐겨찾기삭제 "
                "6:즐겨찾기목록 7:차단추가 8:차단해제 9:차단목록 10:삭제 11:파일저장 12:불러오기 0:종료 >> "
            )
            if 메뉴 == "1":
                이름 = input("이름을 입력하세요: ")
                전화번호 = input("전화번호를 입력하세요: ")
                이메일 = input("이메일을 입력하세요: ")
                회사명 = input("회사명을 입력하세요: ")
                메모 = input("메모를 입력하세요: ")
                self.book.저장하기(이름, 전화번호, 이메일, 회사명, 메모)
            elif 메뉴 == "2":
                이름 = input("검색할 이름을 입력하세요: ")
                print(self.book.검색하기(이름))
            elif 메뉴 == "3":
                print(self.book.전체출력())
            elif 메뉴 == "4":
                이름 = input("즐겨찾기에 추가할 이름: ")
                self.book.즐겨찾기추가(이름)
            elif 메뉴 == "5":
                이름 = input("즐겨찾기에서 삭제할 이름: ")
                self.book.즐겨찾기삭제(이름)
            elif 메뉴 == "6":
                print(self.book.즐겨찾기목록())
            elif 메뉴 == "7":
                이름 = input("차단할 이름: ")
                self.book.차단추가(이름)
            elif 메뉴 == "8":
                이름 = input("차단 해제할 이름: ")
                print(self.book.차단해제(이름))
            elif 메뉴 == "9":
                print(self.book.차단목록())
            elif 메뉴 == "10":
                이름 = input("삭제할 이름: ")
                print(self.book.삭제하기(이름))
            elif 메뉴 == "11":
                print(self.book.파일저장())
            elif 메뉴 == "12":
                print(self.book.파일불러오기())    
            elif 메뉴 == "0":
                print("프로그램을 종료합니다.")
                break
            else:
                print("잘못된 메뉴입니다.")

phone= 전화번호부프로그램()
phone.실행하기()
