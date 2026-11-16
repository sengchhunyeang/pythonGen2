attempts = 0
max_attempts = 3

while attempts < max_attempts:
    password = input("Input password: ")
    if password == "123":
        print("Login successful!")
        break
    else:
        attempts += 1
        remaining = max_attempts - attempts
        if remaining > 0:
            print(f"Invalid password. You have {remaining} attempts left.")
        else:
            print("Invalid password. Your account has been locked.")

print("Program finished.")  # runs after the loop ends