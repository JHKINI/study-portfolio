class 도서관리:
    def __init__(self):
        self.책목록 = {}

    def 저장하기(self, 제목, 저자):
        self.책목록[제목] = 저자

    def 검색하기(self, 제목):
        if 제목 in self.책목록:
            return self.책목록.get(제목)
        else:
            return "책이 없습니다"

    def 출력하기(self):
        return self.책목록

    def 삭제하기(self, 제목):
        if 제목 in self.책목록:
            del self.책목록[제목]
            return "삭제 완료"
        else:
            return "삭제할 책이 없습니다"


class 도서프로그램:
    def __init__(self):
        self.book = 도서관리()

    def 실행하기(self):
        while True:
            메뉴 = input("1:저장 2:검색 3:출력 4:삭제 0:종료 >> ")

            if 메뉴 == "1":
                제목 = input("책 제목: ")
                저자 = input("저자: ")
                self.book.저장하기(제목, 저자)

            elif 메뉴 == "2":
                제목 = input("검색할 책 제목: ")
                print(self.book.검색하기(제목))

            elif 메뉴 == "3":
                print(self.book.출력하기())

            elif 메뉴 == "4":
                제목 = input("삭제할 책 제목: ")
                print(self.book.삭제하기(제목))

            elif 메뉴 == "0":
                print("프로그램 종료")
                break

            else:
                print("잘못된 메뉴입니다")


app = 도서프로그램()
app.실행하기()