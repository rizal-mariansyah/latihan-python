import os

os.system ("cls" if os.name == "nt" else "clear")


print("========== toko sederhana ==========\n")
print("Daftar produk\n")
print(40*"-","\n")

produk = {"buku": 5000,
          "pensil": 2000,
          "penghapus": 1500,
          "penggaris": 3000
}

for nama,harga in produk.items():
    print(f"{nama:<12}: Rp. {harga}")

print("\n",40*"-",)
    
print( "\njumlah produk: ", len(produk))
  
