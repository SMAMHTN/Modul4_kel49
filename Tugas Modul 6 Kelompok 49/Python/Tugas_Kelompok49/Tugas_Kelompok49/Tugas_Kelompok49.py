class Mahasiswa:
    def __init__ (self): 
        self.a = ""
        self.b = ""
        self.c = ""
        self.d = ""
        self.e = ""
        self.f = ""


    def geta (self):         
        return self.a
    def seta (self,a):      
        self.a = a

    def getb (self):
        return self.b
    def setb (self,b):
        self.b = b

    def getc (self):
        return self.c
    def setc (self,c):
        self.c = c

    def getd (self):         
        return self.d
    def setd (self,d):      
        self.d = d

    def gete (self):
        return self.e
    def sete (self,e):
        self.e = e

    def getf (self):
        return self.f
    def setf (self,f):
        self.f = f

    def getg (self):
        return self.g
    def setg (self,g):
        self.g = g






#Disini Dimulai Source Code utamanya
c = input("Masukkan Nomor Kelompok anda:")
print('-' * 40)
print("Masukkan Data anggota pertama:")
a = input("Nama\t\t:")
b = input("NIM\t\t:")
f = input("NIM\t\t:")
print("Masukkan Data anggota kedua:")
d = input("Nama\t\t:")
e = input("NIM\t\t:")
g = input("NIM\t\t:")

call = Mahasiswa()
call.seta(a)
call.setb(b)
call.setc(c)
call.setd(d)
call.sete(e)
call.setf(f)
call.setg(g)

outa = call.geta()
outb = call.getb()
outc = call.getc()
outd = call.getd()
oute = call.gete()
outf = call.getf()
outg = call.getg()
    
print()
print(f"Data Praktikan Kelompok {outc}".center(40,"-"))
print("Anggota 1:")
print("Nama:", outa)
print("NIM:", outb)
print("Asal:", outf)
print('-' * 40)
print("Anggota 2:")
print("Nama:", outd)
print("NIM:", oute)
print("Asal:", outg)
print('-' * 40)

print()
print(f"Nama anggota pertama adalah {outa} dengan NIM {outb} dari {outf}")
print(f"Nama anggota Kedua adalah {outd} dengan NIM {oute} dari {outg}")