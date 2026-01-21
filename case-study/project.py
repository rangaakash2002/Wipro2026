from abc import ABC, abstractmethod
import csv
import json
#abstract class

class Person(ABC):
    def __init__(self, pid, name, department):
        self.id = pid
        self.name = name
        self.department = department

    @abstractmethod
    def get_details(self):
        pass


#descriptor for marks
class MarksDescriptor:
    def __set__(self, instance, value):
        if any(m < 0 or m > 100 for m in value):
            raise ValueError("Marks should be between 0 and 100")
        instance.__dict__['marks'] = value

    def __get__(self, instance, owner):
        return instance.__dict__.get('marks', [])


#student class
class Student(Person):
    marks = MarksDescriptor()

    def __init__(self, sid, name, department, semester, marks):
        super().__init__(sid, name, department)
        self.semester = semester
        self.marks = marks

    def get_details(self):
        return f"Name: {self.name}\nRole: Student\nDepartment: {self.department}"

    def calculate_performance(self):
        avg = sum(self.marks) / len(self.marks)
        grade = "A" if avg >= 80 else "B" if avg >= 60 else "C"
        return avg, grade

    # Operator overloading >
    def __gt__(self, other):
        return self.calculate_performance()[0] > other.calculate_performance()[0]


#descriptor for salary
class SalaryDescriptor:
    def __get__(self, obj, objtype=None):
        return obj._salary

    def __set__(self, obj, value):
        if value < 0:
            raise ValueError("Salary should be positive")
        obj._salary = value


#faculty class
class Faculty(Person):
    salary = SalaryDescriptor()

    def __init__(self, fid, name, department, salary):
        super().__init__(fid, name, department)
        self.salary = salary

    def get_details(self):
        return f"Name: {self.name}\nRole: Faculty\nDepartment: {self.department}"


#course class
class Course:
    def __init__(self, code, name, credits, faculty):
        self.code = code
        self.name = name
        self.credits = credits
        self.faculty = faculty

    def __add__(self, other):
        return self.credits + other.credits


#generator
def student_generator(students):
    print("Fetching Student Records...")
    for s in students:
        yield f"{s.id} - {s.name}"


#file handling(csv)
def save_students_csv(students):
    with open("students_report.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["ID", "Name", "Department", "Average", "Grade"])

        for s in students:
            avg, grade = s.calculate_performance()
            writer.writerow([s.id, s.name, s.department, avg, grade])
#file handling(json)
    print("CSV report saved successfully")
def save_students_json(students):
    data = [{
        "id": s.id,
        "name": s.name,
        "department": s.department,
        "semester": s.semester,
        "marks": s.marks
    } for s in students]

    with open("students.json", "w") as f:
        json.dump(data, f, indent=4)

    print("Student data saved to students.json")


#sample objects create
s1 = Student("S101", "Ananya Sharma", "Computer Science", 4, [78, 85, 90, 88, 92])
s2 = Student("S102", "Rohan Verma", "Computer Science", 4, [70, 72, 75, 78, 74])

f1 = Faculty("F201", "Dr. Rajesh Kumar", "Computer Science", 85000)

c1 = Course("CS401", "Data Structures", 4, f1)
c2 = Course("CS402", "Algorithms", 3, f1)

#polymorphism
print("Student Details\n----------------------------")
print(s1.get_details())

print("\nFaculty Details\n----------------------------")
print(f1.get_details())

#operator overloading
print("\nComparing Students Performance")
print("Ananya > Rohan :", s1 > s2)

print("\nTotal Course Credits :", c1 + c2)

#genrator
print("\nStudent Record Generator\n----------------------------")
for record in student_generator([s1, s2]):
    print(record)

#output
save_students_json([s1, s2])
save_students_csv([s1, s2])
