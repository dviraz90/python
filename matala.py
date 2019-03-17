zero = "zero"
one = "one"
two = "two"
three = "three"
four = "four"
five = "five"
six = "six"
seven = "seven"
eight ="eight"
nine = "nine"

num = int(input("enter number:"))
if num<10 and num > 0:
    if num == 9:
        print(nine)
    elif num == 8:
        print(eight)
    elif num == 7:
        print(seven)
    elif num == 6:
        print(six)
    elif num == 5:
        print(five)
    elif num == 4:
        print(four)
    elif num == 3:
        print(three)
    elif num == 2:
        print(two)
    elif num == 1:
        print(one)
    elif num == 0:
        print(zero)
elif num <100 and num >10:
    print(num , "is 2 digits number , sum is:", (num%10) + (num//10))
elif num < 1000 and num > 99:
    print(num ,"is 3 digits number , kefel is:" ,(num%10) * ((num//10)%10) * (num //100)) 
else:
    print("the number is more then 3 digits or negative number!")

