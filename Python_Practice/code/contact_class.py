class Contact:
    def __init__(self,name,phone,email,company):
        self.name=name
        self.phone=phone
        self.email=email
        self.company=company
class ContactBook:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self,contact):
        self.contacts.append(contact)
    
    def search_contact(self,name):
        for contact in self.contacts:
            if contact.name == name:
                return contact
        return None
    def add_contact_from_input(self):
        name = input("이름을 입력하세요: ")
        phone = input("전화번호를 입력하세요: ")
        email = input("이메일을 입력하세요: ")
        company = input("회사를 입력하세요: ")
        contact = Contact(name, phone, email, company)
        self.add_contact(contact)
pb= ContactBook()
while True:
    pb.add_contact_from_input()
    search_name = input("검색할 이름을 입력하세요: ")
    contact = pb.search_contact(search_name)
    if contact:
        print("이름: {}, 전화번호: {}, 이메일: {}, 회사: {}".format(contact.name, contact.phone, contact.email, contact.company))
    else:
        print("연락처를 찾을 수 없습니다.")
    