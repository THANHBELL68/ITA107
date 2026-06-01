# ==============================================================================
# Bài 2 – Meeting Rooms và so sánh Greedy vs DP
# ==============================================================================

import heapq 
import time 

# ------------------------------------------------------------------------------
# Phần A – Minimum Meeting Rooms (Sử dụng Min-Heap)
# ------------------------------------------------------------------------------
def min_meeting_rooms(meetings): 
    """ 
    Tìm số phòng họp tối thiểu cần thiết để tổ chức tất cả các cuộc họp.
    
    - Chiến lược Greedy: Sắp xếp các cuộc họp theo thời gian bắt đầu (start time).
      Sử dụng một Min-Heap để theo dõi thời gian kết thúc (end time) của các phòng đang dùng.
    - Độ phức tạp Big-O:
        + Thời gian: O(n log n) - Do bước sắp xếp và các thao tác push/pop trên Heap.
        + Không gian: O(n) - Trong trường hợp xấu nhất, Heap cần lưu end time của tất cả cuộc họp.
    """ 
    if not meetings: 
        return 0 
     
    # Bước 1: Sắp xếp các cuộc họp theo thời gian bắt đầu (start time)
    meetings.sort(key=lambda x: x[0]) 
     
    # Khởi tạo một Min-Heap rỗng để lưu trữ thời gian kết thúc của các phòng đang sử dụng
    heap = [] 
     
    # Bước 2: Thêm thời gian kết thúc của cuộc họp đầu tiên (kết thúc sớm nhất sau khi sort) vào heap 
    heapq.heappush(heap, meetings[0][1]) 
     
    # Bước 3: Duyệt qua các cuộc họp còn lại 
    for i in range(1, len(meetings)): 
        start, end = meetings[i] 
         
        # Nếu cuộc họp hiện tại bắt đầu SAU HOẶC ĐÚNG BẰNG thời điểm phòng có cuộc họp kết thúc sớm nhất
        if start >= heap[0]: 
            # Giải phóng/Tái sử dụng phòng họp này (loại bỏ thời gian kết thúc cũ khỏi heap)
            heapq.heappop(heap) 
         
        # Đẩy thời gian kết thúc của cuộc họp hiện tại vào heap 
        # (Nếu tái sử dụng: heap giữ nguyên kích thước. Nếu mở phòng mới: heap tăng kích thước)
        heapq.heappush(heap, end) 
     
    # Số lượng phòng họp tối thiểu cần dùng chính bằng số lượng phần tử còn lại trong heap
    return len(heap) 


# ------------------------------------------------------------------------------
# Hàm bổ trợ: Coin Change Greedy (Từ bài trước để phục vụ Phần B & C)
# ------------------------------------------------------------------------------
def coin_change_greedy(amount, coins): 
    """ Đổi tiền bằng số xu ít nhất theo thuật toán Greedy """
    # Tạo bản sao tránh làm thay đổi mảng gốc và sắp xếp giảm dần
    coins_sorted = sorted(coins, reverse=True)
    count = 0 
    result = [] 
     
    for coin in coins_sorted: 
        while amount >= coin: 
            result.append(coin) 
            amount -= coin 
            count += 1 
     
    if amount == 0: 
        return count, result 
    else: 
        return -1, [] 


# ------------------------------------------------------------------------------
# Phần B – Coin Change với Dynamic Programming (Quy hoạch động)
# ------------------------------------------------------------------------------
def coin_change_dp(amount, coins): 
    """ 
    Đổi tiền bằng số xu ít nhất bằng phương pháp Quy hoạch động (Dynamic Programming).
    Luôn đảm bảo cho ra lời giải tối ưu toàn cục với mọi hệ thống mệnh giá xu.
    
    - dp[i] = số xu ít nhất để đổi số tiền có giá trị là i.
    - Công thức truy hồi: dp[i] = min(dp[i - coin] + 1) với mọi coin <= i.
    - Độ phức tạp Big-O:
        + Thời gian: O(amount * len(coins)) - 2 vòng lặp lồng nhau.
        + Không gian: O(amount) - Mảng dp kích thước amount + 1.
    """ 
    # Bước 1: Khởi tạo mảng dp với giá trị vô cùng (float('inf')), kích thước amount + 1
    dp = [float('inf')] * (amount + 1) 
    dp[0] = 0  # Base case: Cần 0 đồng xu để đổi 0 đồng tiền
     
    # Bước 2: Tính toán dp[i] cho i chạy từ 1 đến amount 
    for i in range(1, amount + 1): 
        for coin in coins: 
            if coin <= i: 
                dp[i] = min(dp[i], dp[i - coin] + 1) 
     
    # Bước 3: Trả về kết quả tối ưu
    if dp[amount] == float('inf'): 
        return -1  # Không thể đổi được số tiền này bằng các mệnh giá xu hiện có
    return dp[amount] 


