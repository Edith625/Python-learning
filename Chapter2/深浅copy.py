#  赋值
# lst1 = ["a", "b", "c"]
# lst2 = lst1
# lst1.append("e")
# print(lst1)
# print(lst2)

# 浅copy第一层
# lst1 = ["克拉玛依", "冰糖苹果", "羊肉串"]
# lst2 = lst1.copy()
# lst1.append("a")
# print(lst1)
# print(lst2)
# print(id(lst1))
# print(id(lst2))

# # 浅copy第二层
# lst1 = ["大盘鸡", "和田玉", "口岸", ["葫芦娃","黑猫警长"]]
# lst2 = lst1.copy()
# lst1[3].append("舒克")
# print(lst1)
# print(lst2)
# 相当于表面copy，延伸（比如添加的东西）并没有copy

# 深copy

import copy

# 深copy
lst1 = ["大盘鸡", "和田玉", "口岸", ["葫芦娃","黑猫警长"]]
lst2 = copy. deepcopy(lst1)
lst1[3].append("舒克")
print(lst1)
print(lst2) 
print(id(lst1[3]))
print(id(lst2[3]))