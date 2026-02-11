from kbbi import KBBI, TidakDitemukan

# Fungsi cek kata ada di KBBI atau tidak
def ada_di_kbbi(kata):
    try:
        KBBI(kata)
        return True
    except TidakDitemukan:
        return False

# Fungsi membuat permutasi huruf (tanpa itertools)
def permutasi(s):
    if len(s) == 1:
        return [s]
    hasil = []
    for i in range(len(s)):
        huruf = s[i]
        sisa = s[:i] + s[i+1:]
        for p in permutasi(sisa):
            hasil.append(huruf + p)
    return hasil


kata = input("Masukkan kata: ").strip().lower()

# cek dulu kata asli ada di KBBI atau tidak
if not ada_di_kbbi(kata):
    print(f"'{kata}' tidak ada di KBBI, jadi tidak bisa dicek anagram resminya.")
else:
    # buat semua permutasi
    semua_perm = set(permutasi(kata))

    # buang kata aslinya
    semua_perm.discard(kata)

    anagram_valid = []

    # cek tiap permutasi apakah valid di KBBI
    for kandidat in semua_perm:
        if ada_di_kbbi(kandidat):
            anagram_valid.append(kandidat)

    if anagram_valid:
        print(f"Kata '{kata}' PUNYA anagram lain yang valid di KBBI:")
        for w in sorted(anagram_valid):
            print("-", w)
    else:
        print(f"Kata '{kata}' TIDAK punya anagram lain yang valid di KBBI.")
