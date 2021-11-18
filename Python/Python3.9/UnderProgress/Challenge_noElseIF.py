x=float(input("enter the amount of time spent in hr: "))
try:
    print(y)
except x<=1:
    print("10 baht")
except x<=3:
    y=x*20
    print(y)
except x>3:
    y=x*40
    print(y)