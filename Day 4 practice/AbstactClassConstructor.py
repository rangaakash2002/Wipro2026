from abc import ABC, abstractmethod
class employee(ABC):
    def __init__(self,name):
        self.name=name
        @abstractmethod
        def salary(self):
            pass
class Manager(employee):
    def salary(self):
        print(self.name,"salary is 50000")
m=Manager("Akash")
m.salary()

