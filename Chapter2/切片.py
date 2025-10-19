# s = "我最喜欢python了"
# print(s[1]+s[2]+s[3])
# print(s[1:4]) #顾头不顾尾 [star : ) end 取不倒
# print(s[1:]) #后面不写，切到末尾
# print(s[:3]) #前面不写，从头开始切 
# print(s[:]) #都不写为从头到尾切
# print(s[3:1]) #默认从左往右,从右往左给出第三个参数

# s = "abcdefg"
# print(s[5:1:-1]) #fedc
# print(s[1:5:2]) #bd

# 练习1
# s = 'abcdefghigklmnopqrst'
# print(s[::-2]) #从头到尾，从右向前, trpn
# print(s[1:8:3]) # be
# print(s[-1:-7:-2])
# print(s[10:3:-4])


# 练习2
# 回文：上海自来水来自上海
# 让用户随便输入一句话。判断是否是回文 与原文相等

content = input(">>>: ")
s = content[::-1]
if s == content:
    print("是回文")
else:
    print("不是回文")
