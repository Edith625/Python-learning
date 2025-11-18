a = 10
def func():
      global a # 当前func内部使用的a都是全局的
      a = a + 1
      print(a)
func()
print(a)

a = 10 #a变为20
def func():
      global a # 全局变量
      a = 20
      print(a) #20
print(a) #10
func()
print(a) #20 a是全局

# nolocal
def func1():
      a = 10
      def func2():
            nonlocal a #外层中的变量引入
            a += 1
            print(a)
      func2()
func1()