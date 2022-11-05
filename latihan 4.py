print('-----Bilangan acak yang lebih kecil dari 0.5-----')
print(' ')
import random
N = int(input('Masukan nilai N : '))
a = 0
for i in range(N):
    a +=1
    b = random.uniform(.0,.5)
    print('Data ke :',a,'--->',b)
print('Selesai')
print (' ')
jawab = 'lanjutkan'
hitung = 0
while jawab == 'lanjutkan':
      hitung += 1
      jawab = input('ingin mengulanginya ? (lanjutkan/tidak)')
      if jawab == 'tidak':
        break
print(f'Total Perulangan : '+ str (hitung))
print('-----Selesai-----')