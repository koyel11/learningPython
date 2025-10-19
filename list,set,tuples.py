#collection=single "variable" used to store multiple values
#list = [] ordered and changeable.Duplicate is OK
#Set = {} unordered and immutable,but Add/Remove OK. NO duplicates.Indexing cannot be used
#Tuple = () ordered and unchangeable.Duplicate OK.Faster

fruits = ["apple","orange","banana","coconut"]
# print(fruits[0])

#fruits.append("pinapple") #add element in last
fruits.remove("apple")
fruits.insert(0,"pinapple")
fruits.sort()
fruits.reverse()

for fruit in fruits:
    print(fruit)
