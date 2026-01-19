class Animal:
    def speak(self):
        print("Animal makes sound")
class dog(Animal):
    def bark(self):
        print("dog bark")
a=dog()
a.speak()
a.bark()