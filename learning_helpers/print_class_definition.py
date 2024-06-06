import os

def print_class_definition(file_path, class_name):
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        inside_class = False
        for line in lines:
            if f'class {class_name}' in line:
                inside_class = True
            if inside_class:
                print(line, end='')
                if line.strip().startswith('class ') and not line.strip().endswith(':'):
                    inside_class = False
                if line.strip() == '' and not inside_class:
                    break

# 打印 _client.py 文件中 OpenAI 类的定义
print_class_definition('D:/Project/newAgain/.venv/Lib/site-packages/openai/_client.py', 'OpenAI')
