import os
import re

DOCS_DIR = "docs"
OUTPUT_FILE = os.path.join(DOCS_DIR, "index.html")

# YYYYMMDD(8桁連続数字）パターン)
date_pattern = re.compile(r"\b\d{8}\b")

files = []

for root, _, filenames in os.walk(DOCS_DIR):
    for name in filenames:

        # YYYYMMDDを含むファイルを除外
        if date_pattern.search(name):
            continue

        path = os.path.join(root, name)
        rel = os.path.relpath(path, ".")
        files.append(rel)

files.sort()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("<!DOCTYPE html>\n<html><head><meta charset='UTF-8'><title>Download Files</title></head><body>\n")
    f.write("<h1>Download Files</h1>\n<ul>\n")
    
    for file in files:
        f.write(f"<li><a href='{file}'>{file}</a></li>\n")

    f.write("</ul>\n</body></html>")

print("index.html generated at root")
