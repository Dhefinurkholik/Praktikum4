def angka_terbesar (a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    return c
def angka_terkecil (a, b, c):
    if a < b and b < c:
        return a
    elif b < a and b < c:
        return b
    return c
def nilai_tengah (a, b, c):
    if (b > a > c) or (c > b > a):
        return a
    elif (a > b > c) or (c > b > a):
        return b
    return c
a, b, c = (
    int(input('masukan nilai a: ')),
    int(input('masukan nilai b: ')),
    int(input('masukan nilai c: '))
)
i1 = angka_terkecil(a, b, c)
i2 = nilai_tengah(a, b, c)
i3 = angka_terbesar(a, b, c)
print(f'urutan: {i1}, {i2}, {i3}')