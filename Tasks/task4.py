usernames = ["Ava", "Leo", "Raj", "Zoe", "Max", "Sam", "Eli", "Mia", "Ian", "Kim"]
passwords = ["12345", "abcde", "pass1", "qwert", "aaaaa"]
tries = 3
while tries > 0 :
    username = input("Enter username: ")
    password = input("Enter password: ")
    if username in usernames and password in passwords:
        tries = 0
        print(f"Login succesful. Welcome {username} !")
    else:
        tries = tries - 1
        print(f"Login incorrect. Tries left: {tries}")
