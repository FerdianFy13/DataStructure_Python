# named tuple merupakan sebuah peningkatan dari tuple dimana name tuple dapat mengakses element didalamnya yang memungkingkan user untuk memiliki sebuha struktur data
# yang serupa dengan penggunaan tuple yang dapat diakses berdasarkan nama yang menggunakan package collections

from collections import namedtuple as nt

# penamaan nama harus sesuai dengan penamaan variable agar memudahkan ketika proses pemanggilannya
product = nt("product", ["handphone", "laptop", "mouse"])
product1 = product("hp", "lenovo", "fantech")

# named tuple memperhatikan urutan dari field type yang telah dituliskan karena mendukung penggunana built in structure data
# cara mengakses named tuple dalam bahasa pemrograman python
print(product1)

# untuk mengakes value didalamnya user cukup menggunakan tanda titik atau dot dibelkang nametype
print(product1.handphone)

# summary
# -   Named tuple murapakan collection data type, artinya named tuple dapat digunakan untuk menampung sekumpulan nilai/data.
# -   Named tuple merupakan sequence data type, artinya nilai/data yang tersimpan di dalam named tuple dapat diakses berdasarkan index numerik. Hanya saja nilai pada named tuple umumnya diakses dengan memanfaatkan nama.
# -   Named tuple merupakan immutable data type, artinya kita tidak dapat mengubah, menambah, ataupun menghapus nilai/data yang ditampung di dalam sebuah named tuple.
