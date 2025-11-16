# def func1():
#       print("aafunc1")
#       def func2(): #func2在1里面不执行
#             print("bbfunc2")
#       print("cc")
#       func2()#在func1访问2，2在1层级里
# func1()

def func1():
      print("func1_before")
      def func2():
            print("func2_before")
            def func3():
                  print("func3")
            func3()
            print("func2_after")
      func2()
      print("func1_after")
func1()

# func1_before, func2_before, func3,func2_after,func1_after