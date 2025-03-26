#!/usr/bin/env python3
import os
import re
import shutil
import tempfile

def get_doi_from_bib(bib_content, identifier):
    # 查找匹配的 BibTeX 条目
    entries = re.split(r'(?=@)', bib_content)
    for entry in entries:
        if identifier in entry and 'doi' in entry:
            doi_match = re.search(r'doi\s*=\s*{([^}]*)}', entry)
            if doi_match:
                return doi_match.group(1)
    return None

def update_publication_page(index_md_path, doi):
    # 读取原始文件内容
    with open(index_md_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # 分离 front matter
    parts = content.split('---', 2)
    if len(parts) < 3:
        print(f"Warning: Invalid front matter in {index_md_path}")
        return
    
    # 更新 front matter
    front_matter = parts[1].strip()
    if 'doi:' not in front_matter:
        front_matter += f"\ndoi: {doi}"
    
    # 确保所有必要的字段都存在
    required_fields = {
        "abstract": "''",
        "featured": "false",
        "url_pdf": "''",
        "url_code": "''",
        "url_dataset": "''",
        "url_poster": "''",
        "url_project": "''",
        "url_slides": "''",
        "url_source": "''",
        "url_video": "''",
        "image": "",
        "  caption": "''",
        "  focal_point": "''",
        "  preview_only": "false",
        "projects": "[]"
    }
    
    for field, default_value in required_fields.items():
        if field not in front_matter:
            front_matter += f"\n{field}: {default_value}"
    
    # 创建新的内容
    new_content = f"---\n{front_matter}\n---\n"
    
    # 使用临时文件安全地更新内容
    with tempfile.NamedTemporaryFile(mode='w', delete=False, encoding='utf-8') as temp_file:
        temp_file.write(new_content)
    
    # 替换原始文件
    shutil.move(temp_file.name, index_md_path)

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
            index_md_path = os.path.join(entry.path, 'index.md')
            if os.path.exists(index_md_path):
                print(f"Processing {entry.path}...")
                identifier = entry.name.replace('-', '')  # 移除标识符中的连字符
                doi = get_doi_from_bib(bib_content, identifier)
                
                if doi:
                    print(f"Found DOI: {doi}")
                    update_publication_page(index_md_path, doi)
                    print(f"Updated {index_md_path}")
                else:
                    print(f"No DOI found for {identifier}")

if __name__ == '__main__':
    main()
    print("Publication pages updated successfully!") 