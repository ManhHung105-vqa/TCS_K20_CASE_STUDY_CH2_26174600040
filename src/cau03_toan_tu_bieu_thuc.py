tong_phut = 135
cong_suat_w = 250

so_gio = tong_phut // 60
so_phut_con_lai = tong_phut % 60
print(f"Thời gian: {so_gio} giờ và {so_phut_con_lai} phút")

su_dung_lau = tong_phut > 60
print("Sử dụng lâu (>60 phút):", su_dung_lau)

du_lieu_hop_le = (cong_suat_w > 0) and (tong_phut > 0)
print("Dữ liệu hợp lệ:", du_lieu_hop_le)

# Dự đoán: 100 + 20 * 3 = 160 (nhân trước cộng sau)
# Dự đoán: (100 + 20) * 3 = 360 (thực hiện trong ngoặc trước)
print("Kết quả 100 + 20 * 3:", 100 + 20 * 3)
print("Kết quả (100 + 20) * 3:", (100 + 20) * 3)