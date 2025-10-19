# print(dir(str))
# s = "asbcsdjhkjnfck"
# a = len(s) #计算字符串长度
# print(a)
money = input("please enter your salary").strip()
if money.isdigit():#判断是否是由数字组成
    money = int(money) #转化
    if money > 3000 :
        print("buy a bag")
    else:
        print("buy shoes")
else:
    print("wrong")