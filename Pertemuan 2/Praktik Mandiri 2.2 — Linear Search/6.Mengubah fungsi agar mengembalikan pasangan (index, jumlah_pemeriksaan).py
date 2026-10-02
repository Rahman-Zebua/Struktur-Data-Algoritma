#Mengubah fungsi agar mengembalikan pasangan (index, jumlah_pemeriksaan)
def trace(data, target):
    pemeriksaan = 0
    for i in range(len(data)):
        pemeriksaan += 1
        if data[i] == target:
            return (i, pemeriksaan)
    return (-1, pemeriksaan)
bilangan = [25, 7, 42, 13, 9, 31, 18, 50, 4, 27, 15, 36, 2, 44, 21]
target = 21
hasil = trace(bilangan, target)
print(hasil)