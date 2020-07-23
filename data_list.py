anak_yunus = ['Hardiyan', 'Irma', 'Dini']
anak_darja = ['yuselda', 'Devi']
anak_yunus.append('joni')  #fungsi append menambahkan data ke dalam data list
print(anak_yunus)
print(anak_darja)

print(f'\nAnak ke 1 dari Bapak Yunus Adalah {anak_yunus[0]}') #mengambil data dari data list
print(f'Anak ke 2 dari Bapak Darja Adalah {anak_darja[1]}') #mengambil data dari data list
print(f'\nAnak Bapak Yunus Bernama {anak_yunus}')
print(f'Anak Bapak Darja Bernama {anak_darja}')

#sapa semua anak metode simple
for a in anak_yunus:
    print(f'Hai {a}')

#sapa semua anak metode ribet
for a in range(0, len(anak_darja)):         #len digunakan untuk mengambil jumlah list
    print (f'{a+1}Hai {anak_darja[a]}')
