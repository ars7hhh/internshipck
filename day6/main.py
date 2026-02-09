'''file=open("sample.txt","r")
print(file.read())
file.close()


file=open("sample1.txt","w")
file.write("Saheed Arshad")

file=open("sample1.txt","a")      #append
file.write("\n Saheed Arshad")'''

'''with open("arsh.jpg","rb") as f:
    print(f.read())
    '''
'''
try:
    with open("sample5.txt","r") as f:
        print(f.read())
    

except Exception as e:
    print(f" Error:{e}")

finally:
    print("this is default")
'''
import csv
with open("Company_Data.csv","r")as f:
   file=csv.reader(f)
   for row in file:
      print(row)


