dict={"arshad":9900,
      "zidan":8966,
      "farwez":9362,
      }
print("Personal Contact Book",dict)
dict["nazeem"]=("1111")
print("added contact",dict)
dict["arshad"]="01010"
print("updated contact:",dict)
print(dict.get("zidan"))
print(dict.get("razeen","contact not found"))
for key,values in dict.items():
    print("names:",key,"phone",values)




