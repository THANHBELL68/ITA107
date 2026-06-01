# ==============================================================================
# Bài 1 – Backtracking cơ bản
# File: lab3_bai1.py
# ==============================================================================

# ------------------------------------------------------------------------------
# Hàm 1 – Tìm tất cả hoán vị (Permutations)
# ------------------------------------------------------------------------------
def permutations(nums):
    """
    Tìm tất cả hoán vị của danh sách nums bằng thuật toán Quay lui (Backtracking).
    
    - Base case: len(path) == len(nums) -> Đã chọn đủ số lượng phần tử. 
                 Tiến hành sao chép cấu trúc qua path.copy() và lưu vào result.
    - Recursive case: Duyệt qua danh sách các phần tử chưa dùng (`remaining`). 
                      Thực hiện CHOOSE phần tử hiện tại, gộp các phần tử còn lại 
                      để EXPLORE, sau đó UNCHOOSE bằng cách pop() để quay lui.
    - Độ phức tạp Big-O:
        + Thời gian: O(N! * N) - Có N! cấu trúc hoán vị, mỗi lần lưu cấu trúc mất O(N) để copy.
        + Không gian: O(N) - Độ sâu tối đa của Call Stack đệ quy là N.
    """
    result = []
     
    def backtrack(path, remaining):
        # Base case: Đã chọn đủ n số 
        if len(path) == len(nums): 
            result.append(path.copy())  # QUAN TRỌNG: phải copy để tránh lỗi tham chiếu!
            return 
         
        # Thử từng số còn lại 
        for i in range(len(remaining)): 
            # CHOOSE: Chọn remaining[i] 
            path.append(remaining[i]) 
             
            # EXPLORE: Đệ quy với các số còn lại (bỏ số vừa chọn bằng slice) 
            new_remaining = remaining[:i] + remaining[i+1:] 
            backtrack(path, new_remaining) 
             
            # UNCHOOSE: Quay lui 
            path.pop() 
     
    backtrack([], nums)
    return result 


# ------------------------------------------------------------------------------
# Hàm 2 – Tìm tất cả tổ hợp (Combinations)
# ------------------------------------------------------------------------------
def combinations(nums, k):
    """
    Tìm tất cả tổ hợp chập k phần tử từ danh sách nums.
    
    - Base case: len(path) == k -> Tập hợp hiện tại đã thu thập đủ k phần tử. 
                 Sao chép dữ liệu và lưu vào danh sách kết quả.
    - Recursive case: Lặp qua các phần tử từ vị trí `start` đến cuối chuỗi. 
                      CHOOSE phần tử, EXPLORE sâu xuống với vị trí tiếp theo `i + 1` 
                      để loại bỏ việc lấy trùng chéo, cuối cùng UNCHOOSE (pop).
    - Độ phức tạp Big-O:
        + Thời gian: O(C(n, k) * k) - Dựa vào tổ hợp chập k của n phần tử.
        + Không gian: O(k) - Chiều sâu tối đa của Call Stack đệ quy được giới hạn bởi k.
    """
    result = []
     
    def backtrack(start, path): 
        # Base case: Đã chọn đủ k phần tử 
        if len(path) == k: 
            result.append(path.copy()) 
            return 
         
        # Thử các số từ vị trí start trở đi 
        for i in range(start, len(nums)): 
            # CHOOSE 
            path.append(nums[i]) 
             
            # EXPLORE: Chỉ xét các số sau i (i+1) -> tránh trùng lặp thứ tự
            backtrack(i + 1, path) 
             
            # UNCHOOSE 
            path.pop() 
     
    backtrack(0, []) 
    return result 


# ------------------------------------------------------------------------------
# Hàm 3 – Tìm tất cả tập con (Subsets)
# ------------------------------------------------------------------------------
def subsets(nums):
    """
    Tìm toàn bộ các tập con (Power Set) của danh sách nums.
    
    - Base case: Không có điều kiện ngắt rõ ràng. Đệ quy sẽ tự kết thúc khi vòng 
                 lặp chạy vượt qua kích thước danh sách (start >= len(nums)).
    - Recursive case: Mỗi lần hàm được kích hoạt, ta ghi nhận ngay trạng thái của `path`. 
                      Vòng lặp tiếp tục thực hiện CHOOSE -> EXPLORE (i + 1) -> UNCHOOSE.
    - Độ phức tạp Big-O:
        + Thời gian: O(2^n * n) - Có 2^n tập con, quá trình nhân bản dữ liệu mất O(n).
        + Không gian: O(n) - Chiều sâu của bộ nhớ stack đệ quy.
    """
    result = []
     
    def backtrack(start, path): 
        # Lưu tất cả tập con (ghi nhận mọi nút/trạng thái đi qua trên cây quyết định)
        result.append(path.copy()) 
         
        # Thử thêm các phần tử từ start 
        for i in range(start, len(nums)): 
            # CHOOSE 
            path.append(nums[i]) 
             
            # EXPLORE 
            backtrack(i + 1, path) 
             
            # UNCHOOSE 
            path.pop() 
     
    backtrack(0, []) 
    return result 


