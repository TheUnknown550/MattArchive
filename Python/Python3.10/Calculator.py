x=int(input("Enter a number: "))
y=int(input("Enter another Number: "))
z=input("what do you want to do with dez numbers: ")
if "ad" in z or z=="+":
    print(" that ans is ", x+y)
elif "sub" in z or z=="-":
    print(" that ans is ", x-y)
elif "mul" in z or z=="*":
    print(" that ans is ", x*y)
elif "de" in z or z=="/":
    print(" that ans is ", x/y)
else:
    print("error")