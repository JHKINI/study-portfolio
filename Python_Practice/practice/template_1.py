class Manager:
    def __init__(self):
        self.data = {}

    # 1️⃣ 추가
    def add_item(self):
        key = input("이름: ")
        value = input("값: ")
        self.data[key] = value
        print("저장 완료")

    # 2️⃣ 조회
    def search_item(self):
        key = input("검색: ")
        print(self.data.get(key, "없음"))

    # 3️⃣ 삭제
    def delete_item(self):
        key = input("삭제: ")
        if key in self.data:
            del self.data[key]
            print("삭제 완료")
        else:
            print("없음")

    # 4️⃣ 전체 출력
    def show_all(self):
        if not self.data:
            print("데이터 없음")
        else:
            for k, v in self.data.items():
                print(k, ":", v)

    # 5️⃣ 수정
    def update_item(self):
        key = input("수정할 이름: ")
        if key in self.data:
            self.data[key] = input("새 값: ")
            print("수정 완료")
        else:
            print("없음")

    # 6️⃣ 메뉴
    def menu(self):
        print("\n--- 메뉴 ---")
        print("1. 추가")
        print("2. 조회")
        print("3. 삭제")
        print("4. 전체보기")
        print("5. 수정")
        print("0. 종료")
        return input("선택: ")

    # 7️⃣ 실행
    def run(self):
        while True:
            choice = self.menu()

            if choice == "1":
                self.add_item()
            elif choice == "2":
                self.search_item()
            elif choice == "3":
                self.delete_item()
            elif choice == "4":
                self.show_all()
            elif choice == "5":
                self.update_item()
            elif choice == "0":
                print("종료")
                break
            else:
                print("잘못 입력")


# 실행
app = Manager()
app.run()