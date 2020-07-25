"""
Tipe data Dictionary menghubungkan antara KEY dan VALUE
KVP = KEY VALUE PAIR
Dictionary = Kamus
"""
import datetime
now = datetime.datetime.now()

#CONTOH 1
kamus = {}                  Contoh data dict simple
kamus  ['anak'] = 'son'
kamus  ['istri'] = 'wife'
kamus  ['ayah'] = 'father'
kamus  ['ibu'] = 'mother'
print(kamus['ibu'])   #Ambil Value"ibu" didalam data Dict

#CONTOH 2
print('\nIni CONTOH ke 2')
data_dari_server_gojek = {
    'tanggal': {now.strftime("%d-%m-%Y %H:%M:%S")},
    'driver_list': [                        #Penggunaan data List dengan Data Dictionary
        {'nama': 'Hardiyan', 'jarak': 10},
        {'nama': 'Devi', 'jarak': 20},
        {'nama': 'Jenna','jarak': 30 },
        {'nama': 'Jihan','jarak': 40}
    ]
}

print(data_dari_server_gojek)
print(f"Driver disekitar Anda {data_dari_server_gojek['driver_list']}")
print(f"Driver #1{data_dari_server_gojek['driver_list'][0]}")
print(f"Driver #2{data_dari_server_gojek['driver_list'][1]}")
print(f"Driver #3{data_dari_server_gojek['driver_list'][2]}")
print(f"Sekarang tanggal {data_dari_server_gojek['tanggal']} Jarak Driver terdekat adalah {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
