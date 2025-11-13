dict1 = {
    "name": "汪峰",
    "wife": {
        "name": "章子怡",
        "age": 18,
        'hobby': ['打球', "武术", "演戏"]
    },
    "hobby": ["唱歌", "跳舞", "当导师"],
    "kids": [
        {"name": "老大", "age": 10},
        {"name": "老二", "age": 8}
        ]
}
# print(dict1)
#查找
# print(dict1['wife']['hobby'][1])
#汪峰添加
# dict1["hobby"].append("卡拉ok")
#wife添加
# dict1['wife']['hobby'].append("卡拉ok")
# print(dict1)

# 二儿子加1岁
dict1['kids'][1]['age']+=1
print(dict1)