class main:
    def __init__ (self, nama, email, HP):
        self.nama = nama
        self.email = email
        self.HP = HP
        self.logam = ["Emas","Logam"]
        self.harga = [732600,216044]

    def welcome (self):
        print(f"Selamat datang, {self.nama} ! Selamat bertransaksi di Mesin Toko Emas Otomatis Kelompok 49!")
        print("Mesin ini akan melakukan bunga harga sebagai berikut:")
        print("Penjualan\t:5%")
        print("Pembelian\t:10%")

    def pembelian_fitur (self):
        print("Masukkan jenis logam yang ingin anda beli")
        count = 1
        for x in self.logam :
            print(count,".",x)
            count = count + 1

    def penjualan_fitur (self):
        print("Masukkan jenis logam yang ingin anda jual")
        count = 1
        for x in self.logam :
            print(count,".",x)
            count = count + 1

    def about_fitur (self):
        print("Berikut adalah Value Logam pada hari ini (per gram):")
        count = 1
        for x in self.logam :
            print(count,".",x,"\t: Rp ",self.harga[count - 1])
            count = count + 1

    def pembelian_transaksi (self,angka1,angka2):
        biaya = self.harga[angka1 - 1] * angka2 * 105 / 100
        print(f"Anda ingin membeli logam {self.logam[angka1-1]} dengan harga {biaya}")
        print("----------------------------------------------------------------")
        print("Lanjutkan Pembelian?")
        print("1.Ya")
        print("2.Tidak")

    def penjualan_transaksi (self,angka1,angka2):
        biaya = self.harga[angka1 - 1] * angka2 * 90 / 100
        print(f"Anda ingin menjual logam {self.logam[angka1-1]} dengan harga {biaya}")
        print("----------------------------------------------------------------")
        print("Lanjutkan Pembelian?")
        print("1.Ya")
        print("2.Tidak")
