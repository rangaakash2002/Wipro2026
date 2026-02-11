import pandas as pd

# Create DataFrame
data = {
    "Employee": ["John", "Alice", "Bob", "Eva", "Mark"],
    "Department": ["IT", "HR", "IT", "Finance", "HR"],
    "Salary": [50000, 60000, 55000, 65000, 62000]
}

df = pd.DataFrame(data)

# 1. Filter all employees from IT department
it_employees = df[df["Department"] == "IT"]
print("IT Department Employees:")
print(it_employees)

# 2. Find average salary per department
avg_salary = df.groupby("Department")["Salary"].mean()
print("\nAverage Salary per Department:")
print(avg_salary)

# 3. Add new column 'Salary_Adjusted' (increase salary by 10%)
df["Salary_Adjusted"] = df["Salary"] * 1.10

print("\nFinal DataFrame:")
print(df)