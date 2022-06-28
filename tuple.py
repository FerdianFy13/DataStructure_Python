# perbedaan antara tuple dan list adalah dari tandanya saja jika list menggunakan tanda kurung siku dan jika tuples menggunakan tanda kurung

tuple = (10, 20, "ferdi", True)

print(tuple[1])

# crud
# tuple tidak dapat melakukan sebuah crud berbeda dengana penggunaan list yang dapat melakukan sebuah tuple
# tuple dapat menggabungkan penggunaan list dengan collection tuple sendiri hanya saja tidak dapat melakukan sebuah crud

tuple_2 = ("wkk", "handsome", [2, 10])
result = tuple_2 + tuple
print(result)
