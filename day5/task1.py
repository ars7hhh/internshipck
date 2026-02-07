def calc_rectangle(len,wid):
    area=len*wid
    perimeter=2*(len+wid)
    return (area,perimeter)
len=float(input("enter the length of rectangle:"))
wid=float(input("enter the width of the rectangle:"))
area,perimeter=calc_rectangle(len,wid)
print("Area:X",area,"Perimeter:Y",perimeter)

