# ==============================================================================
# Bài 3 – Subset Sum với pruning nâng cao
# ==============================================================================

import time

# ------------------------------------------------------------------------------
# Bộ đếm hiệu năng hỗ trợ đo lường và tính tỷ lệ cắt tỉa
# ------------------------------------------------------------------------------
class Counter:
    def __init__(self):
        self.total_calls = 0        # Tổng số lần gọi hàm đệ quy (Node)
        self.pruned_branches = 0    # Số lần các nhánh bị cắt tỉa sớm

    def reset(self):
        self.total_calls = 0
        self.pruned_branches = 0


# ------------------------------------------------------------------------------
# Phần A – Subset Sum cơ bản (Không có Pruning)
# ------------------------------------------------------------------------------
def subset_sum_basic(nums, target, counter):
    """
    Subset Sum cơ bản - KHÔNG có pruning (Duyệt toàn bộ cây quyết định).
    
    - Base case: Nếu current_sum == target, lưu một bản sao của path vào kết quả.
    - Chú ý: Hàm này không có return ngay ở Base Case vì mảng nums có thể chứa 
             số 0 hoặc các số âm, nhưng ở đây theo form đề bài ta chỉ xét số dương.
    """
    result = []
     
    def backtrack(start, path, current_sum):
        counter.total_calls += 1
        
        # Base case: Đạt được tổng mục tiêu
        if current_sum == target:
            result.append(path.copy())
            # Không return ở đây để tiếp tục tìm kiếm (đề phòng trường hợp tập dữ liệu có số 0)
         
        # Duyệt qua các phần tử từ vị trí start
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path, current_sum + nums[i]) 
            path.pop()
     
    backtrack(0, [], 0)
    return result


# ------------------------------------------------------------------------------
# Phần B – Subset Sum với Pruning Nâng Cao (Áp dụng 4 kỹ thuật)
# ------------------------------------------------------------------------------
def subset_sum_advanced(nums, target, counter):
    """
    Subset Sum nâng cao - Áp dụng liên hoàn 4 kỹ thuật Pruning:
    1. Early termination: Vượt quá target -> Hủy nhánh.
    2. Sort & Break: Sắp xếp mảng, nếu cộng số hiện tại vượt target -> Ngắt vòng lặp.
    3. Skip duplicates: Tránh sinh trùng tổ hợp khi mảng có các phần tử giống nhau.
    4. Remaining check: Nếu tổng các phần tử còn lại không đủ bù -> Ngắt vòng lặp.
    """
    result = []
    
    # BẮT BUỘC: Kỹ thuật 2 đòi hỏi mảng đầu vào phải được sắp xếp tăng dần
    nums_sorted = sorted(nums)
    
    # Tính toán trước mảng dồn (Suffix Sum) để tối ưu O(1) cho Kỹ thuật 4 thay vì dùng sum() liên tục
    total_elements = len(nums_sorted)
    suffix_sums = [0] * (total_elements + 1)
    for i in range(total_elements - 1, -1, -1):
        suffix_sums[i] = suffix_sums[i+1] + nums_sorted[i]
     
    def backtrack(start, path, current_sum):
        counter.total_calls += 1
        if current_sum == target:
            result.append(path.copy())
            return
            
        # Kỹ thuật 1: Early termination (Cắt tỉa nếu tổng hiện tại lỡ vượt target)
        if current_sum > target:
            counter.pruned_branches += 1
            return
         
        for i in range(start, len(nums_sorted)):
            # Kỹ thuật 3: Skip duplicates (Bỏ qua nếu số này trùng với số trước ở cùng một tầng đệ quy)
            if i > start and nums_sorted[i] == nums_sorted[i-1]:
                continue
                
            # Kỹ thuật 2: Sort và break (Do mảng đã sắp xếp, số này làm vượt target thì các số sau chắc chắn cũng vậy)
            if current_sum + nums_sorted[i] > target:
                # Toàn bộ các nhánh từ `i` đến cuối vòng lặp bị hủy bỏ
                counter.pruned_branches += (len(nums_sorted) - i)
                break
                
            # Kỹ thuật 4: Remaining check (Lấy tổng còn lại ở hậu phương xem có đủ kéo về target không)
            remaining_sum = suffix_sums[i]
            if current_sum + remaining_sum < target:
                # Cộng hết sạch sành sanh cũng không đủ target -> Huỷ bỏ luôn tất cả phần tử sau
                counter.pruned_branches += (len(nums_sorted) - i)
                break
                
            # CHOOSE
            path.append(nums_sorted[i])
             
            # EXPLORE
            backtrack(i + 1, path, current_sum + nums_sorted[i])
             
            # UNCHOOSE
            path.pop()
     
    backtrack(0, [], 0)
    return result


