##1
#
class NumberIterator:
    def _init_(self, n):
        self.n = n
        self.current = 1

    def _iter_(self):
        return self

    def _next_(self):
        if self.current <= self.n:
            value = self.current
            self.current += 1
            return value
        else:
            raise StopIteration
##2
###fibbinocci
def fabonacci_genrator(n):
    a,b=0,1
    count=0
    while count < n:
        yield a
        a,b=b,a+b
        count+=1
# ###3
#
print("using Iterator:")
for num in numberiterator(5):
    print(num)

print("\nUsing Iterator:")
for num in fibonacci_genrator():
    print(num)

#4

def read_numbers_from_file(filename):
    try:
        file = open("files.txt", "r")
        content = file.read()
        file.close()

        print("File Content:")
        print(content)

    except FileNotFoundError:
        print("Error: File not found")

    except PermissionError:
        print("Error: Permission denied")
#
    except Exception as e:
        print("Unexpected error:", e)


# Program execution
filename = "files.txt"

#write_numbers_to_file(filename)
a=read_numbers_from_file(filename)


#5

def write_numbers_to_file(filename):
    try:
        file = open("files.txt","w")

        for i in range(1, 101):
            file.write(str(i) + "\n")

        file.close()
        print("Numbers written successfully")

    except FileNotFoundError:
        print("Error: File not found")

    except PermissionError:
        print("Error: Permission denied")

    except Exception as e:
        print("Unexpected error:", )
a=write_numbers_to_file("files.txt")
