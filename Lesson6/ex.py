# check password 3 time if wrong terminate

import sys


password = "12345"
max_try = 3
count = 0
while count <max_try:
    user_input=input("Input password :")
    if user_input == password:
        print("Login Successfully ")
        break
    else:
        count+=1 # step 
        print(f"wrong password ")
if count==max_try:
    print("system exit")
    sys.exit()
    
