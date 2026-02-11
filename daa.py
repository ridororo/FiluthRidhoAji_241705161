import time
import matplotlib.pyplot as plt

# Implementasi Linear Search berdasarkan paradigma brute force
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return i
    return -1

# Implementasi Binary Search berdasarkan paradigma divide and conquer
def binary_search(data, target):
    low = 0
    high = len(data) - 1
    while low <= high:
        mid = (low + high) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# Setup Eksperimen dengan variasi ukuran input n
sizes = [1000, 5000, 10000, 50000, 100000]
linear_times = []
binary_times = []

for n in sizes:
    # Menghasilkan data mahasiswa berupa NIM yang sudah terurut
    data_mahasiswa = list(range(n)) 
    target = -1 # Mencari data yang tidak ada untuk skenario Worst Case

    # Mengukur durasi waktu eksekusi Linear Search
    start = time.perf_counter()
    linear_search(data_mahasiswa, target)
    linear_times.append(time.perf_counter() - start)

    # Mengukur durasi waktu eksekusi Binary Search
    start = time.perf_counter()
    binary_search(data_mahasiswa, target)
    binary_times.append(time.perf_counter() - start)

# Menampilkan output tabel hasil eksperimen ke terminal
print(f"{'n':<10} | {'Linear (s)':<15} | {'Binary (s)':<15}")
for i in range(len(sizes)):
    print(f"{sizes[i]:<10} | {linear_times[i]:<15.6f} | {binary_times[i]:<15.6f}")