
#write a program to find sum of all even numbers upto 50
"""sum=0
for i in range(0,51):
    if i%2==0:
        sum=sum+i
print("sum of even numbers are:",sum)"""

#write a program to write first 20 number and their squared number
"""print("first 20 numbers and their squares are:")
for i in range(1,21):
    print(i," ",i*i)"""

#write a program for sum of first 10 odd numbers
"""sum=0
for i in range(0,11):
    if i%2 != 0:
        print(i)
        sum=sum+i
print("sum of odd number:",sum)"""

#write a program to check if a number is divisible by 8 and 12 upto 108 using while loop
num=int(input("write a number to check:"))
while num<=108:
    if num%8==0 and num%12==0:
        print("yes")
    else:
        print("not divisible")
    num+=1

