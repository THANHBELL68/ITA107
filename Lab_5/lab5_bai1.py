from collections import deque

# HÀM 1: XÂY DỰNG ĐỒ THỊ TỪ DANH SÁCH CẠNH


def build_graph(edges, directed=False):
    """
    Xây dựng đồ thị từ danh sách cạnh.

    Input:
        edges: Danh sách các cạnh dạng (u, v)
        directed: True nếu đồ thị có hướng,
                  False nếu đồ thị vô hướng

    Output:
        Dictionary biểu diễn đồ thị
    """

    graph = {}

    for u, v in edges:

        if u not in graph:
            graph[u] = []

        if v not in graph:
            graph[v] = []

        graph[u].append(v)

        if not directed:
            graph[v].append(u)

    return graph


# ================= TEST HÀM 1 =================

print("=== TEST HÀM 1: BUILD GRAPH ===")

edges1 = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('D', 'E')
]

graph1 = build_graph(edges1)

print("\nĐồ thị vô hướng:")
for vertex, neighbors in graph1.items():
    print(f"{vertex}: {neighbors}")

edges2 = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'D'),
    ('D', 'E')
]

graph2 = build_graph(edges2, directed=True)

print("\nĐồ thị có hướng:")
for vertex, neighbors in graph2.items():
    print(f"{vertex}: {neighbors}")


# HÀM 2: BFS


def bfs(graph, start):
    """
    BFS - Breadth First Search

    Duyệt đồ thị theo chiều rộng bằng Queue.

    Input:
        graph: Dictionary biểu diễn đồ thị
        start: Đỉnh bắt đầu

    Output:
        Danh sách thứ tự duyệt BFS
    """

    visited = set()
    queue = deque([start])

    visited.add(start)

    result = []

    while queue:

        vertex = queue.popleft()

        result.append(vertex)

        for neighbor in graph[vertex]:

            if neighbor not in visited:

                visited.add(neighbor)

                queue.append(neighbor)

    return result


# ================= TEST HÀM 2 =================

print("\n=== TEST HÀM 2: BFS ===")

graph_bfs = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

result1 = bfs(graph_bfs, 'A')
print("BFS từ A:", result1)

result2 = bfs(graph_bfs, 'D')
print("BFS từ D:", result2)


# HÀM 3: DFS RECURSIVE


def dfs_recursive(graph, start, visited=None, result=None):
    """
    DFS bằng đệ quy.

    Chiến lược:
    - Đánh dấu đỉnh hiện tại đã thăm
    - Thêm vào kết quả
    - Đệ quy với các đỉnh kề chưa thăm

    Input:
        graph: Dictionary biểu diễn đồ thị
        start: Đỉnh bắt đầu

    Output:
        Danh sách thứ tự duyệt DFS
    """

    if visited is None:
        visited = set()

    if result is None:
        result = []

    visited.add(start)

    result.append(start)

    for neighbor in graph[start]:

        if neighbor not in visited:

            dfs_recursive(
                graph,
                neighbor,
                visited,
                result
            )

    return result


# ================= TEST HÀM 3 =================

print("\n=== TEST HÀM 3: DFS RECURSIVE ===")

graph_dfs = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B', 'F'],
    'F': ['C', 'E']
}

result1 = dfs_recursive(graph_dfs, 'A')
print("DFS từ A:", result1)

result2 = dfs_recursive(graph_dfs, 'C')
print("DFS từ C:", result2)

# HÀM 4: CONNECTED COMPONENTS


def count_connected_components(graph):
    """
    Đếm số thành phần liên thông.

    Chiến lược:
    - Duyệt toàn bộ đỉnh
    - Nếu đỉnh chưa thăm:
        + Chạy BFS
        + Tạo thành 1 component mới

    Output:
        count: số lượng component
        components: danh sách component
    """

    visited = set()

    components = []

    def bfs_component(start):

        queue = deque([start])

        visited.add(start)

        component = []

        while queue:

            vertex = queue.popleft()

            component.append(vertex)

            for neighbor in graph[vertex]:

                if neighbor not in visited:

                    visited.add(neighbor)

                    queue.append(neighbor)

        return component

    for vertex in graph:

        if vertex not in visited:

            component = bfs_component(vertex)

            components.append(component)

    return len(components), components


# ================= TEST HÀM 4 =================

print("\n=== TEST HÀM 4: CONNECTED COMPONENTS ===")

print("\nTest 1: Một component")

graph_cc1 = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A'],
    'D': ['B']
}

count1, comps1 = count_connected_components(graph_cc1)

print("Số components:", count1)

for i, comp in enumerate(comps1, 1):
    print(f"Component {i}: {comp}")

print("\nTest 2: Ba components")

graph_cc2 = {
    'A': ['B'],
    'B': ['A'],
    'C': ['D', 'E'],
    'D': ['C'],
    'E': ['C'],
    'F': []
}

count2, comps2 = count_connected_components(graph_cc2)

print("Số components:", count2)

for i, comp in enumerate(comps2, 1):
    print(f"Component {i}: {comp}")