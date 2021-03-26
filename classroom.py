total_students = 0

for i in range(7):
    students = int(input("Enter the number of student in that classroom: "))

    total_students = total_students + students

    
print("the total is " + str(total_students))
avrg = total_students / 7
print("The average is " + str(avrg))