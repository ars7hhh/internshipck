import csv
with open("students.csv","r") as f:
    file=csv.reader(f)
    for row in file:
        if row[2]=="PASS":
            print("\n students who  passed\n",row[0])



