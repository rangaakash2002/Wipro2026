class employee:
    name="sai"
    age=33
    salary=40000
e1=employee()
print(e1.name,e1.age,e1.salary)

# class students:
#     name="sai"
#     age=22
#     study="ten"
#    s1=students()
# print(s1.name,s1.age,s1.standard)

class workers:
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
w1=workers("jai",44,22000)
w2=workers("ads",43,23000)
print(w1.name,w1.age,w1.salary)


class jobs:
    def __init__ (self,name,age,place):
     self.name=name
     self.age=age
     self.place=place
j1=jobs("op",55,"mcl")
j2=jobs("hgh",44,"gnt")
print(j1.name,j1.age,j1.place)
print(j2.name,j2.age,j2.place)



