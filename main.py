from models import Mahasiswa
from structures.array_structure import ArrayMahasiswa
from structures.stack_undo import StackUndo
from structures.queue_processing import QueueProcessing


# Struktur data yang digunakan
array_mahasiswa = ArrayMahasiswa()
data_mahasiswa = {}
stack_undo = StackUndo()
queue_processing = QueueProcessing()


def tambah_mahasiswa():
    print("\n=== TAMBAH DATA MAHASISWA ===")

    nim = input("Masukkan NIM: ")
    nama = input("Masukkan Nama: ")
    jurusan = input("Masukkan Jurusan: ")

    mahasiswa = Mahasiswa(nim, nama, jurusan)

    # Array digunakan untuk penyimpanan data secara berurutan
    array_mahasiswa.tambah(mahasiswa)

    # Dictionary digunakan untuk pencarian berdasarkan NIM
    data_mahasiswa[nim] = mahasiswa

    # Stack digunakan untuk menyimpan aktivitas Undo
    stack_undo.push({
        "type": "add",
        "mahasiswa": mahasiswa
    })

    print("Data mahasiswa berhasil ditambahkan.")


def tampilkan_mahasiswa():
    print("\n=== DAFTAR MAHASISWA ===")

    if array_mahasiswa.is_empty():
        print("Belum ada data mahasiswa.")
        return

    for mahasiswa in array_mahasiswa.tampilkan():
        print(mahasiswa.tampilkan_data())


def cari_mahasiswa():
    print("\n=== CARI MAHASISWA BERDASARKAN NIM ===")

    nim = input("Masukkan NIM yang dicari: ")

    # Dictionary digunakan untuk pencarian berdasarkan key
    mahasiswa = data_mahasiswa.get(nim)

    if mahasiswa:
        print("Data ditemukan:")
        print(mahasiswa.tampilkan_data())
    else:
        print("Data mahasiswa tidak ditemukan.")


def hapus_mahasiswa():
    print("\n=== HAPUS DATA MAHASISWA ===")

    nim = input("Masukkan NIM yang akan dihapus: ")

    mahasiswa = data_mahasiswa.get(nim)

    if mahasiswa:
        # Hapus dari Array
        array_mahasiswa.hapus(nim)

        # Hapus dari Dictionary
        del data_mahasiswa[nim]

        # Simpan aktivitas untuk Undo
        stack_undo.push({
            "type": "delete",
            "mahasiswa": mahasiswa
        })

        print("Data mahasiswa berhasil dihapus.")
    else:
        print("Data mahasiswa tidak ditemukan.")


def undo_aktivitas():
    print("\n=== UNDO AKTIVITAS ===")

    aktivitas = stack_undo.pop()

    if aktivitas is None:
        print("Tidak ada aktivitas yang dapat di-undo.")
        return

    mahasiswa = aktivitas["mahasiswa"]

    if aktivitas["type"] == "add":

        # Batalkan penambahan
        array_mahasiswa.hapus(mahasiswa.nim)

        if mahasiswa.nim in data_mahasiswa:
            del data_mahasiswa[mahasiswa.nim]

        print(
            f"Penambahan mahasiswa {mahasiswa.nim} "
            "berhasil dibatalkan."
        )

    elif aktivitas["type"] == "delete":

        # Batalkan penghapusan
        array_mahasiswa.tambah(mahasiswa)
        data_mahasiswa[mahasiswa.nim] = mahasiswa

        print(
            f"Penghapusan mahasiswa {mahasiswa.nim} "
            "berhasil dibatalkan."
        )


def tambah_antrean():
    print("\n=== TAMBAH ANTREAN ===")

    nim = input("Masukkan NIM mahasiswa: ")

    mahasiswa = data_mahasiswa.get(nim)

    if mahasiswa:
        queue_processing.enqueue(mahasiswa)

        print("Mahasiswa berhasil masuk ke antrean.")
    else:
        print("Mahasiswa tidak ditemukan.")


def proses_antrean():
    print("\n=== PROSES ANTREAN ===")

    mahasiswa = queue_processing.dequeue()

    if mahasiswa:
        print("Mahasiswa yang diproses:")
        print(mahasiswa.tampilkan_data())
    else:
        print("Antrean kosong.")


def tampilkan_menu():
    print("\n" + "=" * 45)
    print("       SISTEM AKADEMIK SEDERHANA")
    print("=" * 45)
    print("1. Tambah data mahasiswa")
    print("2. Tampilkan data mahasiswa")
    print("3. Cari mahasiswa berdasarkan NIM")
    print("4. Hapus data mahasiswa")
    print("5. Undo aktivitas terakhir")
    print("6. Tambah mahasiswa ke antrean")
    print("7. Proses antrean")
    print("8. Keluar")
    print("=" * 45)


def main():
    while True:
        tampilkan_menu()

        pilihan = input("Pilih menu (1-8): ")

        if pilihan == "1":
            tambah_mahasiswa()

        elif pilihan == "2":
            tampilkan_mahasiswa()

        elif pilihan == "3":
            cari_mahasiswa()

        elif pilihan == "4":
            hapus_mahasiswa()

        elif pilihan == "5":
            undo_aktivitas()

        elif pilihan == "6":
            tambah_antrean()

        elif pilihan == "7":
            proses_antrean()

        elif pilihan == "8":
            print("Program selesai. Terima kasih.")
            break

        else:
            print("Pilihan tidak valid. Silakan pilih 1-8.")


if __name__ == "__main__":
    main()