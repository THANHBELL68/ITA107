# ==============================================================================
# Bài 3 – Matching Problems & Performance Analysis
# File: lab4_bai3.py
# ==============================================================================

import time
import random
import matplotlib.pyplot as plt

# ------------------------------------------------------------------------------
# Phần A – Assign Cookies (Phân phối bánh quy - LeetCode 455)
# ------------------------------------------------------------------------------
def find_content_children(greed, cookies): 
    """ 
    Tìm số trẻ tối đa có thể thỏa mãn điều kiện ăn bánh.
    
    - Chiến lược Greedy: Sắp xếp cả hai danh sách theo chiều tăng dần. Sử dụng 
      kỹ thuật Hai con trỏ (Two Pointers) để duyệt qua từng mảng. Luôn ưu tiên 
      lấy chiếc bánh quy nhỏ nhất đủ điều kiện để đáp ứng cho đứa trẻ ít tham lam nhất.
    - Độ phức tạp Big-O:
        + Thời gian: O(N log N + M log M) với N là số trẻ, M là số bánh quy (do bước sort).
        + Không gian: O(1) hoặc O(N+M) tùy thuộc vào thuật toán sort nội tại của Python.
    """ 
    # Bước 1: Sắp xếp cả 2 mảng tăng dần
    greed.sort()
    cookies.sort()
    
    child_ptr = 0  # Con trỏ đại diện cho danh sách trẻ em
    cookie_ptr = 0 # Con trỏ đại diện cho danh sách bánh quy
    
    # Bước 2: Dùng 2 con trỏ đồng thời duyệt qua hai mảng
    while child_ptr < len(greed) and cookie_ptr < len(cookies):
        # Nếu kích thước bánh đủ đáp ứng độ tham lam của trẻ
        if cookies[cookie_ptr] >= greed[child_ptr]:
            # Đứa trẻ đã được thỏa mãn, dịch chuyển con trỏ sang đứa trẻ tiếp theo
            child_ptr += 1
            
        # Trong mọi trường hợp, chiếc bánh hiện tại đã được xét duyệt (hoặc đã ăn, hoặc quá nhỏ bỏ qua)
        cookie_ptr += 1
        
    # Bước 3: Số trẻ được thỏa mãn chính là vị trí dừng của con trỏ child_ptr
    return child_ptr


# ------------------------------------------------------------------------------
# Phần B – Assign Bikes (Phân phối xe đạp)
# ------------------------------------------------------------------------------
def manhattan_distance(p1, p2): 
    """Tính khoảng cách Manhattan giữa 2 tọa độ (x1, y1) và (x2, y2)"""
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1]) 


def assign_bikes(workers, bikes):
    """
    Ghép mỗi worker với 1 bike sao cho tổng khoảng cách Manhattan nhỏ nhất theo Greedy.
    
    - Chiến lược Greedy: 
      1. Tính tất cả các khoảng cách có thể có giữa mọi cặp (worker, bike).
      2. Sắp xếp danh sách các cặp này theo thứ tự khoảng cách tăng dần.
      3. Duyệt danh sách đã sort, ưu tiên chọn các cặp có khoảng cách ngắn nhất, 
         với điều kiện cả worker và bike trong cặp đó đều chưa được phân phối.
    - Chú ý: Đây là cách giải tiếp cận Tham lam (Greedy), cho tốc độ xử lý nhanh, 
      tuy nhiên nó mang tính chất xấp xỉ (gần đúng) chứ không đảm bảo tối ưu toàn cục 
      100% trong mọi cấu hình phức tạp (muốn tối ưu tuyệt đối phải dùng thuật toán Hungary hoặc DP).
    """
    # 1. Tính tất cả khoảng cách Manhattan và lưu kèm index của worker và bike
    all_distances = []
    for w_idx, worker in enumerate(workers):
        for b_idx, bike in enumerate(bikes):
            dist = manhattan_distance(worker, bike)
            all_distances.append((dist, w_idx, b_idx))
            
    # 2. Sắp xếp danh sách theo khoảng cách tăng dần. 
    # Nếu khoảng cách bằng nhau, Python tự so sánh index của worker và bike (đảm bảo tính ổn định)
    all_distances.sort(key=lambda x: x[0])
    
    # Khởi tạo mảng đánh dấu trạng thái đã sử dụng
    assigned_workers = set()
    assigned_bikes = set()
    
    total_distance = 0
    pairs_matched = [] # Lưu chi tiết kết quả ghép cặp (worker_id, bike_id)
    
    # 3. Greedy chọn cặp gần nhất chưa dùng 
    for dist, w_idx, b_idx in all_distances:
        # Nếu cả worker và bike này đều chưa có chủ/chưa được giao xe
        if w_idx not in assigned_workers and b_idx not in assigned_bikes:
            assigned_workers.add(w_idx)
            assigned_bikes.add(b_idx)
            total_distance += dist
            pairs_matched.append((w_idx, b_idx))
            
            # Nếu đã ghép đủ cho tất cả workers thì dừng sớm
            if len(assigned_workers) == len(workers):
                break
                
    return total_distance, pairs_matched


