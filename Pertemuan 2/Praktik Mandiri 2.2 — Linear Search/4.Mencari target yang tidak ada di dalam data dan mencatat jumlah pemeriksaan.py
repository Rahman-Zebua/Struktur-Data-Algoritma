#Mencari target yang tidak ada di dalam data dan mencatat jumlah pemeriksaan
def trace(data, target):
    pemeriksaan = 0
    for i in range(len(data)):
        pemeriksaan += 1
        if data[i] == target:
            print("Target ditemukan pada indeks", i)
            print("Jumlah pemeriksaan:", pemeriksaan)
            return
    print("Target tidak ditemukan")
    print("Jumlah pemeriksaan:", pemeriksaan)
bilangan = [25, 7, 42, 13, 9, 31, 18, 50, 4, 27, 15, 36, 2, 44, 21]
target = 100
trace(bilangan, target)