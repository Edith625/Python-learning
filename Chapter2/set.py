# s = {"a", "a", "c"}
# print(s)

#去重复
# lst = ["a", "b", "a", "d"]
# s = set(lst)
# print(s)

#交并差
# zhangsan = {"长白山", "三亚", "纳木错", "克拉玛依"}
# lisi = {"长白山", "纳木错", "敦煌", "成都"}
# 交集
# print(zhangsan & lisi)

# 并集
# print(zhangsan | lisi)

# 差集
# print(zhangsan - lisi)

# 新增数据
s = set() #创建set集合 {}默认字典
s.add("克拉玛依")
s.add("新疆北部环线")
s.add("克拉玛依")
# print(s)

# 删减/修改
s.remove("克拉玛依")
s.add("楼兰古城")
print(s)

#查询
for item in s:
    print(item)