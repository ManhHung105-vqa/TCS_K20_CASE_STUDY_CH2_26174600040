ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất W: "))  # Đã sửa: Ép kiểu float cho input
so_phut = int(input("Nhập số phút: "))
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000

print(f"Máy: {ma_may}")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")      # Đã sửa: Tên biến dien_nang_kwh và thêm ngoặc đóng )

# --- MÔ TẢ CÁC LỖI ĐÃ PHÁT HIỆN ---
# Lỗi 1: SyntaxError tại dòng 7 do thiếu dấu ngoặc đóng ')' ở cuối câu lệnh print.
# Lỗi 2: TypeError tại dòng 4 do cong_suat_w chưa ép kiểu số thực (float) nên không thể thực hiện phép toán số học.
# Lỗi 3: NameError tại dòng 7 do gọi biến 'dien_nang' thay vì tên đúng đã khai báo là 'dien_nang_kwh'.