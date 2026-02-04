tuples=(1,2,3,4,5,6)

print(tuples.count(3))
print(tuples.index(4))
print()

#set
set={10,20,30,40,50}
set.add(6)
print(set)

#dictionary
dict={"name":"arshad","job":"developer","age":21}
print(dict)
dict["age"]=22
dict["profession"]="coder"
print(dict)

#lambda
sum=lambda a,b:a+b
print(sum(5,10))

#map
values=[1,2,3,4,5,6]
print(list(map(lambda a:a*2,values)))

#filter
print(list(filter(lambda a:a%2==0,values)))
print(list(filter(lambda a:a%3==0,values)))
   
#reduce
from functools import reduce
print(reduce(lambda a,b:a+b,values))
