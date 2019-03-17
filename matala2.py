
arr1 = ["sunday","monday","tusday","wendsday", "thersday", "friday", "shaabes"]
arr2 = ["jan", "feb", "mar","april","may","jun" ,"jul", "aug", "sep","oct", "nov", "dec"]
month = int(input("enter number between 1 -12:"))
day = int(input("enter number between 1 -7:"))
if month > 12 or day > 7:
    print("not valid")
else:
    print(arr1[day -1] ,arr2[month -1])
