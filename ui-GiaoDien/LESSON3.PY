# class Xe:
#     def __init__(self, _hangxe = "Chua biet", _mauxe = "Chua biet", _giatien = "Chua biet"):
#         self.hangxe = _hangxe
#         self.mauxe = _mauxe
#         self.giatien = _giatien
#     #ham in ra thong tin
#     def show(self):
#         print("Hang xe:", self.hangxe)
#         print("Mau xe:", self.mauxe)
#         print("Gia tien:", self.giatien)
# #chua nhap tt
# # xe1 = Xe()
# # xe1.show()
# # da nhap thong tin dau vao
# xe2 = Xe("Vinfast", "trang", 1000)
# xe2.show()
class PhanSo:
    def __init__(self, _tuso = 0, _mauso=1):
        self.mauso=_mauso
        self.tuso = _tuso
    def _input(self):
        l = input().split()
        self.tuso =int(l[0])
        self.mauso = int(l[1])
    def _output(self):
        print(str(self.tuso) + "/" + str(self.mauso))
    def xuatTuso(self):
        print(self.tuso)
    def xuatMauSo(self):
        print(self.mauso)
    def xuatPSngichdao(self):
        print(str(self.mauso) + "/" + str(self.tuso))
    def psrutgon(self):
        tumoi, maumoi = self.tuso, self.mauso
        mauchung = 2
        while tumoi >= mauchung and maumoi >= mauchung:
            if tumoi%mauchung == 0 and maumoi%mauchung == 0:
                tumoi /= mauchung
                maumoi /= mauchung
            mauchung += 1
        return PhanSo(int(tumoi), int(maumoi))
    def TongVoiPSnghicdao(self):
        a = self.tuso
        b = self.mauso
        tusomoi = a*a + b*b
        mausomoi = a*b

        PhanSo(tusomoi, mausomoi).psrutgon()._output()
ps = PhanSo()
ps._input()
ps._output()
ps.xuatTuso()
ps.xuatMauSo()
ps.xuatPSngichdao()
ps.psrutgon()._output()
ps.TongVoiPSnghicdao()