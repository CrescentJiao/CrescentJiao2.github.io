#!/usr/bin/env python3
import os
import re

def extract_field_from_bib(entry, field):
    match = re.search(rf'{field}\s*=\s*{{([^}}]*)}}', entry)
    if match:
        return match.group(1)
    return None

def get_entry_from_bib(bib_content, identifier):
    entries = re.split(r'(?=@)', bib_content)
    for entry in entries:
        if identifier in entry:
            return entry.strip()
    return None

def create_cite_bib(entry, output_dir):
    """为单个出版物创建 cite.bib 文件"""
    # 直接在文章文件夹中创建 cite.bib
    output_path = os.path.join(output_dir, 'cite.bib')
    
    # 写入文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(entry)

def main():
    # 设置工作目录
    script_dir = os.path.dirname(os.path.abspath(__file__))
    os.chdir(os.path.join(script_dir, '..'))
    
    # 读取 publications.bib 文件
    with open('content/publication/publications.bib', 'r', encoding='utf-8') as f:
        bib_content = f.read()
    
    # 处理每个出版物文件夹
    for entry in os.scandir('content/publication'):
        if entry.is_dir():
            print(f"Creating cite.bib for {entry.path}...")
            identifier = entry.name.replace('-', '')  # 移除标识符中的连字符
            bib_entry = get_entry_from_bib(bib_content, identifier)
            
            if bib_entry:
                create_cite_bib(bib_entry, entry.path)
                print(f"Created {entry.path}/cite.bib")
            else:
                print(f"No BibTeX entry found for {identifier}")

if __name__ == '__main__':
    main()
    print("Cite.bib files created successfully!") 