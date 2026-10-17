# Fungsi pencarian linear
def cari(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1


data = [12, 20, 7, 30]

print(cari(data, 7))
print(cari(data, 99))