# ------------------------------------------------------------------------------
# Phần C – Performance Analysis (Phân tích & Đo lường hiệu suất thực tế)
# ------------------------------------------------------------------------------
def generate_test_data(n): 
    """Tạo dữ liệu tọa độ ngẫu nhiên trong không gian ma trận 1000x1000 cho n đối tượng""" 
    points = [] 
    for _ in range(n): 
        x = random.randint(0, 1000) 
        y = random.randint(0, 1000) 
        points.append((x, y)) 
    return points 


def benchmark_matching_problems(sizes): 
    """Đo lường sự biến thiên thời gian thực thi của thuật toán Assign Bikes với các size khác nhau""" 
    times = [] 
    print(f"\n{'='*50}")
    print(" TIẾN HÀNH ĐO THỜI GIAN CHẠY THỰC TẾ (BENCHMARK)")
    print(f"{'='*50}")
    
    for size in sizes: 
        # Sinh dữ liệu ngẫu nhiên cho số lượng worker và bike bằng nhau
        workers = generate_test_data(size) 
        bikes = generate_test_data(size) 
         
        start = time.time() 
        assign_bikes(workers, bikes) 
        elapsed = time.time() - start 
        
        times.append(elapsed) 
        print(f" -> Kích thước dữ liệu N = {size:5d}: Thời gian xử lý = {elapsed:.6f} giây") 
        
    return times 


def draw_performance_chart(sizes, times):
    """Vẽ biểu đồ đường biểu diễn mối tương quan giữa kích thước đầu vào và thời gian chạy"""
    plt.figure(figsize=(9, 5))
    plt.plot(sizes, times, marker='o', linestyle='-', color='b', linewidth=2, label='Greedy Assign Bikes')
    
    # Thiết lập tiêu đề và các nhãn trục cho biểu đồ
    plt.title("Biểu Đồ Phân Tích Hiệu Năng Thuật Toán Greedy Assign Bikes", fontsize=14, fontweight='bold', pad=15)
    plt.xlabel("Kích thước dữ liệu (Kích thước mảng N)", fontsize=11)
    plt.ylabel("Thời gian thực thi (Giây)", fontsize=11)
    
    # Hiển thị lưới tọa độ nền để dễ quan sát số liệu
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()
    
    # Hiển thị giá trị cụ thể tại các điểm nút dữ liệu lớn
    for x, y in zip(sizes, times):
        plt.annotate(f"{y:.4f}s", (x, y), textcoords="offset points", xytext=(0,10), ha='center', fontsize=9)
        
    plt.tight_layout()
    print("\n[Hệ thống]: Đang khởi tạo và hiển thị biểu đồ...")
    plt.show()


# ==============================================================================
# KHU VỰC CHẠY THỬ TOÀN DIỆN (MAIN)
# ==============================================================================
if __name__ == "__main__":
    
    # 1. Kiểm thử phần A: Assign Cookies
    print("=== TEST PHẦN A: ASSIGN COOKIES ===")
    g1, c1 = [1, 2, 3], [1, 1]
    print(f"Test 1 - Độ tham: {g1}, Bánh: {c1} -> Trẻ thỏa mãn: {find_content_children(g1, c1)}") # Kỳ vọng: 1
    
    g2, c2 = [1, 2], [1, 2, 3]
    print(f"Test 2 - Độ tham: {g2}, Bánh: {c2} -> Trẻ thỏa mãn: {find_content_children(g2, c2)}") # Kỳ vọng: 2
    print("-" * 50)

    # 2. Kiểm thử phần B: Assign Bikes
    print("=== TEST PHẦN B: ASSIGN BIKES ===")
    # Toà độ người làm việc và xe đạp trên mặt phẳng tọa độ
    workers_test = [(0, 0), (2, 1)]
    bikes_test = [(1, 2), (3, 3)]
    
    total_dist, matched_pairs = assign_bikes(workers_test, bikes_test)
    print(f"Vị trí Workers: {workers_test}")
    print(f"Vị trí Bikes  : {bikes_test}")
    print(f" => Tổng khoảng cách ngắn nhất (Tham lam): {total_dist}")
    print(f" => Chi tiết các cặp được ghép (worker_id, bike_id): {matched_pairs}")
    print("-" * 50)

    # 3. Kiểm thử phần C: Chạy phân tích Benchmark và vẽ biểu đồ hiệu năng
    # Thiết lập các mốc kích thước để thử nghiệm, bao gồm cả mốc N = 1000 theo yêu cầu
    test_sizes = [100, 300, 500, 800, 1000]
    execution_times = benchmark_matching_problems(test_sizes)
    
    # Kích hoạt vẽ đồ thị trực quan hóa dữ liệu
    draw_performance_chart(test_sizes, execution_times)