#Mencari seluruh kemunculan target
def linear_search_all(data, target):
    posisi = []
    for index, value in enumerate(data):
        if value == target:
            posisi.append(index)
    return posisi
data = [20, 10, 20, 30, 20]
print(linear_search_all(data, 20))