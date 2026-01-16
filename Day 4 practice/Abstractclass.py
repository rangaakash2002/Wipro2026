from abc import ABC, abstractmethod

class Shape(ABC):

    def display(self):
        print("display method is implemented")

    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):

    def area(self):
        print("area method is implemented")


# Creating object
r = Rectangle()
r.display()
r.area()
