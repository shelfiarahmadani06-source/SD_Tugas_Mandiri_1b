class Node:
    def __init__(self, mahasiswa):
        self.mahasiswa = mahasiswa
        self.next = None


class LinkedListMahasiswa:
    def __init__(self):
        self.head = None

    def tambah(self, mahasiswa):
        new_node = Node(mahasiswa)

        if self.head is None:
            self.head = new_node
            return

        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def cari(self, nim):
        current = self.head

        while current is not None:
            if current.mahasiswa.nim == nim:
                return current.mahasiswa

            current = current.next

        return None

    def hapus(self, nim):
        current = self.head
        previous = None

        while current is not None:

            if current.mahasiswa.nim == nim:

                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                return current.mahasiswa

            previous = current
            current = current.next

        return None

    def tampilkan(self):
        data = []
        current = self.head

        while current is not None:
            data.append(current.mahasiswa)
            current = current.next

        return data

    def is_empty(self):
        return self.head is None

    def size(self):
        jumlah = 0
        current = self.head

        while current is not None:
            jumlah += 1
            current = current.next

        return jumlah