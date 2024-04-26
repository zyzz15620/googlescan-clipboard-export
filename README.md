## Vấn đề và cách tiếp cận
Việc nhập tay thủ công từ phiếu phỏng vấn vào excel là công việc tốn nhiều tài nguyên. Do đó hướng giải quyết là sẽ kết hợp Google Lens trên điện thoại và phầm mềm tự viết:
1. Phần mềm được viết bằng python, sử dụng Tkinter để dựng GUI và một số phép toán cơ bản
2. Phần mềm sẽ quét Clipboard, và hiển thị dữ liệu đã scan trên GUI để kiểm tra bằng mắt trước khi chấp nhận.
3. Dựa vào dữ liệu thô đang hiển thị. Phần mềm cũng sẽ kiểm tra lại format dữ liệu, tính toán Bodyfat, tuổi, Vo2max, beep mét.
4. Cuối cùng là xuất ra .txt để thuận tiện cho vào SQL database.

## Hướng dẫn
1. Sử dụng phiếu khảo sát mẫu để scan, khi scan thì scan một nửa mặt giấy.
2. Chọn gửi đến Clipboard máy tính.
3. Khởi động phần mềm
4. Điền số dòng của phiếu khảo sát vào phần mềm. Số dòng giúp phần mềm phân biệt được dữ liệu của môn gì (ví dụ Boxing và xe đạp sẽ có những chỉ số khác nhau).
5. Chọn Quét.
6. Dữ liệu sẽ hiện thị trên giao diện, kiểm tra lại trước khi chọn Chấp nhận.
