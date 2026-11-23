import os


def cls():
    os.system ("cls" if os.name == "nt" else "clear")


# latihan return
cls()

print("====== KASIR TOKO =======\n")

daftar_barang = {
    "buku": 5000,
    "pensil": 2000,
    "penghapus": 1500
}

def total_harga(harga, jumlah):
    return harga * jumlah

total_buku = total_harga(daftar_barang["buku"], 2)
total_pensil = total_harga(daftar_barang["pensil"], 3)
total_penghapus = total_harga(daftar_barang["penghapus"], 1) 

total_belanjaan = total_buku + total_pensil +total_penghapus

print(f"{"Total buku":<20}: Rp {total_buku}")
print(f"{"Total pensil":<20}: Rp {total_pensil}")
print(f"{"Total penghapus":<20}: Rp {total_penghapus}")
print(f"{"Total belanjaan":<20}: Rp {total_belanjaan}")


data = ["apel", "jeruk", "apel", "mangga"]

print(f"list  : {[x.upper() for x in data]}")               # kurung siku: list, urutan dan duplikat tetap
print(f"set   : {sorted({len(x) for x in data})}")           # kurawal: set, duplikat hilang (5 cuma muncul sekali)
print(f"dict  : {({x: len(x) for x in data})}")  


