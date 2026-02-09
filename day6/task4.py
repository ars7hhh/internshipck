'''
name1=input("enter your friend1:")
name2=input("enter your friend2:")
name3=input("enter your friend3:")
marks1=input("enter marks1:")
marks2=input("enter marks2:")
marks3=input("enter marks3:")
with open("names.txt","w") as f:
    f.write(f"{name1}-{marks1}\n{name2}-{marks2}\n{name3}-{marks3}\n")
'''
#or


for i in range(3):
    name=input(f"enter the student name{i+1}")
    marks=input(f"enter the marks{i+1}")
with open("names.txt","a")as f:
    f.write(f"{name}-{marks}")

'''
name1=input("enter student name:")
marks1=input("enter students marks:")
with open("names.txt","w") as f:
    f.write(f"{name1}={marks1}")
'''