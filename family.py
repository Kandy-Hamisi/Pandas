children = int(input("Enter the number of children in the Family: "))
allowance = 0

if children < 3:
    allowance = children * 500
    print("The allowance for the is " + str(allowance))
elif (children >= 3 or children <=5 ):
    allowance = children * 500
    print("The allowance for the is " + str(allowance))
elif (children > 5 ):
    allowance = children * 500
    print("The allowance for the is " + str(allowance))
else:
    print("no allowance for that number of children")
