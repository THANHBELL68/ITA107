# ==================================================
# LAB 6 - BÀI 2
# UNION FIND (DISJOINT SET UNION)
# ==================================================

# ==================================================
# PHẦN A - DSU BASIC
# ==================================================

def make_set(vertices):
    """
    Khởi tạo mỗi đỉnh là một tập riêng.
    """

    parent = {}

    for v in vertices:
        parent[v] = v

    return parent


def find(parent, v):
    """
    Tìm root của v.
    """

    while parent[v] != v:
        v = parent[v]

    return v


def union(parent, a, b):
    """
    Gộp hai tập hợp.
    """

    root_a = find(parent, a)

    root_b = find(parent, b)

    if root_a != root_b:
        parent[root_b] = root_a


def demo_dsu_basic():

    print("=== DSU BASIC ===")

    vertices = ['A', 'B', 'C', 'D', 'E']

    parent = make_set(vertices)

    ops = [
        ("union", 'A', 'B'),
        ("union", 'C', 'D'),
        ("find", 'B'),
        ("union", 'B', 'C'),
        ("find", 'D'),
        ("find", 'E')
    ]

    for op in ops:

        if op[0] == "union":

            _, x, y = op

            print(f"\nunion({x}, {y})")

            union(parent, x, y)

        else:

            _, x = op

            root = find(parent, x)

            print(f"\nfind({x}) = {root}")

        print("parent =", parent)


# ==================================================
# PHẦN B - DSU OPTIMIZED
# ==================================================

def make_set_optimized(vertices):
    """
    Khởi tạo DSU tối ưu.
    """

    parent = {}

    size = {}

    for v in vertices:
        parent[v] = v
        size[v] = 1

    return parent, size


def find_optimized(parent, v):
    """
    Path Compression.
    """

    if parent[v] != v:

        parent[v] = find_optimized(
            parent,
            parent[v]
        )

    return parent[v]


def union_optimized(parent, size, a, b):
    """
    Union By Size.
    """

    root_a = find_optimized(parent, a)

    root_b = find_optimized(parent, b)

    if root_a == root_b:
        return

    if size[root_a] < size[root_b]:
        root_a, root_b = root_b, root_a

    parent[root_b] = root_a

    size[root_a] += size[root_b]


def demo_dsu_optimized():

    print("\n=== DSU OPTIMIZED ===")

    vertices = ['A', 'B', 'C', 'D', 'E']

    parent, size = make_set_optimized(
        vertices
    )

    union_optimized(parent, size, 'A', 'B')
    union_optimized(parent, size, 'B', 'C')
    union_optimized(parent, size, 'D', 'E')
    union_optimized(parent, size, 'A', 'D')

    print("Parent trước find:")
    print(parent)

    print("\nfind(E) =", find_optimized(parent, 'E'))

    print("\nParent sau find:")
    print(parent)

    print("\nSize:")
    print(size)



# PHẦN C - SO SÁNH BASIC VS OPTIMIZED


def find_with_steps(parent, v):

    steps = 0

    while parent[v] != v:

        v = parent[v]

        steps += 1

    return v, steps


def compare_basic_vs_optimized():

    print("\n=== SO SÁNH BASIC VS OPTIMIZED ===")

    n = 10

    vertices = list(range(n))

    # -------------------
    # BASIC
    # -------------------

    parent_basic = make_set(vertices)

    for i in range(n - 1):
        union(
            parent_basic,
            i,
            i + 1
        )

    total_steps_basic = 0

    for _ in range(20):

        _, steps = find_with_steps(
            parent_basic,
            n - 1
        )

        total_steps_basic += steps

    # -------------------
    # OPTIMIZED
    # -------------------

    parent_opt, size_opt = \
        make_set_optimized(vertices)

    for i in range(n - 1):

        union_optimized(
            parent_opt,
            size_opt,
            i,
            i + 1
        )

    for _ in range(20):
        find_optimized(
            parent_opt,
            n - 1
        )

    _, steps_opt = find_with_steps(
        parent_opt,
        n - 1
    )

    print("\nBasic:")
    print("Parent =", parent_basic)
    print(
        "Tổng số bước sau 20 lần find:",
        total_steps_basic
    )

    print("\nOptimized:")
    print("Parent =", parent_opt)
    print(
        "Số bước sau path compression:",
        steps_opt
    )


# MAIN


if __name__ == "__main__":

    demo_dsu_basic()

    demo_dsu_optimized()

    compare_basic_vs_optimized()