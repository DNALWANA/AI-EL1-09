def binary_search(arr, target):
    """
    Mencari indeks dari nilai 'target' dalam list 'arr' yang sudah terurut.
    Mengembalikan indeks jika ditemukan, atau -1 jika tidak ada.
    """
    left = 0
    right = len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        
        mid = (left + right) // 2

        print(f"Langkah {steps}: Cek nilai di indeks {mid} (angka: {arr[mid]})")

        
        if arr[mid] == target:
            return mid, steps
        
        
        elif arr[mid] < target:
            left = mid + 1
            
        
        else:
            right = mid - 1

    return -1, steps



def main():
    print("=" * 55)
    print("DEMONSTRASI BINARY SEARCH")
    print("=" * 55)

    
    data_angka = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    target_cari = 23

    print(f"Data Array : {data_angka}")
    print(f"Target yang dicari: {target_cari}\n")

    result_index, total_steps = binary_search(data_angka, target_cari)

    print("-" * 55)
    if result_index != -1:
        print(f"HASIL: Angka {target_cari} ditemukan pada indeks ke-{result_index}.")
        print(f"Total langkah pencarian: {total_steps} kali.")
    else:
        print(f"HASIL: Angka {target_cari} tidak ditemukan dalam array.")
    print("=" * 55)


if __name__ == "__main__":
    main()
