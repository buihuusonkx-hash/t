# -*- coding: utf-8 -*-
path = r"c:\Users\Administrator\Downloads\math-matrix-pro-2026\src\App.tsx"

with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

# All remaining corrupted patterns -> correct Vietnamese
replacements = [
    # Tab labels
    ("label: 'Ma trận \u0027ặc tả'", "label: 'Ma trận đặc tả'"),
    ("label: 'Tạo \u0027ề'", "label: 'Tạo đề'"),
    # Auto-fill comment
    ("yêu cầu cần \u0027ạt khi thay \u0027.i tên bài học", "yêu cầu cần đạt khi thay đổi tên bài học"),
    # Cấu trúc
    ("Cấu trúc \u0027ề thi", "Cấu trúc đề thi"),
    # Buttons
    ("Tự \u0027Tng phân b.", "Tự động phân bổ"),
    ("Phân b. TLN (Rải \u0027ều)", "Phân bổ TLN (Rải đều)"),
    # Placeholder
    ("chủ \u0027ề (ví dụ: Chương I. Ứng dụng \u0027ạo hàm...)", "chủ đề (ví dụ: Chương I. Ứng dụng đạo hàm...)"),
    ("nTi dung (VD: Tính \u0027ơn \u0027i?u của hàm s\u0027)", "nội dung (VD: Tính đơn điệu của hàm số)"),
    # Labels
    ("Yêu cầu cần \u0027ạt", "Yêu cầu cần đạt"),
    ("Nút \u0027iều hư>ng", "Nút điều hướng"),
    ("Xem Ma trận \u0027ề ", "Xem Ma trận đề "),
    ("Xem Ma trận \u0027ặc tả ", "Xem Ma trận đặc tả "),
    # Helper comment
    ("yêu cầu cần \u0027ạt theo mức \u0027T", "yêu cầu cần đạt theo mức độ"),
    # Tạo đề thi
    ("Tạo \u0027ề thi ", "Tạo đề thi "),
    # Hàm sinh đề
    ("Hàm sinh \u0027ề dựa trên dữ li?u từ Ma trận \u0027ặc tả", "Hàm sinh đề dựa trên dữ liệu từ Ma trận đặc tả"),
    # Duyệt qua
    ("Duy?t qua toàn bT dữ li?u người dùng \u0027ã nhập", "Duyệt qua toàn bộ dữ liệu người dùng đã nhập"),
    # Header điều khiển
    ("Header \u0027iều khifn", "Header điều khiển"),
    # Sinh đề
    ("Sinh \u0027ề từ Ma trận \u0027ặc tả", "Sinh đề từ Ma trận đặc tả"),
    # Câu hỏi được chọn lọc
    ("Câu hỏi \u0027ược chọn lọc chính xác theo: {data.reduce((acc, c) => acc + c.noiDungs.length, 0)} \u0027ơn v< kiến thức \u0027ã thiết lập.",
     "Câu hỏi được chọn lọc chính xác theo: {data.reduce((acc, c) => acc + c.noiDungs.length, 0)} đơn vị kiến thức đã thiết lập."),
    # Câu trắc nghiệm
    ("Câu trắc nghi?m \u0027úng sai.", "Câu trắc nghiệm đúng sai."),
    ("Câu trắc nghi?m nhiều", "Câu trắc nghiệm nhiều"),
    ("Câu trắc nghi?m trả lời ngắn.", "Câu trắc nghiệm trả lời ngắn."),
    # Remaining misc patterns
    (">NTi dung bài học<", ">Nội dung bài học<"),
    (">NTi dung kiến thức<", ">Nội dung kiến thức<"),
    (">NTi dung<", ">Nội dung<"),
    ("Thêm nTi dung bài học", "Thêm nội dung bài học"),
    ("Xây dựng nTi dung kiến thức và phân b. câu hỏi", "Xây dựng nội dung kiến thức và phân bổ câu hỏi"),
    (">S\u0027 tiết<", ">Số tiết<"),
    (">t.ng s\u0027 câu<", ">tổng số câu<"),
    (">Trắc nghi?m (12 câu)<", ">Trắc nghiệm (12 câu)<"),
    (">T.ng<", ">Tổng<"),
    (">T\"NG C~NG<", ">TỔNG CỘNG<"),
    (">Mức \u0027T<", ">Mức độ<"),
    ("MA TRẬN Đ? KI,M TRA ĐSNH KỲ", "MA TRẬN ĐỀ KIỂM TRA ĐỊNH KỲ"),
    ("M\"N: {monHoc.toUpperCase()} - LsP 12", "MÔN: {monHoc.toUpperCase()} - LỚP 12"),
    ("BẢNG MA TRẬN ĐẶC TẢ CHI TIẾT Đ? KI,M TRA", "BẢNG MA TRẬN ĐẶC TẢ CHI TIẾT ĐỀ KIỂM TRA"),
    ("HƯsNG DẪN CHẤM V? ĐÁNH GIÁ N,NG LỰC", "HƯỚNG DẪN CHẤM VÀ ĐÁNH GIÁ NĂNG LỰC"),
    ("Tự \u0027Tng từ CSDL chuẩn", "Tự động từ CSDL chuẩn"),
    ("TẠO Đ? THEO ĐẶC TẢ", "TẠO ĐỀ THEO ĐẶC TẢ"),
    ("Đáp s\u0027: ", "Đáp số: "),
    ("Các Component giao di?n nhỏ", "Các Component giao diện nhỏ"),
    # Comments
    ("// KhYi tạo", "// Khởi tạo"),
    ("// --- Logic Nghi?p vụ ---", "// --- Logic Nghiệp vụ ---"),
    ("// NLC: T.ng từ NB, TH, VD", "// NLC: Tổng từ NB, TH, VD"),
    ("// DS: Đếm s\u0027 câu (m-i câu 4 ý)", "// DS: Đếm số câu (mỗi câu 4 ý)"),
    ("// TLN: T.ng từ TH, VD, VDC", "// TLN: Tổng từ TH, VD, VDC"),
    ("// Gom tất cả các \u0027ơn v< kiến thức vào mTt danh sách phẳng", "// Gom tất cả các đơn vị kiến thức vào một danh sách phẳng"),
    ("\"Vui lòng nhập \u0027S\u0027 tiết\u0027 \u0027f tính toán!\"", "\"Vui lòng nhập 'Số tiết' để tính toán!\""),
    ("// Reset toàn bT dữ li?u câu hỏi cũ", "// Reset toàn bộ dữ liệu câu hỏi cũ"),
    ("// Hàm b. trợ phân ph\u0027i s\u0027 câu dựa trên tỷ l? s\u0027 tiết (Largest Remainder Method)", "// Hàm bổ trợ phân phối số câu dựa trên tỷ lệ số tiết (Largest Remainder Method)"),
    ("// 1. Phân b. Đúng/Sai (T.ng 4 câu)", "// 1. Phân bổ Đúng/Sai (Tổng 4 câu)"),
    ("// 2. Phân b. Trả lời ngắn (T.ng 6 câu: 2 TH - 2 VD - 2 VDC)", "// 2. Phân bổ Trả lời ngắn (Tổng 6 câu: 2 TH - 2 VD - 2 VDC)"),
    ("// 3. Phân b. Trắc nghi?m NLC (T.ng 12 câu: Chia mức NB và TH, bỏ VD)", "// 3. Phân bổ Trắc nghiệm NLC (Tổng 12 câu: Chia mức NB và TH, bỏ VD)"),
    ("// --- THỰC HI?N ĐI?N DỮ LI?U ---", "// --- THỰC HIỆN ĐIỀN DỮ LIỆU ---"),
    ("trong ma trận sẽ tự hifu cấu trúc", "trong ma trận sẽ tự hiểu cấu trúc"),
    ("// Gán Trắc nghi?m NLC (Chia 60% NB - 40% TH)", "// Gán Trắc nghiệm NLC (Chia 60% NB - 40% TH)"),
    ("// --- BƯsC CUỐI: KI,M TRA PHỦ KÍN ---", "// --- BƯỚC CUỐI: KIỂM TRA PHỦ KÍN ---"),
    ("từ dòng nhiều nhất chuyfn sang", "từ dòng nhiều nhất chuyển sang"),
    ("\"vé v>t\" 1 câu NLC Nhận biết cho dòng b< tr\u0027ng", "\"vé vớt\" 1 câu NLC Nhận biết cho dòng bị trống"),
    ("\"B. sung\"", "\"Bổ sung\""),
    ("// 1. Thu thập tất cả nTi dung vào danh sách phẳng", "// 1. Thu thập tất cả nội dung vào danh sách phẳng"),
    ("nTi dung theo S\u0027 tiết giảm dần (Chương quan trọng \u0027ứng trư>c)", "nội dung theo Số tiết giảm dần (Chương quan trọng đứng trước)"),
    ("// 3. Reset toàn bT s\u0027 câu TLN cũ", "// 3. Reset toàn bộ số câu TLN cũ"),
    ("// 4. Đ<nh nghĩa 6 \"v< trí\" câu TLN cần phân b.", "// 4. Định nghĩa 6 \"vị trí\" câu TLN cần phân bổ"),
    ("// M-i nTi dung sẽ ch? nhận TỐI ĐA 1 câu TLN cho \u0027ến khi hết vòng.", "// Mỗi nội dung sẽ chỉ nhận TỐI ĐA 1 câu TLN cho đến khi hết vòng."),
    ("// --- PHẦN I: TRẮC NGHI?M NHI?U PHƯƠNG ÁN (NLC) ---", "// --- PHẦN I: TRẮC NGHIỆM NHIỀU PHƯƠNG ÁN (NLC) ---"),
    ("// --- PHẦN II: TRẮC NGHI?M ĐsNG/SAI (DS) ---", "// --- PHẦN II: TRẮC NGHIỆM ĐÚNG/SAI (DS) ---"),
    ("// --- PHẦN III: TRẢ LoI NGẮN (TLN) ---", "// --- PHẦN III: TRẢ LỜI NGẮN (TLN) ---"),
    ("// GTp các phần lại và cập nhật state", "// Gộp các phần lại và cập nhật state"),
    ("// S\u0027 thứ tự câu hỏi xuyên su\u0027t", "// Số thứ tự câu hỏi xuyên suốt"),
    # Navigation labels
    ("◂ Nhập li?u", "◂ Nhập liệu"),
    ("o\" Đã tìm thấy YCCĐ", "✓ Đã tìm thấy YCCĐ"),
]

count = 0
for old, new in replacements:
    if old in text:
        text = text.replace(old, new)
        count += 1
        print(f"Fixed: {old[:60]}...")

with open(path, 'w', encoding='utf-8', newline='\n') as f:
    f.write(text)

print(f"\nTotal: {count} replacements applied")
