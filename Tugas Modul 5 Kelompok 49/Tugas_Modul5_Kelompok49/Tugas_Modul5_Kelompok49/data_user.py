class data :
    def __init__ (self,email,password):
        self.email = email
        self.password = password
        self.data = {
            "aldikelompok49@gmail.com" : {
                "email"     : "aldikelompok49@gmail.com",
                "password"  : "12345",
                "role"      : "superadmin"
            },

        }
        self.history = {
            "aldikelompok49@gmail.com":{
                "peminjaman_buku":{"Fisika Dasar","Dasar Komputer dan Pemrograman"},
                "tanggal_peminjaman" : "10-04-2020"
                },
            }

