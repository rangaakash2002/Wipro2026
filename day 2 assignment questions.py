# 1
l= list(i for i in range (1,21))
print(l)

a=list(filter(lambda x: x%2==0,l))
print (a)

sqn=list(map(lambda x:x*x,a))
print (sqn)

# sum=reduce(lambda x,y:x+y,sqn)
# print(sum)
for i,val in enumerate(l):
    print(i,val)


# data=[1,2,3,4,5,6,2,4]
# result=[]
# for i in data:
#     result.append(i*i)
# print(result)

# 2
#
# data=[1,2,3,4,5,6,2,4]
# even_numbers=list(filter(lambda x:x%2==0,data))
# print(even_numbers)
#
# # 3
# data=[1,2,3,4,5,6,2,4]
# even_numbers=list(filter(lambda x: x%2==0,data))
# print(set(even_numbers))

# 1

data=[1,2,3,4,5,6,2,4]
result=[]
for i in data:
    result.append(i*i)
print(result)

#2

data=[1,2,3,4,5,6,2,4]
even_number=list(filter(lambda x: x%2==0,data))
print(even_number)

data=[1,2,3,4,5,6,2,4]
cube_dict={x:x**3 for x in data}
print(cube_dict)
