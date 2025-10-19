# i = 1
# while i <= 88888: # 88888
    # print(i) #88887
    # i = i + 1

# 从1数到100
# while i <= 100:
    # print(i)
    # i = i + 1

# 从100数到1
#i = 100
#while i >=1:
    #print(i)
    #i = i - 1

# 累加计算
# i = 1
# s = 0
#while i <= 100:
   # s = s + i
   # i = i + 1
# print(s)

flag = True
while True:
    content = input("enter your word(Q return):")
    if content == 'Q':
        flag = False
    else: 
        print("someone say" + content)
