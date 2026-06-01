# ==============================================================================
# Bài 2 – N-Queens với pruning
# File: lab3_bai2.py
# ==============================================================================

import time

# ------------------------------------------------------------------------------
# Phần A – Hàm kiểm tra hợp lệ & Hàm tiện ích
# ------------------------------------------------------------------------------
def is_safe(board, row, col, n): 
    """ 
    Kiểm tra đặt quân hậu ở (row, col) có bị các quân hậu trước đó tấn công không.
    board: list lưu cột của quân hậu ở mỗi hàng (board[i] = j -> hàng i, cột j).
    """ 
    # Kiểm tra tất cả các hàng trước đó 
    for prev_row in range(row): 
        prev_col = board[prev_row] 
         
        # Kiểm tra trùng cột 
        if prev_col == col: 
            return False 
         
        # Kiểm tra trùng đường chéo: Nếu |row1 - row2| == |col1 - col2| -> cùng đường chéo 
        if abs(prev_row - row) == abs(prev_col - col): 
            return False 
     
    return True 


def check_valid_board(board, n):
    """
    Hàm bổ trợ cho bản No-Pruning: Kiểm tra toàn bộ bàn cờ có hợp lệ không 
    bằng cách duyệt qua tất cả các cặp quân hậu (i, j).
    """
    for i in range(n):
        for j in range(i + 1, n):
            # Nếu trùng cột
            if board[i] == board[j]:
                return False
            # Nếu trùng đường chéo
            if abs(i - j) == abs(board[i] - board[j]):
                return False
    return True


def print_board(solution, n): 
    """ 
    In ma trận bàn cờ N×N trực quan với ký hiệu 'Q' (Queen) và '.' (Ô trống).
    """ 
    for row in range(n): 
        line = "" 
        for col in range(n): 
            if solution[row] == col: 
                line += "Q " 
            else: 
                line += ". " 
        print(line) 
    print() 


# ------------------------------------------------------------------------------
# Bộ đếm hỗ trợ theo dõi hiệu năng
# ------------------------------------------------------------------------------
class Counter: 
    """Class dùng để đếm số lần gọi hàm đệ quy và số lượng đáp án tìm thấy""" 
    def __init__(self): 
        self.total_calls = 0 
        self.solutions = 0 
     
    def report(self): 
        print(f"-> Tổng số lần gọi (Node đệ quy): {self.total_calls}") 
        print(f"-> Số giải pháp hợp lệ tìm được: {self.solutions}") 


# ------------------------------------------------------------------------------
# Phần B – N-Queens không có pruning (Sinh - Kiểm tra sau)
# ------------------------------------------------------------------------------
def solve_n_queens_no_pruning(n): 
    """ 
    N-Queens KHÔNG có pruning: Sinh toàn bộ cấu hình (brute-force) 
    rồi mới kiểm tra tính hợp lệ khi đạt đủ N quân hậu ở Base case.
    
    - Base case: row == n -> Đã đặt đủ n quân hậu. Tiến hành kiểm tra toàn cục bằng check_valid_board().
    - Recursive case: Đẩy thẳng lựa chọn cột `col` vào mảng mà không màng tới va chạm, 
                      sau đó gọi EXPLORE sâu xuống hàng tiếp theo, cuối cùng UNCHOOSE.
    """ 
    counter = Counter() 
    result = [] 
    board = [] 
     
    def backtrack(row): 
        counter.total_calls += 1 
         
        # Base case: Đã đặt đủ n quân hậu trên mọi hàng
        if row == n: 
            # Kiểm tra board có thực sự hợp lệ không (Duyệt tất cả cặp quân hậu)
            if check_valid_board(board, n):
                result.append(board.copy())  # Lưu cấu hình hợp lệ
                counter.solutions += 1 
            return 
         
        # Thử tất cả cột từ 0 đến n-1 (Bỏ qua bước kiểm tra is_safe trước đệ quy)
        for col in range(n): 
            # CHOOSE 
            board.append(col) 
             
            # EXPLORE 
            backtrack(row + 1) 
             
            # UNCHOOSE 
            board.pop() 
     
    backtrack(0) 
    counter.report() 
    return result 


# ------------------------------------------------------------------------------
# Phần C – N-Queens có pruning (Cắt tỉa nhánh sớm)
# ------------------------------------------------------------------------------
def solve_n_queens_with_pruning(n): 
    """ 
    N-Queens CÓ pruning: Kiểm tra va chạm ngay trước khi rẽ nhánh đệ quy.
    Nếu phát hiện xung đột, nhánh đó lập tức bị loại bỏ (chặt cụt cây quyết định).
    
    - Base case: row == n -> Khi chạm được tới đây, cấu hình chắc chắn đã hợp lệ 100%.
    - Recursive case: Duyệt các cột, kiểm tra is_safe(). Chỉ khi an toàn mới CHOOSE -> EXPLORE -> UNCHOOSE.
    """ 
    counter = Counter() 
    result = [] 
    board = [] 
     
    def backtrack(row): 
        counter.total_calls += 1 
         
        # Base case: Chắc chắn hợp lệ khi đi tới cuối cây
        if row == n: 
            result.append(board.copy()) 
            counter.solutions += 1 
            return 
         
        # Duyệt từng cột
        for col in range(n): 
            # PRUNING: Cắt tỉa nhánh bị trùng lặp/bị chặn trước khi lún sâu đệ quy 
            if is_safe(board, row, col, n): 
                # CHOOSE 
                board.append(col) 
                 
                # EXPLORE 
                backtrack(row + 1) 
                 
                # UNCHOOSE 
                board.pop() 
     
    backtrack(0) 
    counter.report() 
    return result 


# ------------------------------------------------------------------------------
# Phần D – So sánh và đánh giá hiệu suất giữa hai thuật toán
# ------------------------------------------------------------------------------
def compare_n_queens(n): 
    print(f"\n{'='*50}") 
    print(f" SO SÁNH N-QUEENS VỚI N = {n}") 
    print(f"{'='*50}") 
     
    # 1. Đo lường hiệu năng bản không có pruning 
    print("\n[1] KHÔNG có pruning (Brute-force):") 
    start = time.time() 
    result1 = solve_n_queens_no_pruning(n) 
    time1 = time.time() - start 
    print(f"Thời gian xử lý: {time1:.6f}s") 
     
    # 2. Đo lường hiệu năng bản có pruning 
    print("\n[2] CÓ pruning (Cắt tỉa nhánh):") 
    start = time.time() 
    result2 = solve_n_queens_with_pruning(n) 
    time2 = time.time() - start 
    print(f"Thời gian xử lý: {time2:.6f}s") 
     
    # 3. Phân tích kết quả tăng trưởng hiệu năng
    speedup = time1 / time2 if time2 > 0 else 1
    print(f"\nTốc độ tối ưu tăng thêm: {speedup:.2f}x") 
     
    # Xuất một giải pháp bàn cờ mẫu ra màn hình
    if len(result2) > 0: 
        print(f"\nMột giải pháp mẫu cho {n}-Queens:") 
        print_board(result2[0], n) 


# ==============================================================================
# KHU VỰC KÍCH HOẠT HỆ THỐNG KIỂM THỬ
# ==============================================================================
if __name__ == "__main__":
    # Đề bài yêu cầu test với n=4 và n=6 (hoặc n=5)
    compare_n_queens(4) 
    compare_n_queens(6)