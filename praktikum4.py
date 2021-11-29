nama = []
nim = []
tugas = []
uts = []
uas = []
ulang = "y"

while ulang == "y":
 nama.append(input("Nama : "))
 nim.append(input("NIM : "))
 tugas.append(int(input("Nilai tugas : ")))
 uts.append(int(input("Nilai UTS : ")))
 uas.append(int(input("Nilai UAS : ")))
 ulang = input("Tambah data (y/t) ? ")

print("==========================================================================")
print("| No  |          Nama           |    NIM    | Tugas | UTS | UAS |  Akhir |")
print("==========================================================================")

for i in range(len(nama)):
 print("|", i+1, "  |", end="")
 print('{0:<25}'.format(nama[i]), end="")
 print("|", nim[i], end="")
 print(" |", tugas[i], end="")
 print("    |", uts[i], end="")
 print("  |", uas[i], " | ", end="")
 print(f'{(tugas[i]*30/100) + (uts[i]*35/100) + (uas[i]*35/100) :.2f}', " |")
print("==========================================================================")

