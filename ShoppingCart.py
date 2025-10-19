foods=[]
prices=[]
total=0

while True:
    food = input("Enter a food to buy (q to quit):")

    if food.lower()=="q":
        break
    else:
        price = int(input(f"Enter the Price of {food}:"))
        foods.append(food)
        prices.append(price)

print("-----YOUR CART-----")

for food in foods:
    print(f"{food}:rs.{price}")

for price in prices:
    total+=price

print(f"your total price will be:{total}")
