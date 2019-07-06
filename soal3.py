x = int(input("Masukan angaka :"))
i = 0
p = []
while x != 1:
    if x % 2 == 0:
        x = x /2
        p.append(x)
    else:
        x = 3 * x + 1
        p.append(x)
print('Bilangan asli dengan operasi terbanyak' + ' : ' +str(len(p)))
