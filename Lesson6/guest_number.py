from itertools import count

# guest number 7 if user input correct yes ok
number_guest = 7

for inputCount in count(1):
    print("Number guest number :7")
    user_input = int(input("let guest_number:"))
    if user_input == number_guest:
        print("yes it correct!")
        break  # break stop this statement
    else:
        print("wrong guest ")
