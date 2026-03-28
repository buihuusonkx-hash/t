# -*- coding: utf-8 -*-
path = r"c:\Users\Administrator\Downloads\math-matrix-pro-2026\src\App.tsx"

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Find lines with curly quotes (unicode smart quotes) which indicate remaining corruption
bad_lines = []
for i, line in enumerate(lines):
    if '\u2018' in line or '\u2019' in line or '\u201c' in line or '\u201d' in line:
        bad_lines.append((i+1, line.rstrip()[:150]))

with open(r"c:\Users\Administrator\Downloads\math-matrix-pro-2026\bad_lines.txt", 'w', encoding='utf-8') as f:
    f.write(f"Found {len(bad_lines)} lines with smart quotes\n")
    for num, text in bad_lines:
        f.write(f"L{num}: {text}\n")

print(f"Found {len(bad_lines)} bad lines. Check bad_lines.txt")
