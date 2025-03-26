#!/usr/bin/env python3
import os
import re
import shutil
import tempfile
from datetime import datetime
import yaml
from dateutil import parser

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

def get_publication_type(entry):
    """获取出版物类型"""
    if '@article' in entry.lower():
        return ['article-journal']
    elif '@inproceedings' in entry.lower():
        return ['paper-conference']
    elif '@book' in entry.lower():
        return ['book']
    elif '@incollection' in entry.lower():
        return ['chapter']
    return ['other']

def update_publication_page(bib_entry, output_dir):
    """更新单个出版物页面的 front matter"""
    # 从 BibTeX 条目中提取信息
    title = extract_field_from_bib(bib_entry, 'title') or ''
    authors_str = extract_field_from_bib(bib_entry, 'author') or ''
    authors = [author.strip() for author in authors_str.split(' and ')]
    year = extract_field_from_bib(bib_entry, 'year') or datetime.now().year
    journal = extract_field_from_bib(bib_entry, 'journal') or ''
    booktitle = extract_field_from_bib(bib_entry, 'booktitle') or ''
    doi = extract_field_from_bib(bib_entry, 'doi') or ''
    abstract = extract_field_from_bib(bib_entry, 'abstract') or ''
    
    # 直接在文章文件夹中创建 index.md
    output_path = os.path.join(output_dir, 'index.md')
    
    # 获取出版物类型
    pub_type = get_publication_type(bib_entry)
    
    # 创建 front matter
    front_matter = {
        'title': title,
        'authors': authors,
        'date': f'{year}-01-01',
        'publishDate': datetime.now().isoformat(),
        'publication_types': pub_type,
        'publication': journal or booktitle,
        'doi': doi,
        'abstract': abstract,
        'featured': False,
        'url_pdf': '',
        'url_code': '',
        'url_dataset': '',
        'url_poster': '',
        'url_project': '',
        'url_slides': '',
        'url_source': '',
        'url_video': '',
        'image': {
            'caption': '',
            'focal_point': '',
            'preview_only': False
        },
        'projects': []
    }
    
    # 将 front matter 转换为 YAML
    yaml_content = yaml.dump(front_matter, allow_unicode=True, sort_keys=False)
    
    # 写入文件
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write('---\n')
        f.write(yaml_content)
        f.write('---\n\n')

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
            print(f"Processing {entry.path}...")
            identifier = entry.name.replace('-', '')  # 移除标识符中的连字符
            bib_entry = get_entry_from_bib(bib_content, identifier)
            
            if bib_entry:
                update_publication_page(bib_entry, entry.path)
                print(f"Updated {entry.path}/index.md")
            else:
                print(f"No BibTeX entry found for {identifier}")

if __name__ == '__main__':
    main()
    print("Publication pages updated successfully!") 