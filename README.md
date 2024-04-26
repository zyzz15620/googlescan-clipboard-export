## Tổng quan
Đây là một phần mềm được viết bằng Python tiếp nhận dữ liệu từ Google Lens trên điện thoại và xuất ra file txt, trước khi đưa vào cơ sở dữ liệu SQL. Phần mềm được viết để giải quyết vấn đề nhập thủ công từ phiếu khảo sát vào excel.

## Tính Năng
- Quét dữ liệu từ Clipboard và hiển thị dữ liệu đã quét lên trên giao diện phần mềm.
- Dựa vào chỉ số thô để tính ra các chỉ số: Bodayfat, tuổi, Vo2max, Beep test (mét).
- Đảm bảo dữ liệu không bị thiếu, và đúng cấu trúc trước khi xuất ra txt.

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
