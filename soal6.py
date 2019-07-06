x = int(input('masukan teka-teki: '))

i = 0
batas = len(str(x))
spliz = list(str(x))
# print(batas
# print(spliz[2])
hasil = [
    'mati',
    'mati',
    'mati',
    'mati',
    'mati',
    'mati',
    'mati',
    'mati',
    'mati',
    'mati',
    'mati',
    'mati',
    'mati',
    'mati',
    'mati',
]
z = 0
while i <= batas-1:
    saklar = spliz[i]
    if int(saklar) == 1:
        z = 0
        while z <= 14:
            if hasil[z] == 'mati':
                hasil[z] = 'hidup'
            else:
                hasil[z] ='mati'
            z=z+1
    if int(saklar) == 2:
        z = 1
        u = 0
        m = [2,4,6,8,10,12,14]
        while z <= 15:
            if z in m:
                sklr = hasil[z-1]
                if hasil[z-1] == 'mati':
                    hasil[z-1] = 'hidup'
                elif hasil[z-1] == 'hidup' :
                    hasil[z-1] ='mati'
            z=z+1
    if int(saklar) == 3:
        z = 1
        u = 0
        m = [3,6,9,12,15]
        while z <= 15:
            # print(z)
            if z in m:
                sklr = hasil[z-1]
                if hasil[z-1] == 'mati':
                    hasil[z-1] = 'hidup'
                elif hasil[z-1] == 'hidup' :
                    hasil[z-1] ='mati'
            z=z+1

    i=i+1
print(hasil)
hitung_ganjil =hasil.count('mati')
hitung_genap = hasil.count('hidup')

print("Jumlah lampu menyala : " + " " +str(hitung_genap))
print("Jumlah lampu mati : " + " " +str(hitung_ganjil))
