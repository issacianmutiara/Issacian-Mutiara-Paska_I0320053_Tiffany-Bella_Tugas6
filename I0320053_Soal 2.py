print('=====Menghitung rata rata=====')
print()

x = int(input('Masukkan jumlah data input: '))
data = []
i = 1
while i <= x:
    score = float(input("Masukkan nilai : "))
    data.append(score)
    i += 1

rata2 = sum(data)/x
print()
print("Nilai rata rata dari data yang telah di input adalah : ")