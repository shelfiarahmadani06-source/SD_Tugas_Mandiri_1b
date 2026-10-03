class ArrayMahasiswa:
    def __init__(self):
        self.data = []

    def tambah(self, mahasiswa):
        self.data.append(mahasiswa)

    def tampilkan(self):
        return self.data

    def cari(self, nim):
        for mahasiswa in self.data:
            if mahasiswa.nim == nim:
                return mahasiswa
        return None

    def hapus(self, nim):
        for i, mahasiswa in enumerate(self.data):
            if mahasiswa.nim == nim:
                return self.data.pop(i)
        return None

    def is_empty(self):
        return len(self.data) == 0

    def size(self):
        return len(self.data)