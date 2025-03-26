#!/bin/bash

# 设置工作目录
cd "$(dirname "$0")/.."

# 运行 Python 脚本更新文件
echo "Updating publication pages..."
python3 scripts/update_publication_pages.py

echo "Creating cite.bib files..."
python3 scripts/create_cite_bib_files.py

echo "All files updated successfully!" 