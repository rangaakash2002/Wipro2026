import csv
with open("student.csv","w",newline="") as csss:
    writer=csv.writer(csss)

    writer.writerow(["name", "id", "age"])
    writer.writerow(["akash", "55", "22"])
    writer.writerow(["sai", "33", "22"])
    writer.writerow(["jai", "22", "22"])