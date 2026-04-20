import json
import flet as ft


class 전화번호부:
    def __init__(self):
        self.번호부 = {}
        self.즐겨찾기 = []
        self.차단 = []

    def 저장하기(self, 이름, 전화번호, 이메일, 회사명, 메모):
        이름 = 이름.strip()
        if not 이름:
            return "이름을 입력하세요"

        if 이름 in self.번호부:
            return "이미 존재하는 이름입니다"

        self.번호부[이름] = {
            "전화번호": 전화번호.strip(),
            "이메일": 이메일.strip(),
            "회사명": 회사명.strip(),
            "메모": 메모.strip()
        }
        return "저장 완료"

    def 검색하기(self, 이름):
        이름 = 이름.strip()

        if 이름 in self.차단:
            return "차단된 번호입니다"

        if 이름 in self.번호부:
            return {이름: self.번호부[이름]}

        # 부분검색
        결과 = {}
        for key, value in self.번호부.items():
            if 이름 in key:
                결과[key] = value

        return 결과 if 결과 else "번호가 없습니다"

    def 전체출력(self):
        return self.번호부

    def 즐겨찾기추가(self, 이름):
        if 이름 not in self.번호부:
            return "번호부에 없는 이름입니다"
        if 이름 in self.즐겨찾기:
            return "이미 즐겨찾기에 있습니다"
        self.즐겨찾기.append(이름)
        return "즐겨찾기 추가 완료"

    def 즐겨찾기삭제(self, 이름):
        if 이름 in self.즐겨찾기:
            self.즐겨찾기.remove(이름)
            return "즐겨찾기 삭제 완료"
        return "즐겨찾기에 없는 이름입니다"

    def 차단추가(self, 이름):
        if 이름 not in self.번호부:
            return "번호부에 없는 이름입니다"
        if 이름 in self.차단:
            return "이미 차단된 이름입니다"
        self.차단.append(이름)
        return "차단 완료"

    def 차단해제(self, 이름):
        if 이름 in self.차단:
            self.차단.remove(이름)
            return "차단 해제 완료"
        return "차단 해제할 번호가 없습니다"

    def 삭제하기(self, 이름):
        if 이름 in self.번호부:
            del self.번호부[이름]

            if 이름 in self.즐겨찾기:
                self.즐겨찾기.remove(이름)
            if 이름 in self.차단:
                self.차단.remove(이름)

            return "삭제 완료"
        return "삭제할 번호가 없습니다"

    def 파일저장(self):
        with open("phonebook.json", "w", encoding="utf-8") as f:
            data = {
                "번호부": self.번호부,
                "즐겨찾기": self.즐겨찾기,
                "차단": self.차단
            }
            json.dump(data, f, ensure_ascii=False, indent=2)
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


