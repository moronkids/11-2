
x = int(input("Masukan angaka :"))
abs = x
i = 1
p = []
while x >= 1:
    ang = x
    z = []
    p.append(z)
    while ang != 1:
        if ang % 2 == 0:
            ang = ang /2
            z.append(ang)
        else:
            ang = 3 * ang + 1
            z.append(ang)
    x=x-1

# print(abs)
z = 0
tampung = []
while z <= abs-1:
    # print(z)
    data = len(p[z])
    tampung.append(data)
    z= z+1

tampung.reverse()
max = max(tampung)
nomor = tampung.index(max)
dapet = (nomor+1)
print('Bilangan asli dengan operasi terbanyak' + ' : ' +str(dapet))
