# Chương trình tính chi phí chuyến đi

# Hàm nhập số thực (không âm, không lỗi kiểu dữ liệu)
def nhap_so_thuc(thongbao):
    while True: # Lặp đến khi nhập đúng
        try:
            # Hiển thị thông báo yêu cầu người dùng nhập số, sau đó đọc chuỗi họ nhập và chuyển thành số thực 
            value = float(input(thongbao))
            if value < 0: # Kiểm tra giá trị có âm hay không
                print("Giá trị không được âm, vui lòng nhập lại")
            else:
                return value # Nếu hợp lệ trả về giá trị và thoát khỏi hàm
        except ValueError:
            # Bắt lỗi khi người dùng nhập không phải số
            print("Sai kiểu dữ liệu, vui lòng nhập số")

# Hàm chính tính chi phí chuyến đi
def tinh_chi_phi():
    print("=== TÍNH CHI PHÍ CHUYẾN ĐI ===")
    # Nhập dữ liệu từ người dùng
    quang_duong = nhap_so_thuc("Nhập quãng đường(km): ")
    tieu_hao = nhap_so_thuc("Mức tiêu hao nhiên liệu(lít/100km): ")
    gia_nhien_lieu = nhap_so_thuc("Nhập giá nhiên liệu(VND/lít): ")

    # Tính nhiên liệu cần dùng
    nhien_lieu_can = (quang_duong / 100) * tieu_hao
    # Tính tổng chi phí
    tong_chi_phi = nhien_lieu_can * gia_nhien_lieu

    # Hiển thị kết quả
    print("=== KẾT QUẢ ===")
    print("Nhiên liệu cần dùng là: ",nhien_lieu_can, "lít")
    print("Tổng chi phí: ",tong_chi_phi, "VND")

# Vòng lặp cho phép tính nhiều lần
while True:
    tinh_chi_phi() # Gọi hàm tính chi phí

    tiep_tuc = input("Bạn có muốn tính tiếp không? (y/n): ") # Hỏi người dùng có muốn tính tiếp hay không
    if tiep_tuc != 'y': # Nếu không phải y thì thoát vòng lặp
        print("Cảm ơn bạn đã sử dụng chương trình!")
        break