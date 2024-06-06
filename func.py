import inspect
from openai import OpenAI

# 获取 OpenAI 类的所有成员
members = inspect.getmembers(OpenAI)

# 过滤并显示实例方法、类方法和静态方法
for name, member in members:
    if inspect.isfunction(member):
        print(f"Function: {name}")  # 打印函数名
    elif inspect.ismethod(member):
        print(f"Method: {name}")  # 打印方法名
    elif isinstance(member, staticmethod):
        print(f"Static Method: {name}")  # 打印静态方法名
    elif isinstance(member, classmethod):
        print(f"Class Method: {name}")  # 打印类方法名
