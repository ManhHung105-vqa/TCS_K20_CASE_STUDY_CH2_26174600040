from datetime import datetime

ma_phien = input("Nhập mã phiên: ")
ma_may = input("Nhập mã máy: ")
cong_suat_w = float(input("Nhập công suất thiết bị (W): "))
so_phut = int(input("Nhập thời gian sử dụng (phút): "))
don_gia_kwh = float(input("Nhập đơn giá điện (VND/kWh): "))

dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh
tren_60_phut = so_phut > 60
ghi_nhan_luc = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

print(f"\nMã phiên: {ma_phien}")
print(f"Máy: {ma_may}")
print(f"Công suất: {cong_suat_w:.2f} W")
print(f"Thời lượng: {so_phut} phút")
print(f"Điện năng: {dien_nang_kwh:.3f} kWh")
print(f"Chi phí: {chi_phi:,.2f} VND")
print(f"Trên 60 phút: {tren_60_phut}")
print(f"Ghi nhận lúc: {ghi_nhan_luc}")