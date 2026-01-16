# class student:
#     def display(self):
#         print("this is student class")
# s1=student()
# s1.display()
class calculator:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def add(self):
        print(self.a+self.b)

a=int(input())
b=int(input())
c=calculator(a,b)
c.add()
