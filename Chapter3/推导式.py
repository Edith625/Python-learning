# lst = []
# for i in range(1, 11):
#       lst.append(i)
# print(lst)


#列表推导式 [结果 for循环 if循环 ]
# lst = [i for i in range(1,11)]
# print(lst)

# #1-10奇数添加到列表
# lst = [i for i in range(1, 11) if i %2 == 1]
# print(lst)

# # 1-10奇数平方添加到列表
# lst = [i ** 2 for i in range(1, 11)if i %2 == 1]
# print(lst)

#python x 1 ~ python X 255
# lst = ["python x %s" % i for i in range(1, 256)]
# print(lst)

# 字典 {key:value for循环 if}
# lst = ["hello", "not good", "fine"]
# d = {i:lst[i] for i in range(len(lst))}
# print(d)

#集合推导式 {key for循环 if}
lst = ["aa", "aa", "cc"]
s = {item for item in lst}
print(s)

#生成器推导 g = (i for i in range())
g = (i for i in range(5))
# print(g)
# print(g.__next__())
# 拿空数据
# 1.
# for item in g:
#       print(item)
#2. 使用lst tuple set
print(set(g))