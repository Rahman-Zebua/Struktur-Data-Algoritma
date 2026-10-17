# Pencarian data mahasiswa

# Pencarian menggunakan list
mahasiswa_list = [
    ("22001", "Alya"),
    ("22002", "Bima"),
    ("22003", "Citra")
]


def cari_nim(data, nim):
    for item in data:
        if item[0] == nim:
            return item
    return None


print(cari_nim(mahasiswa_list, "22003"))

# Pencarian menggunakan dictionary
mahasiswa_dict = {
    "22001": "Alya",
    "22002": "Bima",
    "22003": "Citra"
}

print(mahasiswa_dict.get("22003"))