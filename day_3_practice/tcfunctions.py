def add(a,b):
    print(a+b)
add(22,66)
def sub(c,d):
    return c-d,c
add(10,20)
print(sub(33,44))


def add(m,n):
    return m+n
print(add(4,5))
def mult(v,b):
    print(v*b)
mult(2,3)
def mult(u,i):
    return(u*i)
print(mult(4,5))
def div(e,f):
    return e/f
print(div(6,4))


def hello_1(name="akash",course="python"):
    print('%s,%s'%(name,course))
hello_1()
hello_1('sai','jawa')
def print_param(*params):
    print(params)
    print_params('jaya')
    print_params(1,2,3,4,5)
def print_params(**params):
    print(params)
    print_params(x,2,3,t,5)


