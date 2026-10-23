

import heapq


def binary_search(arr, target):
    """Mencari target pada list terurut. Mengembalikan indeks dan jumlah langkah."""
    left = 0
    right = len(arr) - 1
    steps = 0

    while left <= right:
        steps += 1
        mid = (left + right) // 2

        print(
            f"Langkah {steps}: memeriksa indeks {mid} "
            f"(nilai: {arr[mid]})"
        )

        if arr[mid] == target:
            return mid, steps
        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1, steps


def run_binary_search():
    print("\n" + "=" * 55)
    print("DEMONSTRASI BINARY SEARCH")
    print("=" * 55)

    data = [2, 5, 8, 12, 16, 23, 38, 56, 72, 91]
    print(f"Data terurut: {data}")

    try:
        target = int(input("Masukkan angka yang dicari: "))
    except ValueError:
        print("Input tidak valid. Masukkan angka bulat.")
        return

    print()
    index, steps = binary_search(data, target)
    print("-" * 55)

    if index != -1:
        print(f"HASIL: Angka {target} ditemukan pada indeks ke-{index}.")
    else:
        print(f"HASIL: Angka {target} tidak ditemukan.")

    print(f"Jumlah langkah pencarian: {steps}")
    print("=" * 55)




def a_star_search(graph, heuristic, start, goal):
    """
    Mencari jalur dengan biaya terendah menggunakan A*.
    f(n) = g(n) + h(n)
    """
    if start not in graph or goal not in graph:
        return None, float("inf")

    priority_queue = [(heuristic.get(start, 0), 0, start, [start])]
    best_cost = {start: 0}

    print(f"\nMulai pencarian dari [{start}] menuju [{goal}]...\n")

    while priority_queue:
        f_score, g_score, current, path = heapq.heappop(priority_queue)

        if g_score > best_cost.get(current, float("inf")):
            continue

        print(
            f"Mengunjungi node: {current} | "
            f"Biaya g: {g_score} | Estimasi total f: {f_score}"
        )

        if current == goal:
            return path, g_score

        for neighbor, weight in graph.get(current, []):
            if weight < 0:
                raise ValueError("A* memerlukan bobot sisi nonnegatif.")

            new_cost = g_score + weight

            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                estimate = heuristic.get(neighbor, 0)
                new_f_score = new_cost + estimate

                heapq.heappush(
                    priority_queue,
                    (new_f_score, new_cost, neighbor, path + [neighbor])
                )

    return None, float("inf")


def run_a_star():
    print("\n" + "=" * 55)
    print("DEMONSTRASI A* SEARCH")
    print("=" * 55)

    city_graph = {
        "A": [("B", 1), ("C", 4)],
        "B": [("A", 1), ("D", 2), ("E", 5)],
        "C": [("A", 4), ("F", 3)],
        "D": [("B", 2), ("G", 3)],
        "E": [("B", 5), ("G", 1)],
        "F": [("C", 3), ("G", 2)],
        "G": [("D", 3), ("E", 1), ("F", 2)],
    }

    heuristic_values = {
        "A": 7,
        "B": 6,
        "C": 5,
        "D": 2,
        "E": 3,
        "F": 2,
        "G": 0,
    }

    print("Node tersedia: A, B, C, D, E, F, G")
    start = input("Masukkan node awal: ").strip().upper()
    goal = input("Masukkan node tujuan: ").strip().upper()

    if start not in city_graph or goal not in city_graph:
        print("Input tidak valid. Gunakan node A, B, C, D, E, F, atau G.")
        return

    try:
        path, total_cost = a_star_search(
            city_graph, heuristic_values, start, goal
        )
    except ValueError as error:
        print(f"Terjadi kesalahan: {error}")
        return

    print("\n" + "=" * 55)
    print("HASIL PENCARIAN JALUR A*")
    print("=" * 55)

    if path is not None:
        print("Jalur: " + " -> ".join(path))
        print(f"Total biaya/jarak: {total_cost}")
    else:
        print("Jalur tidak ditemukan.")

    print("=" * 55)



def main():
    while True:
        print("\n" + "=" * 55)
        print("PROGRAM GABUNGAN SEARCH ALGORITHM")
        print("=" * 55)
        print("1. Binary Search")
        print("2. A* Search")
        print("0. Keluar")
        print("=" * 55)

        choice = input("Pilih menu (0/1/2): ").strip()

        if choice == "1":
            run_binary_search()
        elif choice == "2":
            run_a_star()
        elif choice == "0":
            print("Program selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Masukkan 0, 1, atau 2.")


if __name__ == "__main__":
    main()
