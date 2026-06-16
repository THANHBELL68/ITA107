from collections import deque

# HÀM KIỂM TRA CHU TRÌNH ĐỒ THỊ CÓ HƯỚNG


def has_cycle_directed(graph):

    WHITE, GRAY, BLACK = 0, 1, 2

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

# PHẦN A - TOPOLOGICAL SORT BẰNG DFS


def topological_sort_dfs(graph):
    """
    Topological Sort sử dụng DFS Post-order

    Return:
        List topo order
        hoặc None nếu có chu trình
    """

    if has_cycle_directed(graph):
        return None

    visited = set()

    stack = []

    def dfs(vertex):

        visited.add(vertex)

        for neighbor in graph[vertex]:

            if neighbor not in visited:
                dfs(neighbor)

        # Post-order
        stack.append(vertex)

    for vertex in graph:

        if vertex not in visited:
            dfs(vertex)

    return stack[::-1]



# TEST TOPO DFS


print("=== TOPOLOGICAL SORT DFS ===")

graph_dfs = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}

print(topological_sort_dfs(graph_dfs))



# PHẦN B - KAHN'S ALGORITHM


def topological_sort_kahn(graph):
    """
    Topological Sort bằng Kahn's Algorithm

    Return:
        List topo order
        hoặc None nếu có chu trình
    """

    in_degree = {
        vertex: 0
        for vertex in graph
    }

    # Tính in-degree
    for vertex in graph:

        for neighbor in graph[vertex]:

            in_degree[neighbor] += 1

    queue = deque()

    for vertex in graph:

        if in_degree[vertex] == 0:
            queue.append(vertex)

    result = []

    while queue:

        vertex = queue.popleft()

        result.append(vertex)

        for neighbor in graph[vertex]:

            in_degree[neighbor] -= 1

            if in_degree[neighbor] == 0:
                queue.append(neighbor)

    if len(result) != len(graph):
        return None

    return result



# TEST KAHN


print("\n=== TOPOLOGICAL SORT KAHN ===")

graph_kahn = {
    'A': ['C'],
    'B': ['C', 'D'],
    'C': ['E'],
    'D': ['F'],
    'E': ['H', 'F'],
    'F': ['G'],
    'G': [],
    'H': []
}

print(topological_sort_kahn(graph_kahn))



# PHẦN C - COURSE SCHEDULE


def can_finish(num_courses, prerequisites):
    """
    Course Schedule I

    True:
        Có thể học hết

    False:
        Có chu trình
    """

    graph = {
        i: []
        for i in range(num_courses)
    }

    for course, prereq in prerequisites:
        graph[prereq].append(course)

    return not has_cycle_directed(graph)



# COURSE SCHEDULE II


def find_order(num_courses, prerequisites):
    """
    Trả về thứ tự học hợp lệ

    Nếu có chu trình:
        return []
    """

    graph = {
        i: []
        for i in range(num_courses)
    }

    for course, prereq in prerequisites:
        graph[prereq].append(course)

    order = topological_sort_kahn(graph)

    if order is None:
        return []

    return order



# TEST COURSE SCHEDULE


print("\n=== TEST COURSE SCHEDULE ===")

n1 = 4

prereqs1 = [
    [1, 0],
    [2, 0],
    [3, 1],
    [3, 2]
]

print("Test 1:")
print("Can Finish:", can_finish(n1, prereqs1))
print("Order:", find_order(n1, prereqs1))

n2 = 2

prereqs2 = [
    [1, 0],
    [0, 1]
]

print("\nTest 2:")
print("Can Finish:", can_finish(n2, prereqs2))
print("Order:", find_order(n2, prereqs2))