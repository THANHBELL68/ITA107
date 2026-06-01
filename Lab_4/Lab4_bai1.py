# ==============================================================================
# Bài 1 – Thuật toán Tham lam (Greedy Algorithm) cơ bản
# File: lab4_bai1.py
# ==============================================================================

# ------------------------------------------------------------------------------
# Hàm 1 – Activity Selection (Chọn số lượng hoạt động tối đa)
# ------------------------------------------------------------------------------
def activity_selection(activities): 
    """ 
    Chọn số lượng hoạt động tối đa không chồng lấp lên nhau.
    
    - Chiến lược Greedy: Luôn ưu tiên chọn hoạt động có thời gian kết thúc SỚM NHẤT 
      (Earliest Finish Time). Việc này giúp giải phóng thời gian sớm, nhường chỗ cho 
      các hoạt động phía sau.
    - Độ phức tạp Big-O:
        + Thời gian: O(n log n) - Chiếm phần lớn bởi bước sắp xếp danh sách (sort).
        + Không gian: O(1) - Nếu không tính bộ nhớ lưu trữ kết quả đầu ra.
    """ 
    if not activities: 
        return [] 
     
    # Bước 1: Sắp xếp tăng dần theo thời gian kết thúc (finish time)
    # Sửa lại lỗi hiển thị ký tự lạ [^1] từ tài liệu gốc thành index [1]
    activities.sort(key=lambda x: x[1]) 
     
    # Bước 2: Chọn hoạt động đầu tiên (luôn là hoạt động kết thúc sớm nhất) 
    selected = [activities[0]] 
    last_finish = activities[0][1] 
     
    # Bước 3: Duyệt qua các hoạt động còn lại để lọc cấu hình không trùng lịch
    for i in range(1, len(activities)): 
        start, finish = activities[i] 
         
        # Nếu thời gian bắt đầu >= thời gian kết thúc của hoạt động trước -> Chọn
        if start >= last_finish: 
            selected.append((start, finish)) 
            last_finish = finish 
     
    return selected 


# ------------------------------------------------------------------------------
# Hàm 2 – Coin Change Greedy (Đổi tiền tham lam)
# ------------------------------------------------------------------------------
def coin_change_greedy(amount, coins): 
    """ 
    Đổi tiền bằng số xu ít nhất dựa trên phương pháp tham lam.
    
    - Chiến lược Greedy: Luôn ưu tiên chọn mệnh giá xu LỚN NHẤT có thể dùng tại 
      thời điểm hiện tại để giảm số tiền cần đổi một cách nhanh nhất.
    - LƯU Ý LÝ THUYẾT: Thuật toán này CHỈ ĐÚNG với hệ thống tiền chuẩn (canonical coin system). 
      Với hệ tiền bất kỳ, thuật toán có thể cho ra kết quả sai hoặc không tìm được lời giải.
    - Độ phức tạp Big-O:
        + Thời gian: O(n log n) cho bước sắp xếp số mệnh giá xu. Vòng lặp chạy phụ thuộc vào 
          tỷ lệ số tiền (amount / mệnh giá xu nhỏ nhất).
        + Không gian: O(1) - Không tốn thêm không gian bộ nhớ.
    """ 
    # Bước 1: Sắp xếp các mệnh giá xu giảm dần (lớn nhất đứng trước) 
    coins.sort(reverse=True) 
    count = 0 
    result = []  # Lưu chi tiết danh sách các xu đã dùng 
     
    # Bước 2: Duyệt qua từng mệnh giá xu
    for coin in coins: 
        # Trừ liên tục và lấy nhiều nhất có thể từ mệnh giá hiện tại 
        while amount >= coin: 
            result.append(coin) 
            amount -= coin 
            count += 1 
     
    # Bước 3: Kiểm tra xem đã đổi hết sạch tiền chưa 
    if amount == 0: 
        return count, result 
    else: 
        return -1, []  # Trả về -1 nếu hệ xu không thể đổi khớp số tiền


