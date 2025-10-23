d = {"aa": "11", "bb":"22", "cc":"33", "dd":"44"}
# for k in d:
#     print(k)
#     print(d[k])

# for k in d.keys(): #keys方法
#     print(k)
#     print(d[k])


#拿到所有value
# for v in d.values():
#     print(v)

#解构
# a = 10, 20
# print(a)
# print(type(a))
# a, b = 10, 20
# print(a, b)

#通过解构
for item in d.items():
   k, v = item
   print(k)
   print(v)