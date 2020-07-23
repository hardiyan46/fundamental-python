"""
sequential code di running dengan berurutan
jika kode diatasnya salah maka tidak akan dilanjutkan ke code selanjutnya
"""
import datetime
now = datetime.datetime.now()
print('#'*20)
print('Belajar Python')
print(f'pada tanggal {now.strftime("%d-%m-%Y %H:%M:%S")}')
print('#'*20)

#command diatas berfungi menunjukan waktu dengan import package datetime
#dan mengatur format date time dengan strftime