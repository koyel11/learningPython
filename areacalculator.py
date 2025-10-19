print("***AREA CALCULATOR***")

print("""Write 1 for Rectangle
Write 2 for square
Write 3 for Triangle
Write 4 for Circle""")

num=int(input("enter a number between 1-4:"))

if num==1:
    length=float(input("enter the length:"))
    width=float(input("enter the width"))
    area=2*(length+width)
    print("area:",area)
elif num==2:
    side=float(input("enter a side of square:"))
    area=side**2
    print("area of square is:",area)
elif num==3:
    base=float(input("enter base:"))
    height=float(input("enter height:"))
    area=0.5*base*height
    print("area of triangle is:",area)
elif num==4:
    radius=float(input("enter radius:"))
    area=3.14*radius*radius
    print("area of circle is:",area)
else:
    print("not applicable")
