usernames = ["Ava", "Leo", "Raj", "Zoe", "Max", "Sam", "Eli", "Mia", "Ian", "Kim"] 
while True:
    input_name = input("Enter username: ")
    if input_name in usernames:
        print(f"Login successful. Welcome {input_name} !")
    else:
        print("Login incorrect.")

