class Mahasiswa:
    def __init__(self, nim, nama, jurusan):
        self.nim = nim
        self.nama = nama
        self.jurusan = jurusan

    def tampilkan_data(self):
        return f"NIM: {self.nim} | Nama: {self.nama} | Jurusan: {self.jurusan}"