#Pencarian Data Mahasiswa (Linear Search pada NIM)
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1
nim = ['41250017', '41250003', '41250029', '41250011', '41250008']
target = '41250011'
posisi = linear_search(nim, target)
if posisi != -1:
    print('NIM ditemukan pada indeks', posisi)
else:
    print('NIM tidak ditemukan')