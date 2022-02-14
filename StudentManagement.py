class SinhVien(object):
    def __init__(self,ID, Hoten,Lop,Khoa, NamSinh):
        #Gộp vừa tạo vừa gán
        self.ID = ID
        self.Hoten = Hoten
        self.Lop = Lop
        self.Khoa = Khoa
        self.NamSinh = NamSinh
    def getHoten(self):
        return self.Hoten
    def isSinhVienCaoDang(self):
        return False
    def isSinhVienDaiHoc(self):
        return False
class SinhVienDaiHoc(SinhVien):
    def __init__(self,ID, Hoten,Lop,Khoa, NamSinh,TuChon):
        self.TuChon = TuChon
        SinhVien.__init__(self,ID, Hoten,Lop,Khoa, NamSinh)
    def isSinhVienDaiHoc(self):
        return True
class Employee(Person):
    def __init__(self, name, idnumber,salary,post):
        self.salary = salary
        self.post = post
        #ủy quyền pt kt của lớp cha
        Person.__init__(self, name, idnumber)
if __name__ == "__main__":
    #= Employee('Rahuld',886012,200000,'Intern')
    #truyền vô biến đầu vào và gán cho từng
    #thuộc tính của lớp
    #display()
    sv = SinhVien('123','Bao','CTK28','CNTT',1992)
    print(sv.getHoten(),sv.isSinhVienDaiHoc())

    sv = SinhVienDaiHoc('124','Binh','CTK27','CNTT',1990,'LT PYTHON')
    print(sv.getHoten(),sv.isSinhVienDaiHoc())