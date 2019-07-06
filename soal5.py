arr = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
arr2 = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

x = str(input("masukan kata : "))
z = x.split(' ')
batas = len(z)
i = 0
arr = []
while i <= batas-1:
    arr.append([z[i]])
    i=i+1

z =0
data = []
while z <= batas-1:
    uh = arr[z]
    t = ''.join(uh)
    ubah = list(t)
    data.append(ubah)
    # print(ubah)
    z=z+1

y = 0

itung = 0
hasil = []
pjml = 0
asx = 0
endd = []
while y <= batas-1:
    # print(batas)
    # print(y)
    bts =len(data[y])
    rx = bts-1
    pjml = pjml * asx
    # print(rx)

    n = 0
    while n <= rx:
        try:
            hsl = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'].index(str(data[y][n]))
            pjml = pjml + (hsl+1)
            n = n + 1
        except ValueError:
            hsl = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z'].index(str(data[y][n]))
            n = n + 1
            pjml = pjml + (hsl+1)
    y = y + 1
    asx = asx + 1
    endd.append(pjml)
# print(data)
print(endd)
