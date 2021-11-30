# Latihan membuat list python  

* Nama          : Hizbullah Ridwan
* NIM           : 312110055
* Kelas         : TI.21.C.1
* Mata Kuliah   : Bahasa Pemrograman
----------------------------------
Dalam latihan membuat conditional dan loop [python](https://www.python.org/) ini, saya menggunakan [visual studio code](https://code.visualstudio.com/) sebagai teks editornya.     
    

* [Latihan](https://github.com/Ridwanwildan/List-Python#latihan)         
* [Tugas](https://github.com/Ridwanwildan/List-Python#tugas)      
  

## Latihan      

```bash
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

```    

Program ini merupakan latihan cara membuat list, menampilkan elemen yang ada didalam list, mengubah, dan menggabungkannya. Untuk membuat list dan membuat elemen didalamnya, maka seperti ini :       

> a = [10, 20, 30, 40, 50]      

Angka 10 berada di **index ke-0** dan **elemen ke-1**, Angka 20 berada di **index ke-1** dan **elemen ke-2** dan seterusnya berurutan. Untuk mengakses nilai tertentu didalam sebuah list maka kita harus gunakan nomor indexnya. contohnya seperti ini :         

> a[2]       
> mengakses satu index       
> a[1:4]        
> mengakses index ke 1 sampai index ke 4         

Jika ingin mengubah nilai pada index, caranya seperti ini :       

> a[3] = 4444      
> mengubah satu index     
> a[3:] = [3000, 4000]      
> mengubah index ke 3 sampai index terakhir      

Kemudian untuk menambahkan nilai baru didalam listnya kita menggunakan append(), caranya seperti ini :       

> b.append("Hizbullah")         
> menambahkan satu index      
> b.extend([66, 77, 88])      
> menambahkan banyak index       

Dan yang terakhir, jika kita ingin menggabungkan dua list menjadi satu, maka contoh caranya adalah seperti ini :     

> c = a + b       
> menggabungkan a[] dan b[] menjadi c[]         


## Tugas     

![Gambar 1](screenshot/flowchart.PNG)      

```bash
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

```           
![Gambar 2](screenshot/img1.PNG)      

Dalam program ini, pertama kita akan mendekalarasikan list yang kosong. yaitu **nama, nim, tugas, uts, uas** dan nanti akan kita input satu persatu. Kita bisa bebas berapa kali menginputkan data-datanya. Supaya bisa demikian, maka kita harus menggunakan while loop dan akan berhenti jika kita sudah tidak ingin menambah datanya lagi.        

```bash
ulang = "y"

while ulang == "y":
 ```      

 Tadi kita sudah mendeklarasikan beberapa list yang kosong, dan sekarang kita akan mengisinya. Untuk data yang didalamnya berisi angka gunakan integer input. append() artinya kita memasukkan satu nilai dan jika sebelumnya sudah ada nilai, maka nilai yang baru kita masukkan ini akan disimpan di urutan paling belakang.        

```bash
nama.append(input("Nama : "))
 nim.append(input("NIM : "))
 tugas.append(int(input("Nilai tugas : ")))
 uts.append(int(input("Nilai UTS : ")))
 uas.append(int(input("Nilai UAS : ")))
 ulang = input("Tambah data (y/t) ? ")
 ```       

 Setelah while loop selesai, maka kita harus membuat tabel hasilnya. Dan ini merupakan cara membuat header tabelnya.      

```bash
 print("==========================================================================")
print("| No  |          Nama           |    NIM    | Tugas | UTS | UAS |  Akhir |")
print("==========================================================================")
```         

Jika tabelnya sudah dibuat, maka berikutnya kita akan buat isi tabelnya. Dalam membuat isi tabel ini kita menggunakan for loop, karena jumlah banyaknya baris pada tabel harus disesuaikan dengan jumlah data yang tadi sdah kita input. Kita akan mengulang **i** sebanyak n kali dan nilai n ditentukan oleh **len(nama)** yaitu jumlah banyaknya index pada list **nama**.        

```bash
for i in range(len(nama)):
```       

Yang paling kiri ditampilkan adalah nomor. Jika **i** di looping maka **i** akan mulai dari angka 0 dan supaya **i** mulai dari angka 1 kita harus menambahkan i dengan 1 **i+1**. Kita tambah lagi **end=""** Supaya output berikutnya tidak berada di barisan baru.

```bash
print("|", i+1, "  |", end="")
```      

Selanjutnya menampilkan nama. Dalam menampilkan nama, saya menggunakan **print.('{0:<25}'.format())** supaya tampilannya rapi dan bisa menyesuaikan dengan panjang huruf namanya. Supaya nama ditampilkan berurutan dari index ke-0 sampai seterusnya kita gunakan **nama[i]**.         

```bash
print('{0:<25}'.format(nama[i]), end="")
```          

Setelah itu menampilkan NIM, nilai tugas, nilai UTS, dan nilai UAS. Untuk menampilkannya, kita pakai **list[i]** seperti tadi.          

```bash
print("|", nim[i], end="")
print(" |", tugas[i], end="")
print("    |", uts[i], end="")
print("  |", uas[i], " | ", end="")
 ```        

 Yang terakhir adalah menghitung dan menampilkan nilai akhir dari masing-masing datanya. Nilai akhir ini didapat dari penjumlahan **30% nilai tugas**, **35% nilai UTS**, dan **35% nilai UAS**. Supaya angka dibelakang komanya tidak terlalu banyak, kita batasi dengan menambahkan **:.2f** nantinya angka dibelakang koma hanya ada dua angka saja.          

 ```bash
print(f'{(tugas[i]*30/100) + (uts[i]*35/100) + (uas[i]*35/100) :.2f}', " |")
 ```        

 Jangan lupa tambahkan footer tabel dipaling bawahnya.        

 ```bash
 print("==========================================================================")
  ```          

  Terimakasih         