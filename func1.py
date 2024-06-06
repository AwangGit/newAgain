import inspect
from openai import OpenAI

# 创建 OpenAI 类的实例
client = OpenAI(
    base_url='https://api.openai-proxy.org/v1',
    api_key='your-api-key'
)

# 获取 OpenAI 类的所有成员
members = inspect.getmembers(client)

# 过滤并显示实例方法、类方法和静态方法
for name, member in members:
    if inspect.ismethod(member):
        print(f"Instance Method: {name}")
    elif inspect.isfunction(member):
        if isinstance(getattr(OpenAI, name, None), staticmethod):
            print(f"Static Method: {name}")
        elif isinstance(getattr(OpenAI, name, None), classmethod):
            print(f"Class Method: {name}")
        else:
            print(f"Function: {name}")
