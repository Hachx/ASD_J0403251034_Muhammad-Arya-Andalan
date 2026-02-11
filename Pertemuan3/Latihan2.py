class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = self.head
            return
        
        temp = self.head
        while temp.next != self.head:
            temp = temp.next
        temp.next = new_node
        new_node.next = self.head

    def search(self, key):
        # Skenario 3: List Kosong
        if not self.head:
            print("Circular Linked List kosong. Tidak ada elemen yang bisa dicari.")
            return

        current = self.head
        found = False
        
        while True:
            if current.data == key:
                found = True
                break
            current = current.next
            if current == self.head:
                break
        
        if found:
            print(f"Elemen {key} ditemukan dalam Circular Linked List.")
        else:
            print(f"Elemen {key} tidak ditemukan dalam Circular Linked List.")

# --- Bagian Input Interaktif ---

cllist = CircularLinkedList()

# 1. Memasukkan elemen
print("Format: Masukkan angka dipisahkan koma (contoh: 3, 7, 12) atau kosongkan jika ingin list kosong.")
input_elemen = input("Masukkan elemen ke dalam Circular Linked List: ")

# Logika untuk menangani input string menjadi list angka
if input_elemen.strip():
    # Memisahkan string berdasarkan koma dan mengubahnya jadi integer
    elemen_list = [int(x.strip()) for x in input_elemen.split(',')]
    for el in elemen_list:
        cllist.append(el)
else:
    elemen_list = []

# 2. Mencari elemen
input_cari = input("Masukkan elemen yang ingin dicari: ")

if input_cari.strip():
    target = int(input_cari)
    cllist.search(target)
else:
    print("Input pencarian tidak valid.")