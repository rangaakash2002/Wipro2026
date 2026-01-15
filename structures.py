num=int(input())
if (num%2==0):
    print("even")
else:
    print("odd")


weekdays=int(input())
if(weekdays==1):
    print("monday")
elif(weekdays==2):
    print("tuesday")
elif (weekdays == 3):
    print("wednessday")
elif(weekdays==4):
    print("thursday")
elif (weekdays == 5):
    print("friday")
elif (weekdays == 6):
    print("saturday")
else:
    print("sunday")

num=int(input())
if num>0 and num<10:
    print("small")
elif num>10 and num<100:
    print("medium")
else:
    print("large")