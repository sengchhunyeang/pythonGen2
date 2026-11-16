# # if is check condition for decision making it work until condition is true

# age_people = int(input("Enter your age:"))

# if age_people >= 18: # True
#     print("Can vote")
# # print("Age:",age_people)


# if elif else
# if check condition if True
# elif check condition if false but create new condition
# else if all condition above it false is work

# 18  to 25 = can be able to soldier but if longer than 25
age = int(input("Your age:"))
if age >= 26: # 17>=26 = False 
    print("lost chance to be soldier")
elif age >= 18: # 17>=18 = False
    print("can be able to soldier ")
else: 
    print("your age not enough yet to be soldier")