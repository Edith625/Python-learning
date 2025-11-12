Login_pairs = [
    ["Ava", "12345"],
    ["Leo", "abcde"],
    ["Raj", "pass1"],
    ["Zoe", "qwert"],
    ["Max", "aaaaa"],
    ["Sam", "zzzzz"],
    ["Eli", "11111"],
    ["Mia", "apple"],
    ["Ian", "hello"],
    ["kim", "admin"]
]
tries = 3
#验证三次登陆
while tries > 0:
    input_username = input("Enter username: ") 
    input_password = input("Enter password: ")
    current_pair = [input_username, input_password]
    if current_pair in Login_pairs:
        print(f"Login success. Welcome: {input_username}")
    else:
        tries = tries - 1
        print(f"Login incorrect. Tries left: {tries}")
#三次尝试失败，是否机器人验证
if tries == 0:
    while True:
        robot_answer = input("Are you a robot(Y/n)?")
        if robot_answer == "Y" or robot_answer == "":
            exit()
        elif robot_answer == "n":
            print("Extra trying times")
            break
#不是机器人额外三次验证 
    tries = 3
    while tries > 0:
        input_username = input("Enter username: ") 
        input_password = input("Enter password: ")
        current_pair = [input_username, input_password]
        if current_pair in Login_pairs:
            print(f"Login success. Welcome: {input_username}")
            exit()
        else:
            tries = tries - 1
            print(f"Login incorrect. Tries left: {tries}")
        if tries == 0:
            print("Too many tries time, Account locked")     
            exit() 
