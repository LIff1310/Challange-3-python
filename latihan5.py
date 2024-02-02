from datetime import date as dt
print(f"<< \t\t UMUR \t\t >>")
print("-"*25)
print("Masukan Tanggal, Bulan Dan Tahun Lahir")
print("\n")
tanggal = int(input("Tanggal \t\t : "))
bulan = int(input("bulan \t\t\t : "))
tahun = int(input("tahun \t\t\t : "))

tgllahir = dt( tahun, bulan, tanggal )
today = dt.today()
print(f"Tanggal Lahir \t\t : {tgllahir}",)
print(f"Tanggal hari ini \t : {today}")

selisihtgl = today - tgllahir
print(f"selisih tanggal : {selisihtgl.days}")

usiatahun = selisihtgl.days // 365
usiabulan = (selisihtgl.days % 365) // 30
print(f"Umur : {usiatahun} dan {usiabulan} bulan")