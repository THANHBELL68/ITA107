
# PHẦN A - PHÁT HIỆN CHU TRÌNH ĐỒ THỊ VÔ HƯỚNG


def has_cycle_undirected(graph):
    """
    Phát hiện chu trình trong đồ thị vô hướng.

    Ý tưởng:
    - DFS
    - Nếu gặp đỉnh đã visited
      và đỉnh đó KHÔNG phải parent
      => tồn tại chu trình
    """

    visited = set()

    def dfs(vertex, parent):

        visited.add(vertex)

        for neighbor in graph[vertex]:

            if neighbor not in visited:

                if dfs(neighbor, vertex):
                    return True

            elif neighbor != parent:
                return True

        return False

    for vertex in graph:

        if vertex not in visited:

            if dfs(vertex, None):
                return True

    return False


# ================= TEST PHẦN A =================

print("=== TEST CYCLE DETECTION - UNDIRECTED ===")

graph1 = {
    0: [1, 2],
    1: [0, 3],
    2: [0, 3],
    3: [1, 2]
}

print("Test 1 (có chu trình):",
      has_cycle_undirected(graph1))

graph2 = {
    0: [1, 2],
    1: [0, 3],
    2: [0],
    3: [1]
}

print("Test 2 (không có chu trình):",
      has_cycle_undirected(graph2))

graph3 = {
    0: [1],
    1: [0],
    2: [3, 4],
    3: [2, 4],
    4: [2, 3]
}

print("Test 3 (nhiều component, có chu trình):",
      has_cycle_undirected(graph3))

# PHẦN B - PHÁT HIỆN CHU TRÌNH ĐỒ THỊ CÓ HƯỚNG


def has_cycle_directed(graph):
    """
    Cycle Detection cho đồ thị có hướng.

    Three Color Approach

    WHITE = chưa thăm
    GRAY  = đang xử lý
    BLACK = đã xử lý xong

    Nếu gặp GRAY -> có chu trình
    """

    WHITE = 0
    GRAY = 1
    BLACK = 2

    color = {
        vertex: WHITE
        for vertex in graph
    }

    def dfs(vertex):

        color[vertex] = GRAY

        for neighbor in graph[vertex]:

            if color[neighbor] == GRAY:
                return True

            if color[neighbor] == WHITE:

                if dfs(neighbor):
                    return True

        color[vertex] = BLACK

        return False

    for vertex in graph:

        if color[vertex] == WHITE:

            if dfs(vertex):
                return True

    return False


# ================= TEST PHẦN B =================

print("\n=== TEST CYCLE DETECTION - DIRECTED ===")

graph1 = {
    'A': ['B'],
    'B': ['C'],
    'C': ['A']
}

print("Test 1 (A→B→C→A):",
      has_cycle_directed(graph1))

graph2 = {
    'A': ['B', 'C'],
    'B': ['D'],
    'C': ['D'],
    'D': []
}

print("Test 2 (DAG):",
      has_cycle_directed(graph2))

graph3 = {
    'A': ['B'],
    'B': ['C'],
    'C': [],
    'D': ['C']
}

print("Test 3 (cross edge):",
      has_cycle_directed(graph3))

# PHẦN C - SO SÁNH HAI PHƯƠNG PHÁP


def compare_cycle_detection():

    print("\n" + "=" * 60)
    print("SO SÁNH CYCLE DETECTION")
    print("=" * 60)

    print("\n[1] ĐỒ THỊ VÔ HƯỚNG")

    undirected = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C']
    }

    print("Đồ thị:", undirected)
    print("Có chu trình:",
          has_cycle_undirected(undirected))

    print("\n[2] ĐỒ THỊ CÓ HƯỚNG")

    directed = {
        'A': ['B'],
        'B': ['C'],
        'C': ['D'],
        'D': ['B']
    }

    print("Đồ thị:", directed)
    print("Có chu trình:",
          has_cycle_directed(directed))

    print("\n[3] SO SÁNH")

    print("Vô hướng:")
    print("- DFS + Parent")
    print("- Nếu gặp visited và khác parent => cycle")

    print("\nCó hướng:")
    print("- DFS + Three Color")
    print("- Gặp đỉnh GRAY => cycle")

    print("\nĐộ phức tạp:")
    print("Time: O(V + E)")
    print("Space: O(V)")


compare_cycle_detection()