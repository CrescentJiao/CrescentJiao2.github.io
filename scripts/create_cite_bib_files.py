#!/usr/bin/env python3
import os
import re

def extract_bib_entry(bib_content, identifier):
    # 查找匹配的 BibTeX 条目
    entries = re.split(r'(?=@)', bib_content)
    for entry in entries:
        if identifier in entry:
            return entry.strip()
    return None

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
            cite_bib_path = os.path.join(entry.path, 'cite.bib')
            identifier = entry.name.replace('-', '')  # 移除标识符中的连字符
            
            # 提取对应的 BibTeX 条目
            bib_entry = extract_bib_entry(bib_content, identifier)
            
            if bib_entry:
                print(f"Creating cite.bib for {entry.path}...")
                with open(cite_bib_path, 'w', encoding='utf-8') as f:
                    f.write(bib_entry)
                print(f"Created {cite_bib_path}")
            else:
                print(f"No BibTeX entry found for {identifier}")

if __name__ == '__main__':
    main()
    print("Cite.bib files created successfully!") 