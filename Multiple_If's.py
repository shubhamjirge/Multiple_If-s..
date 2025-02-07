# MULTIPLE IF's

print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0
if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("what is your age? "))
    if age <= 12:
        bill = 5
        print("child ticket $5 ")
    elif age <= 18:
        bill = 7
        print("youth ticket $7 ")
    else:
        bill = 12
        print("adult ticket $12 ")
    want_to_photo = input("do you want to a photo take? Type y for yes and n for no!")
    if want_to_photo == "y":
        # add $3 to their bill
        bill += 3
    print(f"your final bill is {bill}.")
else:
    print("Sorry you have to grow taller before you can ride.")