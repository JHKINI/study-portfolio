class Calculator:
    attr_number = []
    def __init__(self,number):
        self.number=number
        self.res_add = None
    
    def add(self):
        res = 0
        for i in self.number:
            res += i
        self.res_add = res
        return res
    def minus(self):
        res = self.number[0]
        for i in self.number[1:]:
            res -= i
        return res
    def multiply(self):
        res = 1
        for i in self.number:
            res *= i
        return res
    def divide(self):
        res = self.number[0]
        for i in self.number[1:]:
            res /= i
        return res


in_list  = []    
print("숫자를 3개 입력하세요:")
for i in range(3):
    in_list.append(int(input()))
    
calc = Calculator(in_list)

print(calc._add())       # 덧셈
print(calc._minus())     # 뺄셈
print(calc._multiply())  # 곱셈
print(calc._divide())    # 나눗셈