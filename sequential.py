"""
sequential code di running dengan berurutan
jika kode diatasnya salah/error maka tidak akan dilanjutkan ke code selanjutnya
"""
import datetime
now = datetime.datetime.now()
print('#'*30)
print('Belajar Python')
print(f'pada tanggal {now.strftime("%d-%m-%Y %H:%M:%S")}')
print('#'*30)

#command diatas berfungi menunjukan waktu dengan import package datetime
#dan mengatur format date time dengan strftime