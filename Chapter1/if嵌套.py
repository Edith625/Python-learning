username = input("please enter your user name")
password = input("please enter your password")
if username == 'edith': #假设正确的用户名是edith
    if password == '123456':#进一步判断密码是否正确
        print("loading success")
    else:
        print("sorry your password is incorrect")#密码不正确
else:
    print("sorry your username is incorrect")#用户名不正确