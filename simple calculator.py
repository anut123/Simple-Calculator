num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
choice = input("select operations-1/2/3/4:")
if choice == "1":
    print(num1,"+",num2,"=",num1+num2)
elif choice == "2":
    print(num1,"-",num2,"=",num1-num2)
elif choice == "3":
    print(num1,"*",num2,"=",num1*num2)
elif choice == "4":
    print(num1,"/",num2,"=",num1/num2)
else:
    print("Invalid")
