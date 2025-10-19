principle=0
rate=0
time=0

while True:
    principle=float(input("enter your amount:"))
    if principle<0:
        print("principle cannot be 0 or less than zero")
    else:
        break
while True:
    rate=float(input("enter your rate of interest:"))
    if rate<0:
        print("rate cannot be 0 or less than zero")
    else:
        break
while True:
    time=int(input("enter your time in years:"))
    if time<0:
        print("time cannot be 0 or less than zero")
    else:
        break
total=principle*pow((1+rate/100),time)
print(f"Compound interest of {time} years is:{total:.2f}")
