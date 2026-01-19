class calc:
    def add(self,a,b,c=0):
        return a+b+c
c=calc()
print(c.add(4))
print(c.add(50,60))
print(c.add(10,40,50))