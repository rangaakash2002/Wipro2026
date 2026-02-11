import matplotlib.pyplot as plt

plt.plot([1,2,3], [4,5,6])
plt.show()


a = [2,4,6,8,10]
b = [10,15,20,25,30]

plt.plot(a, b, marker="o", linestyle="--")
plt.xlabel("X axis")
plt.ylabel("Y axis")
plt.title("Line chart")
plt.grid(True)
plt.show()

# Bar chart
names = ["x","y","z"]
scores = [75,90,83]

plt.bar(names, scores)
plt.title("Student scores")
plt.show()

# Horizontal bar
plt.barh(names, scores)
plt.title("Student scores Horizontal")
plt.show()
#horizontal
plt.barh(names,scores)
plt.show()
#scatters(.)
plt.scatter(a,b)
plt.show()

marks=[50,60,80,70,77,86]
plt.hist(marks,bins=5)
plt.title("Marks")
plt.show()

#pie chart

labels = ["Chrome","Firefox","Edge"]
sizes = [60,80,45]

plt.pie(sizes, labels=labels, autopct='%1.1f%%')
plt.title("Browser usage")
plt.show()
