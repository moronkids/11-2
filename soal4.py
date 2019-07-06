
import math
tgl = int(input('masukan tanggal : '))
uang = int(input('masukan jumlah uang : '))

mie = 2500
batas = 30
i = 0
# untuk mendapatakan kelipatan mie 3
mie_kelipatan_3 = 3
mie_3_list = []
while mie_kelipatan_3 <= 30:
    mie_3_list.append(mie_kelipatan_3)
    mie_kelipatan_3 = mie_kelipatan_3 + 3
# untuk mendapatakan kelipatan mie 3

# untuk mendapatakan kelipatan mie 4
mie_kelipatan_4 = 4
mie_4_list = []
while mie_kelipatan_4 <= 30:
    mie_4_list.append(mie_kelipatan_4)
    mie_kelipatan_4 = mie_kelipatan_4 + 4
# untuk mendapatakan kelipatan mie 4

# untuk mendapatakan kelipatan tanggal 5
tanggal_awal = 5
tanggal_list = []
while tanggal_awal <= 30:
    tanggal_list.append(tanggal_awal)
    tanggal_awal = tanggal_awal + 5
# untuk mendapatakan kelipatan tanggal 5

if tgl in tanggal_list:
    if tgl % 2 == 0:
        jml_mie = uang / mie
        buletin =math.floor(jml_mie)
        akhir = buletin / 4
        if math.floor(akhir) % 2 == 0:
            buletin = buletin + math.floor(akhir) * 10
        else:
            buletin = buletin + math.floor(akhir) * 5
    else:
        jml_mie = uang / mie
        buletin =math.floor(jml_mie)
        akhir = buletin / 3
        if math.floor(akhir) % 2 == 0:
            buletin = buletin + math.floor(akhir) * 10
        else:
            buletin = buletin + math.floor(akhir) * 5
else:
    if tgl % 2 == 0:
        jml_mie = uang / mie
        buletin =math.floor(jml_mie)
        akhir = buletin / 4
        buletin = buletin + math.floor(akhir) * 1

    else:
        jml_mie = uang / mie
        buletin = math.floor(jml_mie)
        akhir = buletin / 3
        buletin = buletin + math.floor(akhir) * 1

print('jumlah mie yang didapatakan adalah : '+ " " + str(buletin))
