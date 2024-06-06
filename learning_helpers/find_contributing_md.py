import os

def find_contributing_md(startpath):
    for root, _, files in os.walk(startpath):
        for file in files:
            if file.lower() == 'contributing.md':
                print(f'Found CONTRIBUTING.md in {root}/{file}')

# 指定 openai 包的根目录
openai_path = 'D:/Project/newAgain/.venv/Lib/site-packages/openai'

# 查找 CONTRIBUTING.md 文件
find_contributing_md(openai_path)
