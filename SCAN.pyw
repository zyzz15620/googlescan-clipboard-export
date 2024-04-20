import tkinter as tk
import pyperclip
import math
from datetime import datetime
from tkinter import messagebox

BD = [1.1620, 0.063, 1.1631, 0.0632, 1.1422, 0.0544, 1.1620, 0.07, 1.1715, 0.0779, 1.1549, 0.0678, 1.1599, 0.0717, 1.1423, 0.0632, 1.1333, 0.0612, 1.1339, 0.0645] # các hằng số trong công thức tính bodyfat Durnin Formula Specification

def ask_confirmation():
	line_count = count_lines()
	response = messagebox.askyesno("Xác nhận", f"Số dòng hiện tại là {line_count}. Bạn có muốn xác nhận?")
	if response:
		get_input()

def count_lines():
	content = text_widget.get("1.0", tk.END)
	line_count = content.count('\n')
	return line_count

def calculate_bodyfat(sex, age, data):
	pos = 0 # Vị trí trong mảng BD
	compare_age = 19 # Mốc tuổi để tính bodyfat
	
	float_data = [float(i) for i in data]
	sf = sum(float_data)

	if sex == 'F':
		pos += 10
	
	while age > compare_age and compare_age < 50:
		pos += 2
		compare_age += 10
	
	bd = BD[pos] - BD[pos+1]*math.log(sf,10)
	
	fat = 495/bd - 450
	fat = round(fat,2)
	
	return fat

def calculate_beep(beep_level):
	exclusive = [1,3,5,7,9,10,12,14,15] # các level không tăng thêm số shuttle
	lap = 20 # độ dài m mỗi shuttle
	shuttles_per_level = 7 # số shuttle của level đầu tiên

	beep_level = beep_level.split('.')
	level = int(beep_level[0])
	shuttle = int(beep_level[1])

	# tính beep vo2max
	ends = level * 0.4325 + 7.0048
	deci = shuttle / ends
	score = 1 * level * deci
	beep_vo2max = round(3.466*score+12.2,1)

	# tính beep m
	for i in range(level):
		shuttle += shuttles_per_level*(i>0) # không cộng dồn chỉ lần đầu tiên
		if i+1 in exclusive:
			continue
		shuttles_per_level += 1

	beep_m = shuttle * lap
	
	return beep_m,beep_vo2max

def calculate_age(birth_date):
	today = datetime.today()
	record_date = today.strftime("%Y-%m-%d")
	birth_date = datetime.strptime(birth_date, "%d-%m-%Y")
	age = today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))
	birth_date = birth_date.strftime("%Y-%m-%d")
	return age, birth_date, record_date

def calculate_data(data):
	data[0] = data[0].title()
	pos = int(pos_entry.get()) # vị trí của các chỉ số đo Fat%
	birth_date = data[2] # vị trí của ngày sinh trong tờ kiểm tra - 1
	
	start_training = data[3]
	data[3] = start_training[-4:]

	sex = data[1]
	age, birth_date, record_date = calculate_age(birth_date)
	record_date = entry_date.get()
	data[2] = birth_date
	data_fat = data[pos:pos+4]

	fat = calculate_bodyfat(sex, age, data_fat)

	del data[pos:pos+4]
	data.insert(pos, fat)

	beep_level = data[-1] # vị trí chỉ số beep test level
	if beep_level == "":
		beep_m, beep_vo2max = "",""
	else:
		beep_m, beep_vo2max = calculate_beep(beep_level)

	
	data.append(beep_m)
	data.append(beep_vo2max)
	data.append(record_date)

	return data

def get_input():
	file_name = entry_name.get()
	content_var = text_widget.get("1.0", "end-1c")
	content_var = content_var.replace(',','.')
	calculating_var = content_var.split('\n')
	calculated_var = calculate_data(calculating_var)
	calculated_var = [str(i) for i in calculated_var]
	save_content = ','.join(calculated_var)

	with open(f"{file_name}.txt", mode='a', encoding='utf-8') as file:
		file.write(save_content + '\n')

	messagebox.showinfo("Thông báo", f"Dữ liệu đã được lưu vào {file_name}.txt")

def get_clipboard():
	while True:
		clipboard_content = pyperclip.paste()
	
		if clipboard_content:
			cleaned_lines = [line for line in clipboard_content.split('\n') if line.strip()]
			cleaned_text = "\n".join(cleaned_lines)
			lines = cleaned_text.split("\n")

			line_count = len(lines)
			# line_count = cleaned_text.count('\n') + 1
			label_count.config(text=f"Số dòng: {line_count}")
			text_widget.delete("1.0", tk.END)
			text_widget.insert(tk.END, cleaned_text)
			# pyperclip.copy("")
			break

root = tk.Tk()
root.title("Scan siêu cấp vippro")
root.geometry("500x900")
# root.attributes("-fullscreen", True)

# Biến lưu nội dung clipboard
content_var = tk.StringVar()
count_var = tk.StringVar()

# Nút bắt đầu lấy dữ liệu từ clipboard
start_button = tk.Button(root, text="Quét", command=get_clipboard, font=20)
start_button.pack()

label_excel = tk.Label(root, text="Tên file Excel:", font=20)
label_excel.pack()

# Khung nhập tên file excel
entry_name = tk.Entry(root, font = 20)
entry_name.pack()

label_pos = tk.Label(root, text="Số dòng trong mục thông tin cá nhân:", font=20)
label_pos.pack()

# Ô nhập số dòng trong mục thông tin cá nhân
pos_entry = tk.Entry(root, font=20)
pos_entry.pack()

label_date = tk.Label(root, text="Ngày kiểm tra: ", font=20)
label_date.pack()

entry_date = tk.Entry(root, font=20)
entry_date.pack()

label_content = tk.Label(root, text="Nội dung scan:", font=20)
label_content.pack()

# Khung hiểu thị dữ liệu từ clipboard
text_widget = tk.Text(root, wrap=tk.WORD, font=20)
text_widget.pack()

label_count = tk.Label(root, text="Số dòng: 0", font=20)
label_count.pack()


# Nút lưu dữ liệu đang có trên giao diện vào file excel
save_button = tk.Button(root, text="Chấp nhận", font=20, command=ask_confirmation)
save_button.pack()

# Nút để thoát khỏi ứng dụng
quit_button = tk.Button(root, text="Thoát", font=20, command=root.quit)
quit_button.pack(pady=10)

root.mainloop()