# ------------------------------------------------------------------------------
# Hàm 3 – Fractional Knapsack (Bài toán Ba lô phân số)
# ------------------------------------------------------------------------------
def fractional_knapsack(capacity, items): 
    """ 
    Giải bài toán Ba lô phân số (Có thể chia cắt vật phẩm).
    
    - Chiến lược Greedy: Tính tỷ lệ giá trị trên một đơn vị trọng lượng (value / weight) 
      của từng vật phẩm. Luôn ưu tiên hốt vật phẩm có mật độ giá trị CAO NHẤT trước.
    - Sự khác biệt: Khác với bài toán 0/1 Knapsack, ở đây ta được phép cắt lấy một phần 
      phân số của vật phẩm nên chiến lược Greedy luôn mang lại kết quả tối ưu tuyệt đối.
    - Độ phức tạp Big-O:
        + Thời gian: O(n log n) - Do bước sắp xếp các vật phẩm theo tỷ lệ giảm dần.
        + Không gian: O(n) - Cần mảng phụ để lưu trữ kèm theo giá trị tỷ lệ (ratio).
    """ 
    # Bước 1: Tính ratio (value/weight) cho mỗi vật và lưu vào cấu trúc mới
    items_with_ratio = [] 
    for weight, value in items: 
        ratio = value / weight 
        items_with_ratio.append((weight, value, ratio)) 
     
    # Sắp xếp danh sách giảm dần theo tỷ lệ ratio
    items_with_ratio.sort(key=lambda x: x[2], reverse=True) 
     
    # Bước 2: Duyệt chọn vật phẩm bỏ vào ba lô
    total_value = 0.0 
    remaining_capacity = capacity 
    result = []  # Lưu chi tiết tỷ lệ vật phẩm thu nạp
     
    for weight, value, ratio in items_with_ratio: 
        if remaining_capacity == 0: 
            break 
         
        # Nếu trọng lượng vật phẩm nhỏ hơn sức chứa còn lại -> Hốt trọn gói
        if weight <= remaining_capacity: 
            total_value += value 
            remaining_capacity -= weight 
            result.append((weight, value, 1.0))  # 1.0 tương đương lấy 100% 
        else: 
            # Ba lô sắp đầy -> Cắt một phần phân số vừa đủ sức chứa còn lại
            fraction = remaining_capacity / weight 
            total_value += value * fraction 
            result.append((weight, value, fraction)) 
            remaining_capacity = 0  # Ba lô đã đầy hoàn toàn
     
    return total_value, result 


# ------------------------------------------------------------------------------
# Hàm 4 – Minimum Number of Intervals to Remove (Xóa ít khoảng nhất)
# ------------------------------------------------------------------------------
def min_intervals_remove(intervals): 
    """ 
    Tìm số lượng khoảng thời gian tối thiểu cần xóa bỏ để các khoảng còn lại không chồng lấp.
    
    - Chiến lược Greedy: Chuyển đổi bài toán thành Activity Selection. 
      Để số lượng khoảng cần XÓA là ÍT NHẤT, ta cần tìm số lượng khoảng giữ lại tối đa 
      sao cho không chồng chéo nhau.
      Công thức: Số lượng cần xóa = Tổng số khoảng ban đầu - Số khoảng tối đa giữ lại.
    - Độ phức tạp Big-O:
        + Thời gian: O(n log n) - Thừa hưởng từ hàm phụ activity_selection.
        + Không gian: O(n) - Bộ nhớ lưu trữ mảng trung gian giữ lại.
    """ 
    if not intervals: 
        return 0 
     
    # Tái sử dụng triệt để thuật toán Activity Selection ở Hàm 1
    max_keep = activity_selection(intervals) 
     
    # Phép toán bù để tìm số lượng tối thiểu phải loại bỏ
    num_remove = len(intervals) - len(max_keep) 
     
    return num_remove 


