class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    def print_list(self):
        if not self.head:
            print("kosong")
            return
        temp = self.head
        output = []
        while temp:
            output.append(str(temp.data))
            temp = temp.next
        print(" -> ".join(output) + " -> null")

    # Metode untuk menggabungkan dua list
    def merge(self, other_list):
        # Jika list pertama kosong, maka hasilnya adalah list kedua
        if not self.head:
            self.head = other_list.head
            return
        
        # Jika list kedua kosong, tidak perlu melakukan apa-apa
        if not other_list.head:
            return

        # Cari node terakhir dari list pertama
        last = self.head
        while last.next:
            last = last.next
        
        # Sambungkan node terakhir list pertama ke head list kedua
        last.next = other_list.head

# --- Bagian Input & Simulasi ---

def get_input_list(prompt):
    user_input = input(prompt)
    llist = LinkedList()
    if user_input.strip() and user_input.lower() != "(tidak ada elemen)":
        elements = [int(x.strip()) for x in user_input.split(',')]
        for el in elements:
            llist.append(el)
    return llist

# Input untuk Linked List 1 & 2
list1 = get_input_list("Masukkan elemen untuk Linked List 1: ")
list2 = get_input_list("Masukkan elemen untuk Linked List 2: ")

# Tampilkan list sebelum digabung
print("Linked List 1:", end=" ")
list1.print_list()
print("Linked List 2:", end=" ")
list2.print_list()

# Proses Penggabungan
list1.merge(list2)

# Tampilkan hasil akhir
print("Linked List setelah digabungkan:", end=" ")
list1.print_list()