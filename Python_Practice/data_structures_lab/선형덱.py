# 1. 선형 덱
class LinearDeque:
    def __init__(self, size):
        self.size = size
        self.deque = []

    def is_empty(self):
        return len(self.deque) == 0

    def is_full(self):
        return len(self.deque) == self.size

    def add_front(self, item):
        if self.is_full():
            print("덱이 가득 참")
        else:
            self.deque.insert(0, item)

    def add_rear(self, item):
        if self.is_full():
            print("덱이 가득 참")
        else:
            self.deque.append(item)

    def delete_front(self):
        if self.is_empty():
            print("덱이 비어 있음")
        else:
            return self.deque.pop(0)

    def delete_rear(self):
        if self.is_empty():
            print("덱이 비어 있음")
        else:
            return self.deque.pop()

    def peek_front(self):
        return self.deque[0]

    def peek_rear(self):
        return self.deque[-1]

    def show(self):
        print(self.deque)


dq = LinearDeque(5)

dq.add_rear(10)
dq.add_rear(20)
dq.add_front(5)
dq.show()          # [5, 10, 20]

print(dq.delete_front())  # 5
print(dq.delete_rear())   # 20
dq.show()          # [10]