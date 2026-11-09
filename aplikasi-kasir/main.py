import os

os.system ("cls" if os.name == "nt" else "clear")


print("========== toko sederhana ==========\n")
print("Daftar produk\n")
print(40*"-","\n")

#nama produk
produk = {"buku": 5000,
          "pensil": 2000,
          "penghapus": 1500,
          "penggaris": 3000
}

total_belanja = 0

for nama,harga in produk.items():
    print(f"{nama:<12}: Rp. {harga}")
   

# koding utama
while True :
    
    nama_produk = input("\nmasukan nama produk: ").strip().lower()

    if nama_produk in produk:
        print(f"\nnama produk: {nama_produk}")
        print(f"harga : Rp.{produk[nama_produk]}")

        jumlah_barang = int(input("\nmasukan jumlah barang yang dibeli: "))
        if jumlah_barang >0:
            harga = produk[nama_produk]
            subtotal = harga * jumlah_barang
            total_belanja += subtotal
            print(f"\njumlah barang: {jumlah_barang}")
            print(f"total harga jumlah barang :Rp. {subtotal}")


        else:
            print("\njumlah barang tidak valid")
    else:
        print("\nproduk tidak ditemukan")

    pilihan = input("\nlanjut belanja (ya/tidak): ").strip().lower()

    if pilihan == "ya":
            print(f"total belanjaan: Rp.{total_belanja}")
            continue
    
    
    elif pilihan == "tidak":
        print(f"\ntotal belanjaan = Rp.{total_belanja}")
        uang_bayar = int(input("\nmasukan uang pembayaran: Rp."))
        if uang_bayar >= total_belanja:
            kembalian = uang_bayar - total_belanja
            total_akhir = uang_bayar - kembalian

    else:
        print("pembayaran tidak valid")
        break

    print(f"total belanjaan = Rp.{total_belanja}")
    print(f"uang bayar = Rp.{uang_bayar}")
    print(f"total kembalian = Rp.{kembalian}")
    print(f"total akhir pembayaran = Rp.{total_akhir}")
    print("terimakasih telah berkunjung")
    break
    


        
            
        








  
