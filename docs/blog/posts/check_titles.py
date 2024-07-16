import os
import yaml

def check_posts_titles(posts_dir):
    missing_titles = []
    
    # 遍历目录中的所有文件
    for root, _, files in os.walk(posts_dir):
        for file in files:
            if file.endswith('.md'):
                file_path = os.path.join(root, file)
                
                # 读取文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    content = f.read()
                    
                    # 查找文件头部
                    if content.startswith('---'):
                        try:
                            end_index = content.index('---', 3)
                            front_matter = content[3:end_index].strip()
                            front_matter_data = yaml.safe_load(front_matter)
                            
                            # 检查title字段
                            if 'title' not in front_matter_data or not front_matter_data['title']:
                                missing_titles.append(file_path)
                        except ValueError:
                            missing_titles.append(file_path)
                    else:
                        missing_titles.append(file_path)
    
    # 输出缺少title字段的文件路径
    if missing_titles:
        print("以下文件缺少title字段:")
        for path in missing_titles:
            print(path)
    else:
        print("所有文件都有title字段。")

# 指定posts目录路径
posts_directory = os.getcwd()
check_posts_titles(posts_directory)

