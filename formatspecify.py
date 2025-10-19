#Format Specifiers= {value:flags} format a value based on what flags are inserted

price1 = 456.5433243
price2 = -5322.65
price3 = 56.96685


print(f"Value of Price1:${price1:.2f}")
print(f"Value of Price2:${price2:.2f}")
print(f"Value of Price3:${price3:.2f}")
#.2f will write first 2 decimal points in a floating number


print(f"Value of Price1:${price1:10}")
#this will make sure whole data is 10 characters (right justified by default)

print(f"Value of Price2:${price2:010}")
#this will omit the spaces with 0s

print(f"Value of Price3:${price3:<10}")
#left justified

print(f"Value of Price3:${price3:^10}")
#center justfied