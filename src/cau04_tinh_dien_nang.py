cong_suat_w = 250
so_phut = 90
don_gia_kwh = 3000

# Dự đoán: dien_nang_kwh = 250 * 90 / 60 / 1000 = 0.375
# Dự đoán: chi_phi = 0.375 * 3000 = 1125.0
dien_nang_kwh = cong_suat_w * so_phut / 60 / 1000
chi_phi = dien_nang_kwh * don_gia_kwh

print("Điện năng (kWh):", dien_nang_kwh, "| Kiểu:", type(dien_nang_kwh))
print("Chi phí (VND):", chi_phi, "| Kiểu:", type(chi_phi))

so_phut_moi = 60
dien_nang_moi = cong_suat_w * so_phut_moi / 60 / 1000
chi_phi_moi = dien_nang_moi * don_gia_kwh

print("\n--- Khi thời gian giảm còn 60 phút ---")
print("Điện năng mới (kWh):", dien_nang_moi, "| Chi phí mới (VND):", chi_phi_moi)
# So sánh: Điện năng tiêu thụ và chi phí điện giảm tỉ lệ thuận khi số phút giảm từ 90 xuống 60.