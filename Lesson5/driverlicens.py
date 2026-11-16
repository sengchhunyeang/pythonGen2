# check License driver
# age = 18 and has license

age = int(input("age your :"))
license = input("Do you have license card ? y/n:")
if license == "y":
    license = True
else:
    license = False
if age >= 18:
    if license == True:
        print("have license can drive")
    else:
        print("No license can drive ")
else:
    print("can not driver ")
# what when why ? practice 