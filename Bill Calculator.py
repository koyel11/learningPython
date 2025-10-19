print("*****welcome to tip calculator*****")

bill=int(input("What was the total bill? $"))
tip=int(input("how much tip would you like to give? (10,15,20)? "))
splits=int(input("how many people to spilt the bill?"))
print("total bill will be:",(bill+tip)/splits)