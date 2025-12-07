# 🚗 TÍNH CHI PHÍ CHUYẾN ĐI — PYTHON TERMINAL APP

Chương trình giúp người dùng tính toán lượng nhiên liệu tiêu thụ và tổng chi phí cho một chuyến đi dựa trên:

- Quãng đường (km)
- Mức tiêu hao nhiên liệu (lít / 100km)
- Giá nhiên liệu (VND / lít)

Ứng dụng chạy trong terminal, hỗ trợ nhập liệu an toàn và tính toán nhiều lần.

---

## 🧩 TÍNH NĂNG

✔ Nhập dữ liệu từ người dùng:

- Quãng đường (km)
- Mức tiêu hao (lít/100km)
- Giá nhiên liệu (VND/lít)

✔ Kiểm tra lỗi đầu vào:

- Không cho phép nhập số âm
- Xử lý lỗi nhập sai kiểu dữ liệu (vd: nhập chữ → báo sai)

✔ Tính toán:

- Nhiên liệu cần dùng = (quãng đường / 100) × tiêu hao
- Tổng chi phí = nhiên liệu cần × giá nhiên liệu

✔ Hiển thị kết quả rõ ràng

✔ Hỗ trợ tính tiếp nhiều lần (vòng lặp)

---

## 📌 CẤU TRÚC HÀM CHÍNH

### `nhap_so_thuc(thongbao)`

- Nhập số thực hợp lệ từ người dùng
- Dùng `try - except` để bắt lỗi kiểu dữ liệu
- Không chấp nhận số âm
- Trả về giá trị hợp lệ

### `tinh_chi_phi()`

- Gọi hàm nhập dữ liệu
- Tính nhiên liệu & chi phí
- In kết quả ra màn hình

### Vòng lặp chính

Cho phép người dùng tính toán nhiều lượt đến khi nhập `n`.

---

## ▶ CÁCH CHẠY CHƯƠNG TRÌNH

1. Mở thư mục chứa file `.py`
2. Chạy lệnh:

```bash
python ten_file.py
```
