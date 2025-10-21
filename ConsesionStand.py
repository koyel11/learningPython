menu={"Pizza":240,
      "Popcorn":400,
      "Fries":100,
      "Chips":80,
      "Coke":50,
      "Soda":90,
      "Lemonade":85}


cart=[]
total=0

print("--------MENU--------")
for keys,value in menu.items():
    print(f"{keys:10}:rs.{value}")

print("--------------------")

while True:
    food=input("Enter Your Order:")
    if food=="q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

for food in cart:
    total+=menu.get(food)
    print(f"{food:10}:rs.{value}")

print(f"Your Total Bill:{total}")