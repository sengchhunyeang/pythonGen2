correct_password = "123"
user_guess = ""
RED = "\033[0;31m"
GREEN = "\033[0;32m"
END = "\033[0m"
# The loop runs as long as the guess is wrong
while user_guess != correct_password:
    user_guess = input("Enter the password: ")
    
    if user_guess != correct_password:
        print(f"{RED}Incorrect password. Try again.\n{END}")

print(f"{GREEN}Access Granted!{END}")


# Homework 2
# 1 check password 123 
# if wrong 3 time terminate ( វាយខុស3ដងឈប់ឲ្យវាយ)
# using while loop + Condition ( if else elif )