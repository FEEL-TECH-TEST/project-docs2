import os
import re

DOCS_DIR = "docs"
OUTPUT_FILE = os.path.join(DOCS_DIR, "index.md")

# YYYYMMDD(8桁連続数字）パターン)
date_pattern = re.compile(r"\b\d{8}\b")

files = []

for root, _, filenames in os.walk(DOCS_DIR):
    for name in filenames:
        # index自身は除外
        if name == "index.md":
            continue

        # YYYYMMDDを含むファイルを除外
        if date_pattern.search(name):
            continue

        path = os.path.join(root, name)
        rel = os.path.relpath(path, DOCS_DIR)
        files.append(rel)

files.sort()

with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
    f.write("# Download Files\n\n")
    for file in files:
        f.write(f"- [{file}]({file})\n")

print("index.md generated")
