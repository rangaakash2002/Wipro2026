#1
# class vehicle:
#     def start(self):
#         print("vehicle is starting")
# v=vehicle()
# v.start()
# #2
# class car(vehicle):
#     def drive(self):
#         print("car is driveing")
# c=car()
# c.start()
# c.drive()
#3

# class vehicle:
#     def __init__(self):
#         vehicle.vehicle_count +=1
#     def start(self):
#         print("vehicle is starting")
#
#
# class car(vehicle):
#     def drive(self):
#         print("car is driveing")
# v1=vehicle()
# c1=car()
# c2=car()
# print("total vehicles created")



#4

# class Animal:
#     def speak(self):
#         print("Animal makes this sound")
# class Dog(Animal):
#     def dog(self):
#         print("dog is barking")
# class Cat(Animal):
#     def cat(self):
#         print("cat is making sounds like meow meow")
#
#
# animals=[Animal(),dog(),cat()]
#
# for a in animals:
#     a.speak()




# class vehicle:
#     def start(self):
#         print("vehicle is starting")
# v=vehicle()
# v.start()
#
# class car(vehicle):
#     def drive(self):
#         print("car is driveing")
# c=car()
# c.start()
# c.drive()

##2 question


#1
# import re
#
#
# emp_id="EMP123"
# pattern_emp=r"^EMP\d{3}"
# match_emp=re.match(pattern_emp,emp_id)
# if match_emp:
#     print("valid employee id")
# else:
#     ("invaid employee id")
#

#2


# import re
#
# text="rangaakash2002@gmail.com"
# pattern=r"[\w.+-]+@[\w-]\.[\w.-]+"
# match=re.search(pattern,text)
# if match:
#     print("mail found:",match.group())
# else:
#     print("give valid email id or not found")
#

#3


# import re
#
# text="Akash has mobile number 8897073205"
# pattern=r"(\w+)(\d+).+)(\d{10})"
# match =re.search(pattern,text)
#   if match:
#     print("Full match:",match.group())
#     print("username(\\w+):",match.group(1))
#     print("user number(\\d+):", match.group(2))
#     print("mobile number(\\d{10}):", match.group(3))

#4

# import re
#
# text = "employee id:EMP123,NAME:Akash"
# pattern = r"(EMP\d{3}),Name:(\w+)"
#
# match = re.search(pattern, text)
#
# if match:
#     print("Full match:", match.group(0))
#     print("Group 1 (Employee ID):", match.group(1))
#     print("Group 2 (Name):", match.group(2))
