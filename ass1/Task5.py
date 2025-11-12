usernames = ["Ava", "Leo", "Raj", "Zoe", "Max", "Sam", "Eli", "Mia", "Ian", "Kim"]
passwords = ["12345", "abcde", "pass1", "qwert", "aaaaa", "zzzzz", "11111","apple", "hello", "admin"]
tries = 3
while tries > 0:
    input_username = input("Enter username: ")
    input_password = input("Enter password: ")
    if input_username in usernames:
        print(f"Login successful. Welcome {input_username} !")
    else:
        tries = tries - 1
        print(f"Login incorrect. Tries left: {tries}")