# ------------------------------------------------------------------------------
# Hàm 4 – In tất cả chuỗi nhị phân độ dài n
# ------------------------------------------------------------------------------
def binary_strings(n):
    """
    Tìm mọi chuỗi cấu tạo nhị phân từ các ký tự '0' và '1' có chiều dài n.
    
    - Base case: len(path) == n -> Đã ráp đủ n ký tự, thực hiện ''.join(path) 
                 để chuyển đổi từ mảng thành chuỗi rồi lưu lại, sau đó ngắt nhánh đệ quy.
    - Recursive case: Lựa chọn cố định tại mỗi bước chỉ nằm trong danh mục ['0', '1']. 
                      Thực hiện CHOOSE ký tự -> EXPLORE tầng tiếp theo -> UNCHOOSE (pop).
    - Độ phức tạp Big-O:
        + Thời gian: O(2^n * n) - Khởi tạo tổng cộng 2^n cấu trúc chuỗi nhị phân.
        + Không gian: O(n) - Bộ nhớ stack đệ quy lưu trữ.
    """
    result = [] 
    
    def backtrack(path): 
        # Base case: Đủ n ký tự 
        if len(path) == n: 
            result.append(''.join(path)) 
            return 
         
        # Thử cả '0' và '1' 
        for choice in ['0', '1']: 
            # CHOOSE 
            path.append(choice) 
             
            # EXPLORE 
            backtrack(path) 
             
            # UNCHOOSE 
            path.pop() 
     
    backtrack([]) 
    return result 


# ==============================================================================
# KHU VỰC CHẠY THỬ VÀ KIỂM TRA (TEST CASES)
# ==============================================================================
if __name__ == "__main__":

    # --- Test Hàm 1: Permutations ---
    print("=== Test Permutations ===") 
    result_perm1 = permutations([1, 2, 3]) 
    print(f"Hoán vị của [1,2,3]: {result_perm1}") 
    print(f"Số hoán vị: {len(result_perm1)}")  # Kỳ vọng: 6
     
    result_perm2 = permutations([1, 2]) 
    print(f"Hoán vị của [1,2]: {result_perm2}") 
    print(f"Số hoán vị: {len(result_perm2)}")  # Kỳ vọng: 2
    print("-" * 50)

    # --- Test Hàm 2: Combinations ---
    print("=== Test Combinations ===") 
    result_comb1 = combinations([1, 2, 3, 4], 2) 
    print(f"Tổ hợp chập 2 từ [1,2,3,4]: {result_comb1}") 
    print(f"Số tổ hợp: {len(result_comb1)}")  # Kỳ vọng: 6
     
    result_comb2 = combinations([1, 2, 3], 2) 
    print(f"Tổ hợp chập 2 từ [1,2,3]: {result_comb2}") 
    print(f"Số tổ hợp: {len(result_comb2)}")  # Kỳ vọng: 3
    print("-" * 50)

    # --- Test Hàm 3: Subsets ---
    print("=== Test Subsets ===") 
    result_sub1 = subsets([1, 2, 3]) 
    print(f"Tập con của [1,2,3]: {result_sub1}") 
    print(f"Số tập con: {len(result_sub1)}")  # Kỳ vọng: 8
     
    result_sub2 = subsets([1, 2]) 
    print(f"Tập con của [1,2]: {result_sub2}") 
    print(f"Số tập con: {len(result_sub2)}")  # Kỳ vọng: 4
    print("-" * 50)

    # --- Test Hàm 4: Binary Strings ---
    print("=== Test Binary Strings ===") 
    result_bin1 = binary_strings(3) 
    print(f"Chuỗi nhị phân độ dài 3: {result_bin1}") 
    print(f"Số chuỗi: {len(result_bin1)}")  # Kỳ vọng: 8
     
    result_bin2 = binary_strings(2) 
    print(f"Chuỗi nhị phân độ dài 2: {result_bin2}") 
    print(f"Số chuỗi: {len(result_bin2)}")  # Kỳ vọng: 4
    print("=" * 50)