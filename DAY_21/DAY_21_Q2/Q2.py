import matplotlib.pyplot as plt
import seaborn as sns

months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun']
sales = [25000, 27000, 30000, 28000, 32000, 31000]

# ----- Matplotlib Line Chart -----
plt.figure()
plt.plot(months, sales, marker='o')
plt.title("Monthly Sales Trend")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.grid(True)
plt.show()

# ----- Seaborn Bar Plot -----
plt.figure()
sns.barplot(x=months, y=sales)
plt.title("Monthly Sales Bar Chart")
plt.xlabel("Months")
plt.ylabel("Sales Amount")
plt.grid(True)
plt.show()