# ==============================================================================
# KHU VỰC CHẠY THỬ VÀ KIỂM TRA TOÀN DIỆN (TEST CASES)
# ==============================================================================
if __name__ == "__main__":

    # ==========================================
    # TEST HÀM 1: Activity Selection
    # ==========================================
    print("=== Test Activity Selection ===") 
    activities1 = [(1, 4), (3, 5), (0, 6), (5, 7), (3, 9), (5, 9), (6, 10), (8, 11), (8, 12), (2, 14), (12, 16)] 
    result_act1 = activity_selection(activities1) 
    print(f"Test 1 - Hoạt động được chọn: {result_act1}") 
    print(f"         Số lượng hoạt động   : {len(result_act1)}")  # Kỳ vọng: 4 
     
    activities2 = [(1, 3), (2, 4), (3, 5), (4, 6)] 
    result_act2 = activity_selection(activities2) 
    print(f"Test 2 - Hoạt động được chọn: {result_act2}") 
    print(f"         Số lượng hoạt động   : {len(result_act2)}")  # Kỳ vọng: 2 
    print("-" * 60)

    # ==========================================
    # TEST HÀM 2: Coin Change Greedy
    # ==========================================
    print("=== Test Coin Change Greedy ===") 
    # Trường hợp 1: Hệ tiền chuẩn USD
    amount1 = 63 
    coins1 = [25, 10, 5, 1] 
    count1, detail1 = coin_change_greedy(amount1, coins1) 
    print(f"Test 1 (Hệ tiền USD) - Số tiền: {amount1} -> Cần ít nhất: {count1} xu. Chi tiết: {detail1}") 
     
    # Trường hợp 2: Hệ tiền Việt Nam chuẩn
    amount2 = 370 
    coins2 = [500, 200, 100, 50, 20, 10] 
    count2, detail2 = coin_change_greedy(amount2, coins2) 
    print(f"Test 2 (Hệ tiền VNĐ) - Số tiền: {amount2} -> Cần ít nhất: {count2} xu. Chi tiết: {detail2}") 
     
    # Trường hợp 3: Chứng minh Greedy sai lầm với hệ tiền dị biệt
    amount3 = 30 
    coins3 = [25, 10, 1] 
    count3, detail3 = coin_change_greedy(amount3, coins3) 
    print(f"Test 3 (Hệ xu dị biệt) - Số tiền: {amount3} -> Greedy cho ra: {count3} xu. Chi tiết: {detail3}") 
    print("  ⚠️ LƯU Ý: Kết quả tối ưu thực tế phải là 3 xu [10, 10, 10]. Trực quan hóa lỗi của chiến lược Greedy.")
    print("-" * 60)

    # ==========================================
    # TEST HÀM 3: Fractional Knapsack
    # ==========================================
    print("=== Test Fractional Knapsack ===") 
    capacity1 = 50 
    items1 = [(10, 60), (20, 100), (30, 120)] 
    total_val1, detail_knap1 = fractional_knapsack(capacity1, items1) 
    print(f"Test 1 - Sức chứa ba lô: {capacity1} -> Tổng giá trị lớn nhất: {total_val1}") 
    for weight, value, fraction in detail_knap1: 
        print(f"         * Vật phẩm (Trọng lượng={weight}, Giá trị={value}): Đã lấy {fraction*100:.1f}%") 
        
    capacity2 = 60 
    items2 = [(10, 500), (20, 300), (30, 400)] 
    total_val2, detail_knap2 = fractional_knapsack(capacity2, items2) 
    print(f"Test 2 - Sức chứa ba lô: {capacity2} -> Tổng giá trị lớn nhất: {total_val2}") 
    for weight, value, fraction in detail_knap2: 
        print(f"         * Vật phẩm (Trọng lượng={weight}, Giá trị={value}): Đã lấy {fraction*100:.1f}%") 
    print("-" * 60)

    # ==========================================
    # TEST HÀM 4: Minimum Number of Intervals to Remove
    # ==========================================
    print("=== Test Minimum Intervals Remove ===") 
    intervals1 = [(1, 2), (2, 3), (3, 4), (1, 3)] 
    rem1 = min_intervals_remove(intervals1) 
    print(f"Test 1 - Cấu hình khoảng: {intervals1} -> Số lượng tối thiểu cần xóa: {rem1}") 
     
    intervals2 = [(1, 2), (1, 2), (1, 2)] 
    rem2 = min_intervals_remove(intervals2) 
    print(f"Test 2 - Cấu hình khoảng: {intervals2} -> Số lượng tối thiểu cần xóa: {rem2}") 
     
    intervals3 = [(1, 100), (11, 22), (1, 11), (2, 12)] 
    rem3 = min_intervals_remove(intervals3) 
    print(f"Test 3 - Cấu hình khoảng: {intervals3} -> Số lượng tối thiểu cần xóa: {rem3}") 
    print("=" * 60)