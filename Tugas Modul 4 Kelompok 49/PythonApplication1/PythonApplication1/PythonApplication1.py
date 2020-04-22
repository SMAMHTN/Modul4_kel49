import Ext_Source_Code

def creator () :
    print("Program ini dibuat oleh kelompok 49 Shift 2")
    print("Aldi Mulyawan 21120119120026")
    print("Mochamad Pratama Wibawa 21120119130062")

print("Selamat datang di Mesin Toko Emas Otomatis Kelompok 49!")
nama = str(input("Masukkan Nama anda\t:"))
email = str(input("Masukkan Email Anda\t:"))
HP = str(input("Masukkan No HP anda\t:"))

call = Ext_Source_Code.main(nama,email,HP)
call.welcome()
print("Semua Value dihitung Sejak 16 April 2020")
print("----------------------------------------------------------------")
choice = 1
while (choice == 1):
    print("Pilih transaksi yang akan anda lakukan!")
    print("1.Penjualan")
    print("2.Pembelian")
    print("3.Value Logam Hari ini ")
    print("4.About")
    a = int(input("Masukkan pilihan anda : "))
    print("----------------------------------------------------------------")

    if (a == 1):
        call.penjualan_fitur()
        b = int(input("Masukkan nomor logam yang ingin anda beli\t\t: "))
        c = int(input("Masukkan berat logam yang akan anda beli (Dalam Gram)\t:"))
        print("Masukkan Logam ke kotak dibawah.....")
        print("Loading......")
        print("Scan berhasil,Data benar.")
        call.penjualan_transaksi(b, c)
        e = int(input("Masukkan Jawaban anda : "))
        if (e == 1):
            print("Terima Kasih telah bertransaksi menggunakan Mesin Toko Emas Otomatis Kelompok 49!")
            print("Detail transaksi akan dikirimkan ke email ",email," serta no HP ",HP)
        print("----------------------------------------------------------------")

    elif (a == 2):
        call.pembelian_fitur()
        b = int(input("Masukkan nomor logam yang ingin anda beli\t\t: "))
        c = int(input("Masukkan berat logam yang akan anda beli (Dalam Gram)\t:"))
        call.pembelian_transaksi(b, c)
        e = int(input("Masukkan Jawaban anda : "))
        if (e == 1):
            print("Terima Kasih telah bertransaksi menggunakan Mesin Toko Emas Otomatis Kelompok 49!")
            print("Detail transaksi akan dikirimkan ke email ",email," serta no HP ",HP)
        print("----------------------------------------------------------------")
    elif (a == 3):
        call.about_fitur()
    elif (a == 4):
        creator()
    else:
        print("Mohon masukkan angka yang sesuai!")

    print("Apakah anda ingin melakukan transaksi lainnya?")
    print("1.Ya")
    print("2.Tidak")
    choice = int(input("Masukkan pilihan anda : "))
    print("----------------------------------------------------------------")

print("Terima Kasih telah menggunakan Mesin Toko Emas Otomatis Kelompok 49!")