numbers=[1,2,3,4,5,6,7,8]
names=["akash","sai","jai","ramu"]
mixed=[10,True,"python",6.5]
numbers[4]=200
print(numbers)
print(names)
print(mixed)
if 80 in numbers:
    print("found")
else:
    print("not found")
matrix=[2,4,6],[2,4,8]
print(matrix[1][2])
name=["akash", "sai", "jai", "ramu"]
name.reverse()
print(name)
print(name[::-2])
name.remove("jai")
print(name)
name.insert(3,"somesh")
print(name)
name.pop()
print(name)
name.append("boys")
print(name)
name.extend("guys","follow")
print(name)