# ------------------------------------------------------------------------------
# Phần C – So sánh và đo lường hiệu suất (Greedy vs DP)
# ------------------------------------------------------------------------------
def compare_coin_change(amount, coins): 
    print(f"\n{'='*60}") 
    print(f" So sánh Coin Change: amount = {amount}, coins = {coins}") 
    print(f"{'='*60}") 
     
    # 1. Thử nghiệm với Thuật toán Greedy 
    print("\n[1] CHIẾN LƯỢC THAM LAM (GREEDY):") 
    start = time.time() 
    greedy_result, greedy_detail = coin_change_greedy(amount, coins) 
    greedy_time = time.time() - start 
    print(f"  + Kết quả : {greedy_result} xu") 
    print(f"  + Chi tiết : {greedy_detail}") 
    print(f"  + Thời gian: {greedy_time:.6f}s") 
     
    # 2. Thử nghiệm với Thuật toán Dynamic Programming 
    print("\n[2] QUY HOẠCH ĐỘNG (DYNAMIC PROGRAMMING):") 
    start = time.time() 
    dp_result = coin_change_dp(amount, coins) 
    dp_time = time.time() - start 
    print(f"  + Kết quả : {dp_result} xu") 
    print(f"  + Thời gian: {dp_time:.6f}s") 
     
    # 3. Phân tích kết quả thực nghiệm 
    print("\n[3] ĐÁNH GIÁ SO SÁNH:") 
    if greedy_result == dp_result: 
        print("  => Kết quả: Greedy ĐÚNG - cho kết quả tối ưu tương đương DP!") 
    else: 
        print(f"  =>  Kết quả: Greedy SAI - kém tối ưu hơn DP (tốn thêm {greedy_result - dp_result} xu)!") 
    
    speed_ratio = dp_time / greedy_time if greedy_time > 0 else 1
    print(f"  => ⚡ Tốc độ  : Greedy chạy nhanh hơn DP {speed_ratio:.2f} lần") 


# ==============================================================================
# KHU VỰC KÍCH HOẠT KIỂM THỬ (MAIN)
# ==============================================================================
if __name__ == "__main__":
    
    # --- KIỂM THỬ PHẦN A: MIN MEETING ROOMS ---
    print("=== TEST PHẦN A: MINIMUM MEETING ROOMS ===")
    
    # Test case 1: Lịch họp thông thường chồng chéo nhau
    tc1 = [(0, 30), (5, 10), (15, 20)]
    print(f"Test 1 {tc1} -> Số phòng tối thiểu: {min_meeting_rooms(tc1)}") # Kỳ vọng: 2
    
    # Test case 2: Các cuộc họp nối tiếp nhau, không chồng lấp
    tc2 = [(1, 3), (3, 6), (6, 9)]
    print(f"Test 2 {tc2} -> Số phòng tối thiểu: {min_meeting_rooms(tc2)}") # Kỳ vọng: 1
    
    # Test case 3: Tất cả cuộc họp diễn ra đồng thời
    tc3 = [(1, 5), (2, 6), (3, 7), (4, 8)]
    print(f"Test 3 {tc3} -> Số phòng tối thiểu: {min_meeting_rooms(tc3)}") # Kỳ vọng: 4
    
    # --- KIỂM THỬ PHẦN B & C: COIN CHANGE COMPARISON ---
    # Test với hệ tiền chuẩn (Greedy đúng) 
    compare_coin_change(67, [25, 10, 5, 1]) 
     
    # Test với hệ mệnh giá lạ (Greedy sai) 
    compare_coin_change(30, [25, 10, 1])