# Ada list yang memiliki 5 elemen
a = [10, 20, 30, 40, 50]

# Tampilkan elemen ke 3
print(a[2])

# Ambil nilai elemen ke 2 sampai ke 4
a[1:3]

# Ambil elemen terakhir
a[4]

# Ubah elemen ke 4 dengan nilai lainnya
a[3] = 4444

# Ubah elemen ke 4 sampai dengan elemen terakhir
a[3:] = [3000, 4000]

# Ambil 2 bagian dari list pertama (a) dan jadikan list kedua (b)
b = a[0:2]

# Tambah list B dengan nilai string
b.append("Hizbullah")

# Tambah list B dengan 3 nilai
b.extend([66, 77, 88])

# Gabungkan list B dengan list A
c = a + b
