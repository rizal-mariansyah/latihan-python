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

total_harga = 0

for nama,harga in produk.items():
    print(f"{nama:<12}: Rp. {harga}")
    total_harga += harga 

# koding utama
while True :
    
    nama_produk = input("\nmasukan nama produk: ").strip().lower()

    if nama_produk == "selesai":
        print("program selesai, terima kasih telah berkunjung")
        break

    if nama_produk in produk:
        print(f"\nnama produk: {nama_produk}")
        print(f"harga : Rp.{produk[nama_produk]}")

        jumlah_barang = int(input("\nmasukan jumlah barang yang dibeli: "))
        if jumlah_barang >0:
            harga = produk[nama_produk]
            subtotal = harga * jumlah_barang
            print(f"\njumlah barang: {jumlah_barang}")
            print(f"total harga jumlah barang : {subtotal}")


        else:
            print("\njumlah barang tidak valid")
    else:
        print("\nproduk tidak ditemukan")








  
