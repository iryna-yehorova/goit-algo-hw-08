import heapq


def optimal_cable_connections(cables):
    heap = list(cables)
    heapq.heapify(heap)

    total_cost = 0
    connections = []

    while len(heap) > 1:
        first = heapq.heappop(heap)
        second = heapq.heappop(heap)
        combined = first + second

        connections.append((first, second, combined))
        total_cost += combined
        heapq.heappush(heap, combined)

    return total_cost, connections


if __name__ == "__main__":
    cost, steps = optimal_cable_connections([4, 3, 2, 6])
    for first, second, combined in steps:
        print(f"{first} + {second} = {combined}")
    print(f"Загальні витрати: {cost}")  # 29
