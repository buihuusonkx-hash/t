# -*- coding: utf-8 -*-
import re

path = r"c:\Users\Administrator\Downloads\math-matrix-pro-2026\src\App.tsx"

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# Precise replacements - corrupted string -> correct Vietnamese
replacements = [
    # Comments - line 40
    ("// KhYi tạo", "// Khởi tạo"),
    # Comments - line 58
    ("// --- Logic Nghi?p vụ ---", "// --- Logic Nghiệp vụ ---"),
    # Comments - line 67
    ("// NLC: T.ng từ NB, TH, VD", "// NLC: Tổng từ NB, TH, VD"),
    # Comments - line 69
    ("// DS: Đếm s' câu (m-i câu 4 ý)", "// DS: Đếm số câu (mỗi câu 4 ý)"),
    # Comments - line 71
    ("// TLN: T.ng từ TH, VD, VDC", "// TLN: Tổng từ TH, VD, VDC"),
    # Comments - line 81
    ("// Gom tất cả các 'ơn v< kiến thức vào mTt danh sách phẳng", "// Gom tất cả các đơn vị kiến thức vào một danh sách phẳng"),
    # Alert - line 89
    ("""alert("Vui lòng nhập 'S' tiết' 'f tính toán!")""", """alert("Vui lòng nhập 'Số tiết' để tính toán!")"""),
    # Comments - line 91
    ("// Reset toàn bT dữ li?u câu hỏi cũ", "// Reset toàn bộ dữ liệu câu hỏi cũ"),
    # Comments - line 97
    ("// Hàm b. trợ phân ph'i s' câu dựa trên tỷ l? s' tiết (Largest Remainder Method)", "// Hàm bổ trợ phân phối số câu dựa trên tỷ lệ số tiết (Largest Remainder Method)"),
    # Comments - line 107
    ("// 1. Phân b. Đúng/Sai (T.ng 4 câu)", "// 1. Phân bổ Đúng/Sai (Tổng 4 câu)"),
    # Comments - line 110
    ("// 2. Phân b. Trả lời ngắn (T.ng 6 câu: 2 TH - 2 VD - 2 VDC)", "// 2. Phân bổ Trả lời ngắn (Tổng 6 câu: 2 TH - 2 VD - 2 VDC)"),
    # Comments - line 115
    ("// 3. Phân b. Trắc nghi?m NLC (T.ng 12 câu: Chia mức NB và TH, bỏ VD)", "// 3. Phân bổ Trắc nghiệm NLC (Tổng 12 câu: Chia mức NB và TH, bỏ VD)"),
    # Comments - line 120
    ("// --- THỰC HI?N ĐI?N DỮ LI?U ---", "// --- THỰC HIỆN ĐIỀN DỮ LIỆU ---"),
    # Comments - line 124
    ("// Gán Đúng/Sai (vào mức 0 - NB, trong ma trận sẽ tự hifu cấu trúc 1NB-2TH-1VD)", "// Gán Đúng/Sai (vào mức 0 - NB, trong ma trận sẽ tự hiểu cấu trúc 1NB-2TH-1VD)"),
    # Comments - line 140
    ("// Gán Trắc nghi?m NLC (Chia 60% NB - 40% TH)", "// Gán Trắc nghiệm NLC (Chia 60% NB - 40% TH)"),
    # Comments - line 153
    ("// --- BƯsC CUỐI: KI,M TRA PHỦ KÍN ---", "// --- BƯỚC CUỐI: KIỂM TRA PHỦ KÍN ---"),
    # Comments - line 154
    ('// Nếu vẫn còn dòng nào "trắng" câu hỏi, lấy 1 câu NLC từ dòng nhiều nhất chuyfn sang', '// Nếu vẫn còn dòng nào "trắng" câu hỏi, lấy 1 câu NLC từ dòng nhiều nhất chuyển sang'),
    # Comments - line 160
    ('// Cấp "vé v>t" 1 câu NLC Nhận biết cho dòng b< tr\'ng', '// Cấp "vé vớt" 1 câu NLC Nhận biết cho dòng bị trống'),
    # Value - line 161
    ('"B. sung"', '"Bổ sung"'),
    # Comments - line 172
    ("// 1. Thu thập tất cả nTi dung vào danh sách phẳng", "// 1. Thu thập tất cả nội dung vào danh sách phẳng"),
    # Comments - line 184
    ("// 2. Sắp xếp nTi dung theo S' tiết giảm dần (Chương quan trọng 'ứng trư>c)", "// 2. Sắp xếp nội dung theo Số tiết giảm dần (Chương quan trọng đứng trước)"),
    # Comments - line 187
    ("// 3. Reset toàn bT s' câu TLN cũ", "// 3. Reset toàn bộ số câu TLN cũ"),
    # Comments - line 195
    ('// 4. Đ<nh nghĩa 6 "v< trí" câu TLN cần phân b.', '// 4. Định nghĩa 6 "vị trí" câu TLN cần phân bổ'),
    # Comments - line 207
    ("// M-i nTi dung sẽ ch? nhận TỐI ĐA 1 câu TLN cho 'ến khi hết vòng.", "// Mỗi nội dung sẽ chỉ nhận TỐI ĐA 1 câu TLN cho đến khi hết vòng."),
    # Tab labels - lines 242-245
    ("'Nhập li?u'", "'Nhập liệu'"),
    ("label: 'Ma trận \u2018ặc tả'", "label: 'Ma trận đặc tả'"),
    ("label: 'Tạo \u2018ề'", "label: 'Tạo đề'"),
    # Separator
    (">?</span>", ">›</span>"),
    # TabNhapLieu labels
    ("Cấu trúc \u2018ề thi", "Cấu trúc đề thi"),
    ("Xây dựng nTi dung kiến thức và phân b. câu hỏi", "Xây dựng nội dung kiến thức và phân bổ câu hỏi"),
    ("Tự \u2018Tng phân b. (Chuẩn 2026)", "Tự động phân bổ (Chuẩn 2026)"),
    ("Phân b. TLN (Rải \u2018ều)", "Phân bổ TLN (Rải đều)"),
    ("Tên chương/chủ \u2018ề (ví dụ: Chương I. Ứng dụng \u2018ạo hàm...)", "Tên chương/chủ đề (ví dụ: Chương I. Ứng dụng đạo hàm...)"),
    (">NTi dung bài học<", ">Nội dung bài học<"),
    ("Tên bài học/nTi dung (VD: Tính \u2018ơn \u2018i?u của hàm s\u2019)", "Tên bài học/nội dung (VD: Tính đơn điệu của hàm số)"),
    ('>o" Đã tìm thấy YCCĐ<', '>✓ Đã tìm thấy YCCĐ<'),
    (">S' tiết<", ">Số tiết<"),
    ("Yêu cầu cần \u2018ạt", "Yêu cầu cần đạt"),
    ("Thêm nTi dung bài học", "Thêm nội dung bài học"),
    ("{/* Nút \u2018iều hư>ng */}", "{/* Nút điều hướng */}"),
    ("Xem Ma trận \u2018ề ", "Xem Ma trận đề "),
    # TabMaTran
    ("MA TRẬN Đ? KI,M TRA ĐSNH KỲ", "MA TRẬN ĐỀ KIỂM TRA ĐỊNH KỲ"),
    ('M"N: {monHoc.toUpperCase()} - LsP 12', 'MÔN: {monHoc.toUpperCase()} - LỚP 12'),
    (">NTi dung kiến thức<", ">Nội dung kiến thức<"),
    (">S' tiết<", ">Số tiết<"),
    (">Trắc nghi?m (12 câu)<", ">Trắc nghiệm (12 câu)<"),
    (">T.ng<", ">Tổng<"),
    (">T\"NG C~NG<", ">TỔNG CỘNG<"),
    (">t.ng s' câu<", ">tổng số câu<"),
    ("? Nhập li?u", "◂ Nhập liệu"),
    ("Xem Ma trận \u2018ặc tả ", "Xem Ma trận đặc tả "),
    # TabDacTa
    ("// Helper lấy yêu cầu cần \u2018ạt theo mức \u2018T", "// Helper lấy yêu cầu cần đạt theo mức độ"),
    ("BẢNG MA TRẬN ĐẶC TẢ CHI TIẾT Đ? KI,M TRA", "BẢNG MA TRẬN ĐẶC TẢ CHI TIẾT ĐỀ KIỂM TRA"),
    ("HƯsNG DẪN CHẤM V? ĐÁNH GIÁ N,NG LỰC", "HƯỚNG DẪN CHẤM VÀ ĐÁNH GIÁ NĂNG LỰC"),
    ("Tự \u2018Tng từ CSDL chuẩn", "Tự động từ CSDL chuẩn"),
    (">NTi dung<", ">Nội dung<"),
    (">Mức \u2018T<", ">Mức độ<"),
    ("? Ma trận", "◂ Ma trận"),
    ("Tạo \u2018ề thi ", "Tạo đề thi "),
    # TabTaoDe
    ("// Hàm sinh \u2018ề dựa trên dữ li?u từ Ma trận \u2018ặc tả", "// Hàm sinh đề dựa trên dữ liệu từ Ma trận đặc tả"),
    ("// S' thứ tự câu hỏi xuyên su't", "// Số thứ tự câu hỏi xuyên suốt"),
    ("// Duy?t qua toàn bT dữ li?u người dùng \u2018ã nhập", "// Duyệt qua toàn bộ dữ liệu người dùng đã nhập"),
    ("// --- PHẦN I: TRẮC NGHI?M NHI?U PHƯƠNG ÁN (NLC) ---", "// --- PHẦN I: TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN (NLC) ---"),
    ("// --- PHẦN II: TRẮC NGHI?M ĐsNG/SAI (DS) ---", "// --- PHẦN II: TRẮC NGHIỆM ĐÚNG/SAI (DS) ---"),
    ("// --- PHẦN III: TRẢ LoI NGẮN (TLN) ---", "// --- PHẦN III: TRẢ LỜI NGẮN (TLN) ---"),
    ("// GTp các phần lại và cập nhật state", "// Gộp các phần lại và cập nhật state"),
    ("{/* Header \u2018iều khifn */}", "{/* Header điều khiển */}"),
    ("Sinh \u2018ề từ Ma trận \u2018ặc tả", "Sinh đề từ Ma trận đặc tả"),
    ("TẠO Đ? THEO ĐẶC TẢ", "TẠO ĐỀ THEO ĐẶC TẢ"),
    ("? Quay lại Đặc tả", "◂ Quay lại Đặc tả"),
    ("Câu trắc nghi?m nhiều phương án lựa chọn.", "Câu trắc nghiệm nhiều phương án lựa chọn."),
    ("Câu trắc nghi?m \u2018úng sai.", "Câu trắc nghiệm đúng sai."),
    ("Câu trắc nghi?m trả lời ngắn.", "Câu trắc nghiệm trả lời ngắn."),
    ("Đáp s\u2019: ................", "Đáp số: ................"),
    ("// --- Các Component giao di?n nhỏ ---", "// --- Các Component giao diện nhỏ ---"),
    # Auto-fill comment
    ("// Auto-fill yêu cầu cần \u2018ạt khi thay \u2018.i tên bài học", "// Auto-fill yêu cầu cần đạt khi thay đổi tên bài học"),
    # Line 767 - the problematic unterminated string
    ("Câu hỏi \u2018ược chọn lọc chính xác theo: {data.reduce((acc, c) => acc + c.noiDungs.length, 0)} \u2018ơn v< kiến thức \u2018ã thiết lập.", "Câu hỏi được chọn lọc chính xác theo: {data.reduce((acc, c) => acc + c.noiDungs.length, 0)} đơn vị kiến thức đã thiết lập."),
]

count = 0
for old, new in replacements:
    if old in text:
        text = text.replace(old, new)
        count += 1

# Also fix any remaining isolated corrupted patterns
# Fix 'nút điều hướng' patterns with different unicode chars
text = text.replace("{/* N\u00fat \u2018i\u1ec1u h\u01b0>ng */}", "{/* Nút điều hướng */}")
text = text.replace("{/* N\u00fat \u2018i\u1ec1u h\u01b0\u003eng */}", "{/* Nút điều hướng */}")

# Clean unused imports
text = text.replace("import { PenSquare, FileText, Download, Plus, Trash2, ChevronRight, Sparkles, RefreshCw, CheckCircle, AlertCircle, Settings, X, Key, LogOut, BookOpen, Layout, ListChecks, FileJson } from 'lucide-react';",
    "import { PenSquare, FileText, Download, Plus, Trash2, ChevronRight, Sparkles, RefreshCw, CheckCircle, X, BookOpen, Layout, ListChecks, FileJson } from 'lucide-react';")

with open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(text)

print(f"Fixed {count} replacements")
print("Done!")
