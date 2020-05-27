# ini adalah kelas utama / super class
class Utama:
    
    def nama(self):
        print('ade arya bimantara')

    def nim(self):
        print('1234567890')

    def gender(self):
        print('laki - laki')

# ini class yang memanggil class utama/super class
class Biodata(Utama):

    def __init__(self):
        super().nama()
        super().nim()
        super().gender()

# eksekusi dari class diatas
Biodata()