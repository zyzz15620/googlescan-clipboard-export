## Tổng quan
Phần mềm được viết để tiếp nhận dữ liệu từ Google Lens trên điện thoại và xuất ra file txt, trước khi đưa vào SQL database. Phần mềm được viết để giải quyết vấn đề nhập thủ công từ phiếu khảo sát vào excel.

## Tính Năng
- Hứng dữ liệu từ clipboard và hiển thị dữ liệu đã quét lên trên giao diện phần mềm để kiểm tra bằng mắt trước khi submit.
- Dựa vào chỉ số thô để tính thêm các chỉ số: Bodayfat, tuổi, Vo2max, Beep test (mét).
- Xuất dữ liệu ra file txt theo cấu trúc phù hợp để import vào mySQL database.

## Cách Sử Dụng
1. Chọn phiếu khảo sát để scan (mỗi môn thể thao sẽ có phiếu khảo sát khác nhau, dự án không kèm phiếu khảo sát)
2. Dùng Google Lens trên điện thoại để scan. Khi scan thì chỉ scan một nửa mặt phải của phiếu khảo sát.
3. Chọn gửi đến Clipboard máy tính.
4. Khởi động phần mềm
5. Điền số dòng của phiếu khảo sát vào phần mềm. Số dòng giúp phần mềm phân biệt được dữ liệu của môn gì (ví dụ Boxing và xe đạp sẽ có số lượng chỉ số khác nhau).
6. Chọn Quét.
7. Dữ liệu sẽ hiện thị trên giao diện, kiểm tra lại trước khi chọn Chấp nhận.

## Yêu Cầu
- Python 3.x
- Các thư viện cần thiết: Tkinter, pyperclip
