str1= "saheed"
str2="Arshad"
Full_name= str1 +" "+str2
print(Full_name)

message="hello   world"
print(message.strip())
print(message.upper())
print(message.lower())
print(message.replace("hello","welcome"))

#slicing
msg="machine learning"
print(msg[0:7])
print(msg[:4])
print(msg[:-3])
print(msg[:-1])
print(msg[3:])
print(msg[0::3])
print(msg[::3])

#split
text="python+ is high level +language"
b = text.split()
b1=text.split("+")


for word in b:
    print(word)

print(" \"i\" \"love\" \"python\"")

A=[1,2,4,5,3,6,7]
A.append(8)
A.pop(1)
A.sort(reverse=True)
A.remove(1)
B=A.copy
A.remove(5)
print(A)
