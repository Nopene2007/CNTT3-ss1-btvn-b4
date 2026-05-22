# Phan tich va de xuat giai phap
    # input: ma_benh_nhan: str
    # nhiet_do:Nhiệt độ cơ thể (Bắt buộc phải lưu là số thực - Float. Ví dụ: 37.5): float
    # nhip_tim: int
    # output: in ra thông tin bệnh nhân kèm theo xác nhận kiểu dữ liệu của nhiệt độ và nhịp tim

# trien khai code
print("--- KẾT QUẢ CHUẨN HÓA DỮ LIỆU ---")
ma_benh_nhan=input("Nhập mã bệnh nhân: ")
nhiet_do=float(input("Nhiệt độ cơ thể: "))
nhip_tim=int(input("Nhịp tim: "))
print(f"Mã bệnh nhân: {ma_benh_nhan}")
print(f"Nhiệt độ cơ thể: {nhiet_do}")
print(f"=> Kiểu dữ liệu hệ thống ghi nhận: {type(nhiet_do)}")
print(f"Nhịp tim: {nhip_tim} nhịp/ phút")
print(f"=> Kiểu dữ liệu hệ thống ghi nhận: {type(nhip_tim)}")
print("-----------------------")
print("Thông báo: Dữ liệu hợp lệ. Màn hình Monitor đã sẵn sàng kết nối!")