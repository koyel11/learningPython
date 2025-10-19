import time

my_time=int(input("enter time in seconds:"))

for x in range(my_time,0,-1):
    seconds=x % 60
    mins=int(x/60)%60
    print(f"{mins}:{seconds:02}")
    time.sleep(1)
print("time is up!")