# Bài 2 – Tối ưu Fibonacci với memoization

# ==============================================================================

import time

# ------------------------------------------------------------------------------
# Phần A – Fibonacci đệ quy đơn giản (Naive)
# ------------------------------------------------------------------------------
def fibonacci_naive(n):
    """
    Fibonacci đệ quy đơn giản - CHẬM
    F(n) = F(n-1) + F(n-2)
    F(0) = 0, F(1) = 1
    
    - Base case: n <= 1 (trả về n)
    - Recursive case: fibonacci_naive(n - 1) + fibonacci_naive(n - 2)
    - Độ phức tạp Big-O: 
        + Thời gian: O(2^n) - Cực kỳ chậm do tính trùng lặp các nhánh cây đệ quy.
        + Không gian: O(n) - Do chiều sâu của Call Stack.
    """
    if n <= 1:
        return n
    return fibonacci_naive(n - 1) + fibonacci_naive(n - 2)


# ------------------------------------------------------------------------------
# Phần B – Fibonacci với memoization (Top-down Dynamic Programming)
# ------------------------------------------------------------------------------
def fibonacci_memo(n, memo=None):
    """
    Fibonacci với memoization - NHANH
    
    - Kiểm tra bộ nhớ đệm: Nếu kết quả của n đã nằm trong `memo`, trả về ngay lập tức.
    - Base case: n <= 1 (lưu vào memo rồi trả về n)
    - Recursive case: Tính fibonacci_memo(n-1) + fibonacci_memo(n-2), 
                      sau đó lưu vào memo[n] trước khi trả về.
    - Độ phức tạp Big-O: 
        + Thời gian: O(n) - Vì mỗi bài toán con chỉ cần tính toán duy nhất một lần.
        + Không gian: O(n) - Cần bộ nhớ lưu dictionary `memo` kích thước n và Call Stack.
    """
    # Khởi tạo memo nếu chưa có
    if memo is None:
        memo = {}
     
    # Bước 1: Kiểm tra xem n đã có trong memo chưa
    if n in memo: 
        return memo[n] 
     
    # Bước 2: Base case 
    if n <= 1: 
        memo[n] = n 
        return memo[n] 
     
    # Bước 3: Recursive case (Hoàn thành phần tự viết)
    memo[n] = fibonacci_memo(n - 1, memo) + fibonacci_memo(n - 2, memo) 
    return memo[n]


# ------------------------------------------------------------------------------
# Phần C – Fibonacci vòng lặp (Iterative - Bottom-up)
# ------------------------------------------------------------------------------
def fibonacci_iterative(n):
    """
    Fibonacci sử dụng vòng lặp (Không dùng đệ quy) - TỐI ƯU KHÔNG GIAN
    
    - Cách xử lý: Sử dụng 2 biến `prev` và `curr` để cuộn chiếu liên tiếp các kết quả 
                  bài toán con mà không cần lưu lại toàn bộ mảng hay gọi stack đệ quy.
    - Độ phức tạp Big-O: 
        + Thời gian: O(n) - Chạy qua duy nhất một vòng lặp từ 2 tới n.
        + Không gian: O(1) - Bộ nhớ cố định, không tốn thêm không gian lưu trữ.
    """
    if n <= 1:
        return n
        
    prev = 0  # Đại diện cho F(0)
    curr = 1  # Đại diện cho F(1)
    
    # Lặp từ 2 đến n để cập nhật các giá trị tiếp theo
    for _ in range(2, n + 1):
        next_fib = prev + curr
        prev = curr
        curr = next_fib
        
    return curr


# ==============================================================================
# KHU VỰC CHẠY THỬ VÀ SO SÁNH HIỆU SUẤT
# ==============================================================================
if __name__ == "__main__":
    print("--- Test cơ bản ---")
    print("Fibonacci naive:") 
    print(f"F(10) = {fibonacci_naive(10)}")  
    print(f"F(20) = {fibonacci_naive(20)}")  
    
    # Test và so sánh thời gian 
    print("\n--- So sánh hiệu suất ---") 
     
    # 1. Đo thời gian bản Naive (Đệ quy thuần)
    start = time.time() 
    result1 = fibonacci_naive(30)  
    time1 = time.time() - start 
    print(f"Naive F(30)       = {result1}, thời gian: {time1:.4f}s") 
     
    # 2. Đo thời gian bản Memoization (Đệ quy có nhớ)
    start = time.time() 
    result2 = fibonacci_memo(100)  
    time2 = time.time() - start 
    print(f"Memo F(100)       = {result2}, thời gian: {time2:.6f}s") 
    
    # 3. Đo thời gian bản Iterative (Vòng lặp)
    start = time
    
    # ============================================