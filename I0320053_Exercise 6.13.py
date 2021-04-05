def tambah (a,b):
    c = a+b
    return c

x = int(input('Masukkan bilangan pertama : '))
y = int(input('Masukkan bilngan kedua : '))

hasil = tambah(x,y)
print(' %d + %d = %d' %(x,y, hasil))