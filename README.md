# Tekno Class 2022 - Week 3
Tekno class 2022 Assignment

* NAMA: -
* NIM: -

## Catatan
1. Dilarang mengubah default template dari code atau file
2. Dilarang mengubah dataset yang ada didalam dataset.py
3. Gunakan print() untuk menampilkan hasil
4. Sertakan nama dan NIM kamu diatas

## Assignment - Studi Kasus File Manager
Disini kamu akan menyelesaikan permasalahan menggunakan struktur data di python dengan konsep studi kasus file manager. Kamu akan coba untuk mengakses, membuat, dan menampilkan data-data file dan folder dalam bentuk objek collection.

## Assignment 1
Kamu diminta Untuk mencari file dengan nama tertentu (exact) kemudian kembalikan ID nya. Catatan bahwa kemungkinan file dengan nama tersebut ada lebih dari satu, maka kembaliannya adalah list ID file tersebut.

### Sample Input
```
file5.txt
```

### Sample Output
```
[17, 16]
```


## Assignment 2
Disini kamu diminta untuk mencari folder dengan ID tertentu sesuai input, kemudian kembalikan ID dari children yang ada di folder tersebut, ingat bahwa kembalian berupa List

### Sample Input
```
3
```

### Sample Output
```
[6, 17]
```


## Assignment 3
Disini kamu diminta untuk mencari entitas (File/folder) yang mengandung string nama tertentu (include), kemudian kembalikan ID dari setiap item yang ditemukan, ingat bahwa kembalian berupa list ID dari item tersebut.

### Sample Input
```
profile
```

### Sample Output
```
[14, 15]
```


## Assignment 4
Disini kamu diminta untuk membuat file baru dan memasukannya kedalam folder dengan ID tertentu, kemudian kembalikan lagi dataset tersebut. Perlu diingat bahwa beberapa folder kemungkinan tidak dapat dimasukkan file baru (disable).

### Sample Input
```
3
```

### Sample Output
```
[{'id': 1, 'name': 'folder1', 'is_file': False, 'children': [{'id': 3, 'name': 'folder1-1', 'is_file': False, 'children': [{'id': 6, 'name': 'file1.txt', 'is_file': True}, {'id': 17, 'name': 'file5.txt', 'is_file': True}, {'id': 18, 'name': 'mynewfile.txt', 'is_file': True}]}, {'id': 4, 'name': 'folder1-2', 'is_file': False, 'children': [{'id': 8, 'name': 'folder1-2-1', 'is_file': False, 'children': [{'id': 9, 'name': 'file3.txt', 'is_file': True}, {'id': 14, 'name': 'folder_profile', 'is_file': False, 'children': ({'id': 15, 'name': 'profile.pdf', 'is_file': True}, {'id': 16, 'name': 'file5.txt', 'is_file': True})}]}]}, {'id': 5, 'name': 'folder1-3', 'is_file': False, 'children': [{'id': 10, 'name': 'file4.txt', 'is_file': True}, {'id': 11, 'name': 'folder_photo', 'is_file': False, 'children': ({'id': 12, 'name': 'photo1.jpg', 'is_file': True}, {'id': 13, 'name': 'file1.txt', 'is_file': True})}]}]}, {'id': 2, 'name': 'folder2', 'is_file': False, 'children': [{'id': 7, 'name': 'photo2.png', 'is_file': True}]}]
```