
# Bài 1 – Viết hàm đệ quy cơ bản
# Hàm 1 – Tính tổng từ 1 đến n

def sum_to_n(n):
    """
    Tính tổng 1 + 2 + ... + n bằng đệ quy.
    
    - Base case: 
        + n == 0: trả về 0
        + n == 1: trả về 1
    - Recursive case: 
        + Trả về n + sum_to_n(n - 1)
    - Độ phức tạp Big-O: O(n)
        + Giải thích: Hàm gọi đệ quy n lần, mỗi lần thực hiện 1 phép cộng.
    """
    # Base case: n = 0 hoặc n = 1
    if n == 0:
        return 0
    if n == 1:
        return 1
     
    # Recursive case: n + sum(1..n-1)
    return n + sum_to_n(n - 1)


# ------------------------------------------------------------------------------
# Hàm 2 – Tính n mũ k (power)
# ------------------------------------------------------------------------------
def power(n, k):
    """
    Tính n^k bằng đệ quy.
    
    - Base case:
        + k == 0: trả về 1 (bất kỳ số nào mũ 0 đều bằng 1)
        + n == 0: trả về 0 (với k > 0, cơ số 0 luôn bằng 0)
    - Recursive case:
        + Trả về n * power(n, k - 1)
    - Độ phức tạp Big-O: O(k)
        + Giải thích: Hàm gọi đệ quy k lần dựa trên số mũ giảm dần.
    """
    # Base case 1: mũ 0
    if k == 0:
        return 1
     
    # Base case 2: cơ số 0
    if n == 0:
        return 0
     
    # Recursive case: n × n^(k-1)
    return n * power(n, k - 1)


# ------------------------------------------------------------------------------
# Hàm 3 – Đảo chuỗi (reverse string)
# ------------------------------------------------------------------------------
def reverse_string(s):
    """
    Đảo ngược một chuỗi bằng đệ quy.
    
    - Base case:
        + len(s) <= 1: trả về chính chuỗi s (chuỗi rỗng hoặc có 1 ký tự)
    - Recursive case:
        + Tách ký tự đầu s[0], gọi đệ quy đảo phần còn lại s[1:] rồi nối lại:
          reverse_string(s[1:]) + s[0]
    - Độ phức tạp Big-O: O(n) (với n là độ dài của chuỗi s)
        + Giải thích: Hàm gọi đệ quy n lần, mỗi lần thực hiện cắt chuỗi và nối chuỗi.
    """
    # Base case: chuỗi rỗng hoặc 1 ký tự
    if len(s) <= 1:
        return s
        
    # Recursive case: đảo phần còn lại + ký tự đầu
    return reverse_string(s[1:]) + s[0]


# ------------------------------------------------------------------------------
# Hàm 4 – Kiểm tra palindrome (đọc xuôi ngược như nhau)
# ------------------------------------------------------------------------------
def is_palindrome(s):
    """
    Kiểm tra một chuỗi có phải là palindrome hay không bằng đệ quy.
    
    - Base case:
        + len(s) <= 1: trả về True (chuỗi rỗng hoặc 1 ký tự luôn là palindrome)
    - Recursive case:
        + So sánh ký tự đầu s[0] và cuối s[-1]:
          Nếu s[0] != s[-1] -> không phải palindrome (False).
          Nếu s[0] == s[-1] -> tiếp tục kiểm tra phần giữa bằng đệ quy: is_palindrome(s[1:-1])
    - Độ phức tạp Big-O: O(n) (với n là độ dài của chuỗi s)
        + Giải thích: Tối đa thực hiện n/2 lần so sánh ký tự đầu-cuối, về mặt tiệm cận vẫn là O(n).
    """
    # Base case: chuỗi rỗng hoặc 1 ký tự
    if len(s) <= 1:
        return True
     
    # So sánh ký tự đầu và cuối
    if s[0] != s[-1]:
        return False
     
    # Recursive case: kiểm tra phần giữa
    return is_palindrome(s[1:-1])


# ==============================================================================
# KHU VỰC CHẠY THỬ VÀ KIỂM TRA (TEST CASES)
# ==========================================================================
if __name__ == "__main__":
    print("--- TEST HÀM 1: sum_to_n ---")
    print(f"sum_to_n(0)   = {sum_to_n(0)}")     
    print(f"sum_to_n(1)   = {sum_to_n(1)}")     
    print(f"sum_to_n(5)   = {sum_to_n(5)}")     
    print(f"sum_to_n(10)  = {sum_to_n(10)}")    
    print(f"sum_to_n(100) = {sum_to_n(100)}")   
    print()

    print("--- TEST HÀM 2: power ---")
    print(f"power(2, 5) = {power(2, 5)}")       
    print(f"power(3, 4) = {power(3, 4)}")       
    print(f"power(5, 0) = {power(5, 0)}")       
    print(f"power(0, 5) = {power(0, 5)}")       
    print()

    print("--- TEST HÀM 3: reverse_string ---")
    print(f"reverse_string('hello')  = '{reverse_string('hello')}'")   
    print(f"reverse_string('python') = '{reverse_string('python')}'")  
    print(f"reverse_string('a')      = '{reverse_string('a')}'")       
    print(f"reverse_string('')       = '{reverse_string('')}'")        
    print()

    print("--- TEST HÀM 4: is_palindrome ---")
    print(f"is_palindrome('racecar') = {is_palindrome('racecar')}")   # Kỳ vọng: True
    print(f"is_palindrome('madam')   = {is_palindrome('madam')}")     # Kỳ vọng: True
    print(f"is_palindrome('hello')   = {is_palindrome('hello')}")     # Kỳ vọng: False
    print(f"is_palindrome('a')       = {is_palindrome('a')}")         # Kỳ vọng: True
    print(f"is_palindrome('')        = {is_palindrome('')}")          # Kỳ vọng: True
    # Sinh viên tự test thêm:
    print(f"is_palindrome('abba')    = {is_palindrome('abba')}")      # Kỳ vọng: True
    print(f"is_palindrome('python')  = {is_palindrome('python')}")    # Kỳ vọng: False
    print(f"is_palindrome('noon')    = {is_palindrome('noon')}")      # Kỳ vọng: True

