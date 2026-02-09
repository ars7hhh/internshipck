f1=input("type a file name:")

try:
    with open(f1,"r")as f:
         print(f.read())

except FileNotFoundError :
    print("Errors:oops! that file doesnt exist")

    

