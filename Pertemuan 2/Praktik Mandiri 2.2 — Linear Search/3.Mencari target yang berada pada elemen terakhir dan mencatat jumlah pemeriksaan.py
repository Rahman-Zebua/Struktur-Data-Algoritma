#Mencari target yang berada pada elemen terakhir dan Mencatat jumlah pemeriksaan
def trace(data, target):
    pemeriksaan = 0
    for i in range(len(data)):
        pemeriksaan += 1
        print("Pemeriksaan ke-", pemeriksaan, ":", data[i])
        if data[i] == target:
            print("Target ditemukan pada indeks", i)
            print("Jumlah pemeriksaan:", pemeriksaan)
            return
bilangan = [25, 7, 42, 13, 9, 31, 18, 50, 4, 27, 15, 36, 2, 44, 21]
target = 21
trace(bilangan, target)