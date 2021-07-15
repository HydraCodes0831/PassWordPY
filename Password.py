user = input("Please enter a password: ")
retries = 3
while user:
    user_input = input("Please enter your password: ")
    if user_input == user:
        print("Password Accepted: ")
        break
    else:
        if user_input != user:
            retries -= 1
        if retries == 0:
            print("To many failed attempts, try again later.")
            break
        print("Password Incorrect Please Try Again, You Have", retries, "remaining")
