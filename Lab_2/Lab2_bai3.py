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