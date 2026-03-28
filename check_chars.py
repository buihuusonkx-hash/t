# -*- coding: utf-8 -*-
path = r"c:\Users\Administrator\Downloads\math-matrix-pro-2026\src\App.tsx"

with open(path, 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Check specific problem lines and dump their hex
for ln in [244, 245, 343, 345, 352, 355, 375, 398, 409, 413, 428, 476, 482, 488, 504, 505, 513, 514, 515, 518, 557, 569, 573, 577, 581, 584, 594, 603, 620, 621, 628, 637, 638, 639, 671, 674, 677, 688, 691, 698, 701, 719, 733, 753, 759, 764, 767, 781, 800, 818, 843, 868, 878, 888]:
    if ln <= len(lines):
        line = lines[ln-1].rstrip()
        # Find any chars that look suspicious
        problems = []
        for ci, ch in enumerate(line):
            cp = ord(ch)
            # Flag non-ASCII chars that aren't standard Vietnamese
            if cp > 127 and ch not in 'àáạảãăắằặẳẵâấầậẩẫèéẹẻẽêếềệểễìíịỉĩòóọỏõôốồộổỗơớờợởỡùúụủũưứừựửữỳýỵỷỹđÀÁẠẢÃĂẮẰẶẲẴÂẤẦẬẨẪÈÉẸẺẼÊẾỀỆỂỄÌÍỊỈĨÒÓỌỎÕÔỐỒỘỔỖƠỚỜỢỞỠÙÚỤỦŨƯỨỪỰỬỮỲÝỴỶỸĐ›✓':
                problems.append(f"  pos {ci}: U+{cp:04X} '{ch}'")
        if problems:
            print(f"L{ln}: {line[:120]}")
            for p in problems:
                print(p)
            print()

# Also do a global scan for the curly-quote-like chars
print("=== Global scan for problematic chars ===")
count = 0
for i, line in enumerate(lines):
    for ci, ch in enumerate(line):
        cp = ord(ch)
        if cp in (0x2018, 0x2019, 0x201C, 0x201D, 0x2013, 0x2014):
            print(f"L{i+1} pos {ci}: U+{cp:04X} '{ch}' context: ...{line[max(0,ci-10):ci+10].rstrip()}...")
            count += 1
print(f"Total: {count} smart-quote chars found")
