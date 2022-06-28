# set merupakan sebuah implementasi dari konsep himpunan yang digunakan sebagai collection data type yang menggunakan tanda kurung kurawal seperti
# penggunaan dictionary

sets = {1, 2, 3, 4, 5, 6, 7, 8, 9, "ferdian firmansyah", True}
# perbedaan antara dictionary dan set adalah set menggunakan key and value, sedangkan set berkonsep seperti list yang tidak menggunakan key and value
# dalam collection data type
# ketika menggunakan set kita tidak dapat memberikan data kosong dalam set, hal ini akan memberikan kerancuan dimana sistem akan menganggap collection
# type data yang digunakan adalah dictionary
# untuk menggunakan data kosong dapat menggunakan method set yang telah disediakan oleh package python beruapa set()
# dalam penggunaan sett tidak mengenal namanya index seperti penggunaan list dan tuple, sehingga user hanya dapat memanggil value dari collectiond data type tersebut
set_blank = set()

# set tidak mengenal namanya duplikasi ketika mencampur dengan penggunaan collection type data list
# sehingga set akan melakukan validasi data terlebih dahulu untuk mengecek duplikasi data dari collection data type yang digunakan
set_col = set([1, 1, 2, 2, 3, 4, 55, 55])
set_col.add("ff")

# penggunaan remove memiliki kekurangan dimana ketika data yang ingin dihapus tidak ada akan menyebabkan error dan untuk mengatasi
# permasalahan diatas dapat menggunakan method discard
set_col.discard("ff")

# menggabungkan data antar set dengan menggunakan method union(join), inersection(mencari data yang sama diantara set)
set_gab = sets.intersection(set_col)
print(set_col)
print(sets, dict)
print(set_blank)
print(set_col)
print(set_gab)
