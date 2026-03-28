# -*- coding: utf-8 -*-
path = r"c:\Users\Administrator\Downloads\math-matrix-pro-2026\src\App.tsx"

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Dump exact content of suspicious lines
for ln in [244, 245]:
    line = lines[ln-1]
    print(f"=== LINE {ln} ===")
    print(repr(line))
    # Show each char with its codepoint
    for i, ch in enumerate(line):
        if ord(ch) > 127:
            print(f"  [{i}] U+{ord(ch):04X} = {ch}")
    print()

# Also scan the whole file for any line containing wrong text patterns
print("=== Scanning for remaining issues ===")
issues = {
    "'ặc": "đặc",
    "'ề": "đề",
    "'ạt": "đạt",
    "'ơn": "đơn",
    "'ạo": "đạo",
    "'ổi": "đổi",
    "'ộ": "độ",
    "'ã": "đã",
    "'ược": "được",
    "'úng": "đúng",
    "'ến": "đến",
    "'ều": "đều",
    "'ộng": "động",
    "'iều": "điều",
    "'ịnh": "định",
    "'ứng": "đứng",
    "nTi": "nội",
    "bT ": "bộ ",
    "li?u": "liệu",
    "nghi?m": "nghiệm",
    "s' ": "số ",
    "t.ng": "tổng",
    "b. ": "bổ ",
    "ph'i": "phối",
    "l?": "lệ",
}

for i, line in enumerate(lines):
    for bad, good in issues.items():
        if bad in line:
            print(f"L{i+1}: found '{bad}' -> should be '{good}'")
            print(f"  {line.rstrip()[:120]}")