# ==============================================================================
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
    
    # ==============================================================================
# Bài 3 – Cài đặt Merge Sort hoặc Quick Sort

# LỰA CHỌN A – MERGE SORT (Sắp xếp trộn)
# ------------------------------------------------------------------------------
def merge_sort(arr):
    """
    Sắp xếp mảng bằng thuật toán Merge Sort.
    
    - Base case: len(arr) <= 1 -> Mảng có 0 hoặc 1 phần tử đã tự sắp xếp. Trả về chính nó.
    - Recursive case: 
        + Divide: Chia đôi mảng thành 2 nửa left và right.
        + Conquer: Gọi đệ quy merge_sort() để sắp xếp độc lập từng nửa.
        + Combine: Trộn (merge) 2 nửa đã được sắp xếp thành một mảng hoàn chỉnh.
    - Độ phức tạp Big-O: 
        + Thời gian: O(n log n) trong mọi trường hợp (tốt nhất, trung bình, xấu nhất).
        + Không gian: O(n) do cần bộ nhớ phụ để lưu các mảng con trong quá trình trộn.
    """
    # Base case: mảng 0 hoặc 1 phần tử
    if len(arr) <= 1:
        return arr
     
    # Divide - chia đôi mảng
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]
     
    # Conquer - đệ quy sắp xếp 2 nửa
    left_sorted = merge_sort(left)
    right_sorted = merge_sort(right)
     
    # Combine - trộn 2 nửa đã sắp xếp
    return merge(left_sorted, right_sorted)


def merge(left, right):
    """
    Trộn hai mảng đã được sắp xếp (left và right) thành một mảng sắp xếp duy nhất.
    """
    result = []
    i = j = 0
     
    # So sánh và chọn phần tử nhỏ hơn từ hai mảng
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
     
    # Thêm các phần tử còn lại của mảng left (nếu có)
    result.extend(left[i:])
    
    # Thêm các phần tử còn lại của mảng right (nếu có)
    result.extend(right[j:])
     
    return result


# ------------------------------------------------------------------------------
# LỰA CHỌN B – QUICK SORT (Sắp xếp nhanh)
# ------------------------------------------------------------------------------
def quick_sort(arr):
    """
    Sắp xếp mảng bằng thuật toán Quick Sort (Sử dụng List Comprehension).
    
    - Base case: len(arr) <= 1 -> Trả về chính mảng arr.
    - Recursive case:
        + Chọn một phần tử chốt (pivot), ở đây chọn phần tử ở giữa mảng.
        + Partition: Phân hoạch mảng đầu vào thành 3 danh sách riêng biệt:
            * left: chứa phần tử nhỏ hơn pivot.
            * middle: chứa phần tử bằng pivot.
            * right: chứa phần tử lớn hơn pivot.
        + Đệ quy sắp xếp `left` và `right`, sau đó ghép nối kết quả lại với `middle`.
    - Độ phức tạp Big-O:
        + Thời gian trung bình (Average Case): O(n log n) - Rất nhanh trên thực tế.
        + Thời gian xấu nhất (Worst Case): O(n^2) - Xảy ra khi pivot chọn trúng phần tử cực đại/cực tiểu liên tục.
        + Không gian: O(n) do cách tiếp cận tạo list mới (bản cải tiến In-place sẽ là O(log n)).
    """
    # Base case
    if len(arr) <= 1:
        return arr
        
    # Chọn pivot (chọn phần tử ở vị trí giữa mảng)
    pivot = arr[len(arr) // 2]
     
    # Partition - chia thành 3 phần bằng List Comprehension
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
     
    # Đệ quy và kết hợp (Combine)
    return quick_sort(left) + middle + quick_sort(right)


# ==============================================================================
# KHU VỰC CHẠY THỬ VÀ KIỂM TRA (TEST CASES)
# ==============================================================================
if __name__ == "__main__":
    # Khởi tạo mảng kiểm thử mẫu
    arr_test = [64, 34, 25, 12, 22, 11, 90]
    
    print("--- KIỂM TRA THUẬT TOÁN SẮP XẾP ---")
    print(f"Mảng ban đầu: {arr_test}\n")
    
    # 1. Test Merge Sort
    sorted_merge = merge_sort(arr_test)
    print(f"[Merge Sort] Mảng sau khi sắp xếp: {sorted_merge}")
    
    # 2. Test Quick Sort
    sorted_quick = quick_sort(arr_test)
    print(f"[Quick Sort] Mảng sau khi sắp xếp: {sorted_quick}")
    
    # Kiểm tra tính chính xác của thuật toán
    assert sorted_merge == [11, 12, 22, 25, 34, 64, 90], "Merge Sort chạy sai kết quả!"
    assert sorted_quick == [11, 12, 22, 25, 34, 64, 90], "Quick Sort chạy sai kết quả!"
    print("\n=> Cả hai thuật toán đều đã sắp xếp chính xác!")