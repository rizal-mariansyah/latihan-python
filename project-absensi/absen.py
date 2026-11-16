import os

os.system ("cls" if os.name == "nt" else "clear")

data_absensi = []

def catatan_absensi(nama,status):
    data_absensi.append({"nama":nama, "status":status})
    
    print (f"{'nama siswa':<20}: {nama}")
    print (f"{'status kehadiran':<20}: {status}")

catatan_absensi("budi","hadir")
catatan_absensi("sari","sakit")
catatan_absensi("wahyu","alpa")
catatan_absensi("Andi","hadir")



print("="*10, "Rekap Absensi","="*10,"\n")

kehadiran = 0

hitung = {
    "hadir": 0,
    "izin": 0,
    "sakit": 0,
    "alpa": 0
}
for nomor, s in enumerate (data_absensi,start=1):
    if s["status"] == "hadir":
        kehadiran += 1
    
    hitung[s["status"]] += 1
    jumlah_hadir= len(data_absensi) / kehadiran * 100

        
    print(f"{nomor}. {s['nama']:<8} - {s['status']}") 

print(f"jumlah hadir : {kehadiran} dari {len(data_absensi)} siswa")
print ("="*10,"Ringkasan","="*10)
print(f"{s["status"]} : {jumlah_hadir:.1f}")