def main(page: ft.Page):
    book = 전화번호부()

    page.title = "전화번호부 앱"
    page.window_width = 1000
    page.window_height = 700
    page.scroll = ft.ScrollMode.AUTO
    page.padding = 20

    이름 = ft.TextField(label="이름", width=250)
    전화번호 = ft.TextField(label="전화번호", width=250)
    이메일 = ft.TextField(label="이메일", width=250)
    회사명 = ft.TextField(label="회사명", width=250)
    메모 = ft.TextField(label="메모", width=400, multiline=True, min_lines=2, max_lines=4)
    검색어 = ft.TextField(label="검색할 이름", width=250)

    상태메시지 = ft.Text(value="", size=16)
    결과영역 = ft.Column(scroll=ft.ScrollMode.AUTO, expand=True)

    def 상태표시(msg):
        상태메시지.value = msg
        page.update()

    def 입력초기화():
        이름.value = ""
        전화번호.value = ""
        이메일.value = ""
        회사명.value = ""
        메모.value = ""

    def 카드만들기(이름값, 정보):
        즐겨찾기표시 = "⭐" if 이름값 in book.즐겨찾기 else ""
        차단표시 = "⛔" if 이름값 in book.차단 else ""

        return ft.Card(
            content=ft.Container(
                padding=15,
                content=ft.Column(
                    controls=[
                        ft.Text(f"{이름값} {즐겨찾기표시}{차단표시}", size=18, weight=ft.FontWeight.BOLD),
                        ft.Text(f"전화번호: {정보.get('전화번호', '')}"),
                        ft.Text(f"이메일: {정보.get('이메일', '')}"),
                        ft.Text(f"회사명: {정보.get('회사명', '')}"),
                        ft.Text(f"메모: {정보.get('메모', '')}"),
                    ],
                    spacing=5
                )
            )
        )

    def 결과출력(data):
        결과영역.controls.clear()

        if isinstance(data, str):
            결과영역.controls.append(ft.Text(data, size=16))
        elif isinstance(data, dict):
            if not data:
                결과영역.controls.append(ft.Text("데이터가 없습니다", size=16))
            else:
                for 이름값, 정보 in data.items():
                    결과영역.controls.append(카드만들기(이름값, 정보))
        elif isinstance(data, list):
            if not data:
                결과영역.controls.append(ft.Text("목록이 비어 있습니다", size=16))
            else:
                for item in data:
                    결과영역.controls.append(ft.Text(str(item), size=16))

        page.update()

    def 저장(e):
        msg = book.저장하기(
            이름.value,
            전화번호.value,
            이메일.value,
            회사명.value,
            메모.value
        )
        상태표시(msg)
        if msg == "저장 완료":
            입력초기화()
            결과출력(book.전체출력())

    def 검색(e):
        결과 = book.검색하기(검색어.value)
        결과출력(결과)
        상태표시("검색 완료")

    def 전체보기(e):
        결과출력(book.전체출력())
        상태표시("전체 출력 완료")

    def 삭제(e):
        msg = book.삭제하기(검색어.value.strip())
        상태표시(msg)
        결과출력(book.전체출력())

    def 즐겨찾기추가(e):
        msg = book.즐겨찾기추가(검색어.value.strip())
        상태표시(msg)
        결과출력(book.전체출력())

    def 차단추가(e):
        msg = book.차단추가(검색어.value.strip())
        상태표시(msg)
        결과출력(book.전체출력())

    def 파일저장(e):
        msg = book.파일저장()
        상태표시(msg)

    def 파일불러오기(e):
        msg = book.파일불러오기()
        상태표시(msg)
        결과출력(book.전체출력())

    page.add(
        ft.Text("고객 연락처 관리 앱 ", size=28, weight=ft.FontWeight.BOLD),

        ft.Row(
            controls=[
                ft.Column(
                    controls=[
                        이름,
                        전화번호,
                        이메일,
                        회사명,
                        메모,
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("저장", on_click=저장),
                                ft.ElevatedButton("전체보기", on_click=전체보기),
                                ft.ElevatedButton("파일저장", on_click=파일저장),
                                ft.ElevatedButton("파일불러오기", on_click=파일불러오기),
                            ],
                            wrap=True
                        ),
                    ],
                    spacing=10
                ),
                ft.VerticalDivider(),
                ft.Column(
                    controls=[
                        검색어,
                        ft.Row(
                            controls=[
                                ft.ElevatedButton("검색", on_click=검색),
                                ft.ElevatedButton("삭제", on_click=삭제),
                                ft.ElevatedButton("즐겨찾기 추가", on_click=즐겨찾기추가),
                                ft.ElevatedButton("차단 추가", on_click=차단추가),
                            ],
                            wrap=True
                        ),
                        상태메시지,
                    ],
                    spacing=10
                )
            ],
            alignment=ft.MainAxisAlignment.START,
            vertical_alignment=ft.CrossAxisAlignment.START
        ),

        ft.Divider(),
        ft.Text("결과", size=22, weight=ft.FontWeight.BOLD),
        결과영역
    )


ft.app(target=main)