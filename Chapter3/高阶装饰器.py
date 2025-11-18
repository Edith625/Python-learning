def wrapper1(fn):
      def inner(*args, **kwargs):
            print("wrapper1-before")
            ret = fn(*args, **kwargs)
            print("wrapper1-after")
            return ret
      return inner

def wrapper2(fn):
      def inner(*args, **kwargs):
            print("wrapper2-before")
            ret = fn(*args, **kwargs)
            print("wrapper2-after")
            return ret
      return inner

def wrapper3(fn):
      def inner(*args, **kwargs):
            print("wrapper3-before")
            ret = fn(*args, **kwargs)
            print("wrapper3-after")
            return ret
      return inner

@wrapper3 #装饰2的结果
@wrapper2 #装饰1的结果
@wrapper1 #就近原则


def target():
      print("我是target")
target()