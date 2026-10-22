ma_may = input("Nhập mã máy: ")
print("Kiểu mã máy:", type(ma_may))

cong_suat_raw = input("Nhập công suất W: ")
print("Kiểu ban đầu công suất:", type(cong_suat_raw))

so_phut_raw = input("Nhập số phút: ")
print("Kiểu ban đầu số phút:", type(so_phut_raw))

don_gia_raw = input("Nhập đơn giá: ")
print("Kiểu ban đầu đơn giá:", type(don_gia_raw))

cong_suat_w = float(cong_suat_raw)
so_phut = int(so_phut_raw)
don_gia_kwh = float(don_gia_raw)

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("\n--- Kết quả tính toán ---")
print("Điện năng tiêu thụ (kWh):", dien_nang_kwh)
print("Chi phí (VND):", chi_phi)