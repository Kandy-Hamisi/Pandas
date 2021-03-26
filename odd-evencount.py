
count_odd = 0
count_even = 0


for i in range(10):

    number = int(input("Enter a number: "))
    if not number % 2:
        count_even += 1
    else:
        count_odd += 1


print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)

    

