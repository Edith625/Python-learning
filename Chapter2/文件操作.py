# f = open("32_a_txt.txt", mode="r", encoding="utf-8")
# print(f.read())

# f.read() 只读
# f = open("a.txt", mode="r", encoding="utf-8")
# print(f.read(3))
# print(f.readline())

# for循环
# for line in f:
#       print(line.strip())

# 前面单独读取，后面用for
# first = f.readline()
# print(first)
# print("======")
# for line in f:
#       print(line)

# w:write只写 重新创建文件
# f = open("b.txt", mode="w", encoding="utf-8")
# f.write("周杰伦")
# f.write("\n") 换行
# f.write("jj")

# a:append 追加写 不会重新创建文件，如果文件不存在会重新创建
# f = open("b.txt", mode="a", encoding="utf-8")
# f.write("hello")

# b:bytes字节 8个0和1 二进制 处理非文本文件
# rb:读取,wb:写入
# f1 = open("a/tu.jpg", mode="rb")
# f2 = open("c/tu.jpg", mode="wb")
# for line in f1:
#       f2.write(line)

# with 省略close
# with open("d.txt", mode="r", encoding="utf-8") as f1, \
#       open("e.txt", mode="w", encoding="utf-8") as f2:
#       for line in f1:
#             f2.write(line)
#             print(line.strip())
    
      

