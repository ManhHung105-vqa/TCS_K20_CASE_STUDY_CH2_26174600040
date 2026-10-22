from datetime import datetime

thoi_diem = datetime.now()
thoi_diem_text = thoi_diem.strftime("%Y-%m-%d %H:%M:%S")

print(thoi_diem)
print(type(thoi_diem))
print(thoi_diem_text)
print(type(thoi_diem_text))

bat_dau = datetime(2026, 10, 14, 13, 15)
ket_thuc = datetime(2026, 10, 14, 15, 5)

# Dự đoán phép trừ: 15:05 - 13:15 = 1 giờ 50 phút (1:50:00)
thoi_luong = ket_thuc - bat_dau
print(thoi_luong)
print(type(thoi_luong))

# Giải thích sự khác nhau:
# - datetime: Đối tượng lưu trữ đầy đủ ngày, tháng, năm, giờ, phút, giây của một mốc thời gian cụ thể.
# - str: Chuỗi văn bản thuần túy đại diện cho thời gian (không thể thực hiện phép toán thời gian).
# - timedelta: Đối tượng lưu trữ khoảng thời gian chênh lệch giữa 2 mốc datetime.