
def gua(fn):
      def inner(*args, **kwargs):
            print("开启外挂")
            ret = fn(*args, **kwargs)
            print("关闭外挂")
            return ret
      return inner
@ gua
def dnf():
      print("打卢克")
@ gua
def dnf():
      print("打卢克")


dnf()

