i = int(input("input your maths mark:"))
x = int(input("input your chemistry mark:"))
y = int(input("input your physics mark:"))
total = i + x + y
percentage = float((total/300) * 100)
if percentage >= 70:
    print("Your percentage score is:", percentage)
    print ("Your grade is an A")
elif percentage >= 60:
    print("Your percentage score is:", percentage)
    print ("Your grade is an B")
elif percentage >= 50:
    print("Your percentage score is:", percentage)
    print ("Your grade is an C")
elif percentage >= 40:
    print("Your percentage score is:", percentage)
    print ("Your grade is an D")
else:
    print("Your percentage score is:", percentage)
    print ("Your have failed")