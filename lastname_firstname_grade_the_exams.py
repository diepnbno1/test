import numpy as np
import pandas as pd

# Task 1:
def task1():
    #Tạo vòng lặp while để khi nhập sai sẽ tự động được mời nhập lại
    while True:
        #try/except để không gặp lỗi nếu gõ sai tên file
        try:
            filename = input("Enter a class file to grade (i.e. class1 for class1.txt): ")
            with open(filename) as readfile:
                file1 = readfile.readlines()
            print("Successfully opened ",filename)
            return file1,filename
            break
        except:
            print("File cannot be found.")

# Task 2:
def task2(file):
    print("\n**** ANALYZING ****\n")
    # count là số lượng học sinh invalid
    count = 0
    for student in file:
        st1 = student.split(",")
        #Xác định xem dòng nào không đủ 26 giá trị
        if len(st1) != 26:
            print("Invalid line of data: does not contain exactly 26 values:")
            print(student)
            count += 1
        #Xác định xem ID học sinh nào chưa hợp lý
        elif len(st1[0]) != 9 or st1[0][0] != "N" or st1[0][1:].isnumeric() == False:
            print("Invalid line of data: N# is invalid")
            print(student)
            count += 1
    if count == 0:
        print("No errors found!")
    print("\n**** REPORT ****\n")
    print("Total valid lines of data: ",len(file) - count)
    print("Total invalid lines of data: ", count)

# Task3:
def task3(file,asw):
    print("\n**** ANALYZING ****\n")
    # Xác định số lượng học sinh invalid
    count = 0
    student_valid = []
    for student in file:
        st1 = student.split(",")
        #Xác định các dòng invalid do không đủ 26 giá trị
        if len(st1) != 26:
            print("Invalid line of data: does not contain exactly 26 values:")
            print(student)
            count += 1
        #Xác định các học sinh có ID invalid
        elif len(st1[0]) != 9 or st1[0][0] != "N" or st1[0][1:].isnumeric() == False:
            print("Invalid line of data: N# is invalid")
            print(student)
            count += 1
        #Đưa những học sinh valid vào một nhóm
        else:
            student_valid.append(student)
    if count == 0:
        print("No errors found!")
    print("\n**** REPORT ****\n")
    print("Total valid lines of data: ",len(file) - count, "\n")
    print("Total invalid lines of data: ", count, "\n")

    #Bỏ dấu phẩy trong đáp án và đưa về dạng list
    asw = asw.split(",")
    student_diem_total = []
    #Chạy vòng lặp với từng học sinh valid
    for student in student_valid:
        #Loại bỏ khoảng trắng 2 phía ngoài cùng bên phải và bên trái dòng, bỏ dấu cách, chuyển sang dạng list
        student_baithi = student.strip().split(",")
        #Thêm ID học sinh vào trước
        student_diem = [student_baithi[0]]
        #Vòng lặp chạy với từng câu trong bài thi
        for i in range(25):
            #So sánh từng câu trong bài thi học sinh với đáp án để chấm điểm từng câu
            if asw[i] == student_baithi[i+1]:
                student_diem.append(4)
            elif student_baithi[i+1] == "":
                student_diem.append(0)
            else:
                student_diem.append(-1)
        #Thêm kết quả điểm số từng học sinh vào student_diem_total
        student_diem_total.append(student_diem)

    #Tạo tiêu đề cột
    colum = ["ID", "Cau1", "Cau2", "Cau3", "Cau4","Cau5", "Cau6", "Cau7", "Cau8","Cau9", "Cau10", "Cau11", "Cau12","Cau13", "Cau14", "Cau15", "Cau15","Cau17", "Cau18", "Cau19", "Cau20","Cau21", "Cau22", "Cau23", "Cau24","Cau25"]
    #Tạo dataframe
    df = pd.DataFrame(data = student_diem_total, columns = colum)
    #Cộng tổng cho cả hàng
    df["Total_score"] = df.sum(axis = 1)
    #Xuất ra các điểm cần thiết
    print("Mean (average) score: ",round(df["Total_score"].mean(),2) ,"\n")
    print("Highest score: ",df["Total_score"].max(),"\n")
    print("Lowest score: ",df["Total_score"].min(), "\n")
    print("Range of scores: ",df["Total_score"].max() - df["Total_score"].min(), "\n")
    print("Median score: ", df["Total_score"].median(),"\n")
    #Trả về dataframe
    return df[["ID","Total_score"]]

# Task4:
def task4(fname,df):
    #Đặt tên file mới theo cấu trúc yêu cầu
    fname = fname[0:6] + "_grades.txt"
    #Mở file mới để ghi vào
    with open(fname, "w") as writefile:
        for _ in range(len(df.index)):
            writefile.write("{},{}\n".format(df.iloc[_,0],df.iloc[_,1]))

# Phần chính
while True:
    # Đưa đáp án vào
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    # Xuất ra dữ liệu, tên file đã gọi
    fileclass,filename = task1()
    # Xuất ra dataframe kết quả
    df = task3(fileclass,answer_key)
    # Lưu kết quả vào file mới
    task4(filename, df)
    print("================================ RESTART ================================\n")
