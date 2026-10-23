
import heapq


def a_star_search(graph, heuristic, start, goal):
    """
    Mencari jalur berbiaya terendah menggunakan A*.
    f(n) = g(n) + h(n)
    """
    if start not in graph or goal not in graph:
        return None, float("inf")

    start_h = heuristic.get(start, 0)
    priority_queue = [(start_h, 0, start, [start])]
    best_cost = {start: 0}

    print(f"Mulai pencarian jalur dari [{start}] menuju [{goal}]...\n")

    while priority_queue:
        f_score, g_score, current, path = heapq.heappop(priority_queue)

        if g_score > best_cost.get(current, float("inf")):
            continue

        print(
            f"Mengunjungi node: {current} | "
            f"Cost g: {g_score} | Estimasi total f: {f_score}"
        )

        if current == goal:
            return path, g_score

        for neighbor, weight in graph.get(current, []):
            if weight < 0:
                raise ValueError("A* pada contoh ini membutuhkan bobot nonnegatif.")

            new_cost = g_score + weight
            if new_cost < best_cost.get(neighbor, float("inf")):
                best_cost[neighbor] = new_cost
                estimate = heuristic.get(neighbor, 0)
                heapq.heappush(
                    priority_queue,
                    (
                        new_cost + estimate,
                        new_cost,
                        neighbor,
                        path + [neighbor],
                    ),
                )

    return None, float("inf")


def main():
    print("=" * 55)
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

    print("Node yang tersedia: A, B, C, D, E, F, G")
    start_node = input("Masukkan node awal: ").strip().upper()
    goal_node = input("Masukkan node tujuan: ").strip().upper()

    if start_node not in city_graph or goal_node not in city_graph:
        print("Node tidak valid. Gunakan node A sampai G.")
        return

    path, total_cost = a_star_search(
        city_graph, heuristic_values, start_node, goal_node
    )

    print("\n" + "=" * 55)
    print("HASIL PENCARIAN JALUR A*")
    print("=" * 55)

    if path is not None:
        print(f"Jalur: {' -> '.join(path)}")
        print(f"Total biaya/jarak: {total_cost}")
    else:
        print("Jalur tidak ditemukan.")

    print("=" * 55)


if _name_ == "_main_":
    main()
