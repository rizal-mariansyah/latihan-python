import os

os.system ("cls" if os.name == "nt" else "clear")

data_absensi = []

def catatan_absensi(nama,status):
    data_absensi.append({"nama":nama, "status":status})
    
    print (f"{'nama siswa':<20}: {nama}")
    print (f"{'status kehadiran':<20}: {status}")

catatan_absensi("budi","hadir")
print(data_absensi)