# ------------------------------------------------------------------------------
# Phần C – So sánh và đo lường hiệu năng thực tế
# ------------------------------------------------------------------------------
def compare_subset_sum(nums, target):
    counter = Counter()
    
    print(f"{'='*60}")
    print(f" BÁO CÁO HIỆU NĂNG SUBSET SUM (Target = {target})")
    print(f"{'='*60}")
    print(f"Tập dữ liệu đầu vào ({len(nums)} phần tử): {nums}\n")
    
    # 1. Thực nghiệm với phiên bản Cơ bản (Brute-force)
    counter.reset()
    start_time = time.time()
    res_basic = subset_sum_basic(nums, target, counter)
    time_basic = time.time() - start_time
    
    calls_basic = counter.total_calls
    print("[1] PHIÊN BẢN CƠ BẢN (KHÔNG PRUNING):")
    print(f"  + Tổng số lần gọi hàm (Nodes): {calls_basic:,} lần")
    print(f"  + Thời gian chạy thực tế    : {time_basic:.6f}s")
    print(f"  + Tìm thấy                  : {len(res_basic)} tập con")
    print("-" * 40)
    
    # 2. Thực nghiệm với phiên bản Nâng cao (Pruning)
    counter.reset()
    start_time = time.time()
    res_adv = subset_sum_advanced(nums, target, counter)
    time_advanced = time.time() - start_time
    
    calls_adv = counter.total_calls
    pruned = counter.pruned_branches
    # Tỷ lệ cắt (%) = (Số nhánh bị tỉa / (Tổng số lần gọi thực tế + Số nhánh bị tỉa)) * 100
    prune_rate = (pruned / (calls_adv + pruned)) * 100 if (calls_adv + pruned) > 0 else 0
    
    print("[2] PHIÊN BẢN NÂNG CAO (CÓ PRUNING):")
    print(f"  + Tổng số lần gọi hàm (Nodes): {calls_adv:,} lần")
    print(f"  + Số nhánh đã cắt tỉa sớm    : {pruned:,} nhánh")
    print(f"  + Tỷ lệ cắt tỉa thành công   : {prune_rate:.2f}%")
    print(f"  + Thời gian chạy thực tế    : {time_advanced:.6f}s")
    print(f"  + Tìm thấy                  : {len(res_adv)} tập con")
    print("-" * 40)
    
    # 3. Tổng hợp so sánh tỷ lệ đột phá hiệu năng
    speedup_time = time_basic / time_advanced if time_advanced > 0 else 1
    speedup_nodes = calls_basic / calls_adv if calls_adv > 0 else 1
    
    print("[3] KẾT LUẬN ĐÁNH GIÁ:")
    print(f"  => Thuật toán Pruning giảm thiểu số Node đệ quy: {speedup_nodes:.1f} lần!")
    print(f"  => Tốc độ thời gian hệ thống tăng trưởng vượt trội: {speedup_time:.2f} lần!")
    
    # In ra một vài tập con mẫu tìm được để đối chiếu
    if len(res_adv) > 0:
        print(f"\nMột số tập con hợp lệ mẫu (Hiển thị tối đa 3 tập):")
        for subset in res_adv[:3]:
            print(f"  * {subset} -> Tổng: {sum(subset)}")


# ==============================================================================
# KHU VỰC KÍCH HOẠT HỆ THỐNG KIỂM THỬ DỮ LIỆU LỚN
# ==============================================================================
if __name__ == "__main__":
    # Test cấu hình dữ liệu lớn theo đề bài: nums từ 1 đến 19, target = 50
    big_nums = list(range(1, 20))
    target_val = 50
    
    compare_subset_sum(big_nums, target_val)