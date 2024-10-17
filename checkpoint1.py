# tn:
# 1: d
#2: b
#3: a
#4: b
#5; d
#6: a
#7: b
#8:d
#9: b
#10: b
#thuc hanh:
class HocSinh:
    def __init__(self, _hoten = "chua biet", _diachi = "chua biet", _chieucao = "chua biet", _cannang = "chua biet", _hocluc = "chua biet"):
        self.ten = _hoten
        self.diachi = _diachi
        self.chieucao = _chieucao
        self.cannang = _cannang
        self.hocluc = _hocluc
    def show(self):
        print("Ten hoc sinh:", self.ten)
        print("Dia chi:", self.diachi)
        print("Chieu cao", self.chieucao)
        print("Can nang:", self.cannang)
        print("Hoc luc:", self.hocluc)
    def chuyennha (self, diachinhamoi):
        self.diachi = diachinhamoi
    def khamsuckhoe(self, chieucaomoi, cannangmoi):
        self.chieucao = chieucaomoi
        self.cannang = cannangmoi
print("truoc khi chuyen")
hs1 = HocSinh("Nguyen Van a", "tphcm", 100 , 50 , "gioi")
hs1.show()
#chuyen nha
print("Sau khi chuyen")
hs1.chuyennha("Ha noi")
#suck khoe
hs1.khamsuckhoe(200,80)
hs1.show()
