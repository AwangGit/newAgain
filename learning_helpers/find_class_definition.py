import os


def find_class_definition_in_openai(class_name):
    # 指定 openai 包的根目录
    openai_path = 'D:/Project/newAgain/.venv/Lib/site-packages/openai'

    for root, _, files in os.walk(openai_path):
        for file in files:
            if file.endswith('.py'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r', encoding='utf-8') as f:
                    for line in f:
                        if f'class {class_name}' in line:
                            print(f'Found {class_name} in {file_path}: {line.strip()}')


# 查找 OpenAI 类定义
find_class_definition_in_openai('OpenAI')
