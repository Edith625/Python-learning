# d = {"jay": "周杰伦" , "jj": "林俊杰"}
#添加数据
# d['key'] = "a"#新key = 新增值
# print(d)
# d.setdefault("pp", "aa") #key不存在，存在无法运行
# print(d)

# d['jj'] = "bb" #修改
# print(d)

# 删除
# d.pop('jay')
# print(d)

#查询
# print(d['jay'])
# print(d.get('jay1')) #key不存在none 也可以随意指定默认值

#练习
# lst = {11, 22, 33, 44, 55, 66, 77, 88, 99}
# result ={'bigger': [], 'smaller':[] }
# for item in lst:
#     if item > 50:
#         if result.get('bigger') == None:
#             result['bigger'] = item #如果没有bigger，创建一个
#         else:
#             result['bigger'].append(item)#有加进去
# else:
#     if result.get('smaller') == None:
#         result['smaller'] = item
#     else:
#         result['smaller'].append(item)
# print(result)

#解法2:
# lst = [11, 22, 33, 44, 55, 66, 77, 88, 99]
# result = {'bigger':[], 'smaller':[]}
# for item in lst:
#     if item > 50:
#         result.setdefault("bigger", []).append(item)
#     else:
#         result.setdefault("smaller", []).append(item)
# print(result)