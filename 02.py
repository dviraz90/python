age = int(input("Enter your age: "))
if age < 0:
    print("invalid age...")

elif age < 18:
    print("you are to young")
    print("your can by soft drinks")
else:
    print("you are to old")
    print("your can by wine")