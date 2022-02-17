class SinhVien():
    stt = ""
    name = ""
    ns = ""
    lop = ""
    khoa = ""
    def __init__(self,stt = "",name = "", ns = "",lop="" ,khoa = ""):
        self.stt = str(stt)
        self.name = str(name)
        self.ns = str(ns)
        self.lop = str(lop)
        self.khoa = str(khoa)
    def stt1(self):
        print("ID =", self.stt)
    def hvt1(self):
        print("Họ Và Tên Của Sinh Viên là:", self.name)
    def ns1(self):
        print("Năm Sinh Của Sinh Viên=",self.ns)
    def lop1(self):
        print("Lớp Học Của Sinh Viên:",self.lop)
    def khoa1(self):
        print("Khoá Của Sinh Viên",self.khoa)

databasee = {
    "1" : ("Nguyễn Minh Quang 09/02/2007 9A10 2021-2022"),
    "2" : ("Nguyễn Quang Vinh 19/11/2008 8A4 2021-2022")
}


print("1.Thêm Sinh Viên")
print("2.Xoá Sinh Viên")
print("3.Xem Tất Cả Sinh Viên")
print("4.Tìm Sinh Viên")
print("5.Thoát Chương Trình")
mot = 1
hai = 2
ba = 3
bon = 4
nam = 5
luachon = int(input())

while luachon != 0:
    try:
        if luachon == mot:
            class sv(SinhVien):
                pass
            stt = input("Số Thứ Tự: ")
            hovaten = input("Họ Và Tên Sinh Viên: ")
            ns = input("Năm Sinh: ")
            lop = input("Lớp: ")
            khoa = input("Khoá: ")
            mean = "{} ,{} ,{} ,{}".format(hovaten,ns,lop,khoa)
            databasee[stt] = mean
            sinhvienhoc = sv(stt,hovaten,ns,lop,khoa)
            sinhvienhoc.stt1()
            sinhvienhoc.hvt1()
            sinhvienhoc.ns1()
            sinhvienhoc.lop1()
            sinhvienhoc.khoa1()
            print("Đã Thêm Sinh Viên")
        if luachon == hai:
            stt = input('ID: ')
            if stt in databasee:
                del databasee[stt]
                print("Sinh Viên [ %s ] Đã Bị Xoá" % stt)
            else:
                print('Không Tìm Thấy Sinh Viên: [ %s ]' % stt)
        if luachon == ba:
            def view_all():
                for stt, mean in databasee.items():
                    print('[ %s: %s ]' % (stt, mean))
            view_all()
        if luachon == bon:
            def find():
                stt = input("Sinh Viên Muốn Tìm: ")
                if stt in databasee:
                    print("Đã Tìm Thấy Sinh Viên: [ %s: %s ]" % (stt, databasee[stt]))
                else:
                    print('Không Tìm Thấy Sinh Viên: [ %s ]' % stt)
            find()
        if luachon == nam:
            print("Hẹn Gặp Lại")
            break
        else:
            luachon = int(input("Bạn Muốn làm Gì? "))
    except:
        print("Có Lỗi Vui Lòng Thử Lại")