# name = input ("please enter your name")
# age = input ("please enter your age")
# job = input ("please enter your job")
# hobby = input ("please enter your hobby")
# print("----------- info of "+name+"-----------" )
# print("Name : "+name)
# print("Age : "+age)
# print("Job : "+job)
# print("Hobby: "+hobby)
# print("----------- end -----------" )

# 老式格式
# name = input ("please enter your name")
# age = input ("please enter your age")
# job = input ("please enter your job")
# hobby = input ("please enter your hobby")
# s = """----------- info of %s----------- 
# Name : %s
# Age : %s
# Job : %s
# Hobby : %s
# --------- end ------------
# """ % (name, name, age, job,hobby)
# print(s)

# %d表示在字符串中占位整数
# print("my name is %s, i am from %s, i am %d" % ("edith", "china", 18))

# %f表示在字符串中占位小数
# print("my name is %s, i am from %s, my salary is%.3f" % ("edith", "china", 28.88))

# 新格式化方案 f-string
name = "jame"
addr = "Australia"
hobby = "skating"
print(f"my name is{name}, i like in {addr} doing {hobby}")