import mysql.connector

conn = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="Root@123",
    database="company_db",
    port=3306
)
cursor=conn.cursor()


print("\n Employees with Salary > 50,000:\n")

query1 = "SELECT * FROM employee WHERE salary > 50000"
cursor.execute(query1)

records = cursor.fetchall()

for row in records:
    print(row)

print("\n Inserting New Employee...\n")

query2 = """
INSERT INTO employee (id, name, department, salary)
VALUES (%s, %s, %s, %s)
"""

values = (109, "RANGA AKASH", "CSE", 65000)

cursor.execute(query2, values)
conn.commit()

print(" Employee Inserted Successfully")

print("\n Updating Salary...\n")

query3 = """
UPDATE employee
SET salary = salary * 1.10
WHERE name = %s
"""

cursor.execute(query3, ("RANGA AKASH",))
conn.commit()

print("Salary Updated Successfully")

cursor.close()
conn.close()

print("\n All Operations Completed Successfully")