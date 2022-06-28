# dictionary merupakan sebuah collection type data yang menggunakan key and value seperti assosiative array atau biasa disebut juga semacam hash map
# perbedaan antara tuples list dan dictionary adalah terletak dari tanda penggunaannya jika dictionary menggunakan tanda kurung kurawal
dic = {"nama": "ferdian", "nim": 362055401191}

# akses dictionary dalama bahasa pemrograman python
print(dic["nama"])
print(dic["nim"])

# untuk membaca dictionary dapat mengunakna methode get
# dengan menggunakan methode get kita dapat memberikan pesan error jika key yang dicari dalam dictionary tidak dapat ditemukan ketika dicari dalam data dictionary didalamnya
print(dic.get("namas", "data not found"))

# akses keseluruhan dictionary dalama bahasa pemrograman python
print(dic, dict)

dk = dic.keys()
dv = dic.values()
di = dic.items()
for x in di:
    print(x)
