class animal:
    def sound(self):
        print("animal sound")
class dog:
    def sound(self):
        print("dog barks")
class cat:
    def sound(self):
        print("cat meow")
class rat:
    def sound(self):
        print("rat kizz")
obj=[dog(),cat(),rat()]
for a in obj:
    a.sound()




#2


class Calc:
    def add(self, *params):
        total = 0
        for x in params:
            total += x
        return total


c = Calc()
print(c.add(2, 3))
print(c.add(2, 3, 4))
print(c.add(1, 2, 3, 4, 5))