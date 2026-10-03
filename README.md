# Tugas Mandiri 1a - Struktur Data dan Kompleksitas

## Deskripsi

Program ini merupakan implementasi sederhana sistem akademik untuk mengelola data mahasiswa.

Program dibuat sebagai bagian dari Tugas Mandiri 1a pada mata kuliah yang membahas struktur data dan kompleksitas algoritma.

Studi kasus program adalah sistem akademik yang membutuhkan penyimpanan data mahasiswa, penambahan dan penghapusan data, fitur Undo, proses antrean, serta pencarian data berdasarkan NIM.

## Struktur Data yang Digunakan

Program menggunakan beberapa struktur data sebagai berikut:

1. Array
   - Digunakan untuk menyimpan data mahasiswa secara berurutan.
   - Implementasi terdapat pada `structures/array_structure.py`.

2. Linked List
   - Digunakan sebagai implementasi dan pembanding struktur data.
   - Implementasi terdapat pada `structures/linked_list.py`.

3. Stack
   - Digunakan untuk fitur Undo aktivitas.
   - Menggunakan prinsip LIFO (Last In, First Out).
   - Implementasi terdapat pada `structures/stack_undo.py`.

4. Queue
   - Digunakan untuk proses antrean mahasiswa.
   - Menggunakan prinsip FIFO (First In, First Out).
   - Implementasi terdapat pada `structures/queue_processing.py`.

5. Dictionary
   - Digunakan untuk pencarian data mahasiswa berdasarkan NIM sebagai key.
   - Digunakan pada program utama `main.py`.

## Fitur Program

Program memiliki beberapa fitur utama:

1. Tambah data mahasiswa
2. Tampilkan data mahasiswa
3. Cari mahasiswa berdasarkan NIM
4. Hapus data mahasiswa
5. Undo aktivitas terakhir
6. Tambah mahasiswa ke antrean
7. Proses antrean
8. Keluar dari program

## Struktur Folder

```text
tugas_mandiri_1a/
│
├── structures/
│   ├── __init__.py
│   ├── array_structure.py
│   ├── linked_list.py
│   ├── queue_processing.py
│   └── stack_undo.py
│
├── tests/
│   ├── __init__.py
│   ├── test_array_structure.py
│   ├── test_linked_list.py
│   ├── test_queue_processing.py
│   └── test_stack_undo.py
│
├── main.py
├── models.py
└── README.md