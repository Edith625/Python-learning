# f = open("f.txt", mode="w", encoding="utf-8")
# f.write("hello")
# f.write("\n")
# f.write("fine")
# f.write("\n")
# f.write("nice to meet you")

# 借助os模块 
import os
with open("f.txt", mode="r", encoding="utf-8") as f1,\
      open("f_1.txt", mode="w", encoding="utf-8") as f2:
      for line in f1:
            if "h" in f1:
                  line = line.replace("h", "1")
            f2.write(line)
os.remove("f.txt")
os.rename("f_1.txt", "f.txt")


