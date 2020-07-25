"""
Tipe data Dictionary menghubungkan antara KEY dan VALUE
KVP = KEY VALUE PAIR
Dictionary = Kamus
"""
#CONTOH 1
kamus = {}
kamus  ['anak'] = 'son'
kamus  ['istri'] = 'wife'
kamus  ['ayah'] = 'father'
kamus  ['ibu'] = 'mother'
print(kamus['ibu'])

#CONTOH 2
print('\nIni CONTOH ke 2')
data_dari_server_gojek = {
    'tanggal': '2020-07-25',
    'driver_list': [                        #Penggunaan data List dengan Data Dictionary
        {'nama': 'Hardiyan', 'jarak': 10},
        {'nama': 'Devi', 'jarak': 20},
        {'nama':'Jenna','jarak': 30 },
        {'nama': 'Jihan','jarak': 40}
    ]
}

print(data_dari_server_gojek)
print(f"Driver disekitar Anda {data_dari_server_gojek['driver_list']}")
print(f"Driver #1{data_dari_server_gojek['driver_list'][0]}")
print(f"Driver  #2{data_dari_server_gojek['driver_list'][1]}")
print(f"Driver #3{data_dari_server_gojek['driver_list'][2]}")
print(f"Jarak Driver terdekat adalah {data_dari_server_gojek['driver_list'][0]['jarak']} meter")
