# 2. 원형 덱
class CircularDeque:
    def __init__(self, size):
        self.size = size
        self.deque = [None] * size
        self.front = 0
        self.rear = 0

    def is_empty(self):
        return self.front == self.rear

    def is_full(self):
        return self.front == (self.rear + 1) % self.size

    def add_front(self, item):
        if self.is_full():
            print("덱이 가득 참")
        else:
            self.front = (self.front - 1) % self.size
            self.deque[self.front] = item

    def add_rear(self, item):
        if self.is_full():
            print("덱이 가득 참")
        else:
            self.deque[self.rear] = item
            self.rear = (self.rear + 1) % self.size

    def delete_front(self):
        if self.is_empty():
            print("덱이 비어 있음")
        else:
            item = self.deque[self.front]
            self.deque[self.front] = None
            self.front = (self.front + 1) % self.size
            return item

    def delete_rear(self):
        if self.is_empty():
            print("덱이 비어 있음")
        else:
            self.rear = (self.rear - 1) % self.size
            item = self.deque[self.rear]
            self.deque[self.rear] = None
            return item

    def show(self):
        print(self.deque, "front:", self.front, "rear:", self.rear)


dq = CircularDeque(6)  # 원형큐는 한 칸 비워두므로 실제 저장 가능 개수는 5개

dq.add_rear(10)
dq.add_rear(20)
dq.add_front(5)
dq.show()

print(dq.delete_front())  # 5
print(dq.delete_rear())   # 20
dq.show()