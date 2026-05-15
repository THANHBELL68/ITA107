# Bai 1
def snippet_1(n):
    total = 0 
    for i in range(n): 
        total = total + 1
    return total
  # Độ phức tạp O(n)
  # vì Vòng for chạy n lần vì range(n) tạo ra dãy 0..n-1.
  # Mỗi lần lặp có 1 câu lệnh total = total + 1 coi là 1 bước tính toán chính.
  # Bỏ qua hằng số, số bước ≈ n

# Bai 2
def snippet_2(n):
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count

    # Đô phức tạp O(n²)
    # Vòng ngoài: chạy n lần.
    # Với mỗi i, vòng trong cũng chạy n lần → tổng số lần lệnh count += 1 = n × n = n²
    # Bỏ hằng số
    # Vì có 2 vòng for lồng nhau, mỗi vòng chạy n lần → tổng n * n = n^2 bước.
    
# Bai 3
def snippet_3(n):
    steps = 0
    while n > 0:
        n = n // 2
        steps += 1
    return steps

    # Độ phức tạp: O(log n)
    # mỗi vòng while chia n cho 2, nên số vòng ≈ số lần chia đôi n về 1 là log2(n)

# Bai 4
def constant_work():
    x = 1
    y = 2
    z = x + y
    return z
def snippet_4(n):
    for i in range(n):
        constant_work()

    # Độ phức tạp: O(n)
    # : vòng for chạy n lần, mỗi lần gọi hàm O(1), nên tổng thời gian tỉ lệ tuyến tính với n.

# Bai 5
def snippet_5(n):
    total = 0
    for i in range(n):
        for j in range(i):
            total += 1
    return total

    # Độ phức tạp O(n²)
    # Vì có 2 vòng for lồng nhau, mỗi vòng chạy n lần → tổng n * n = n^2

#Bai 6
def snippet_6(n):
    k = 1
    total = 0
    while k < n:
        for i in range(n):
            total += 1
        k = k * 2
    return total

    # Độ phức tạp (O(n log n))
    # vì vòng while: mỗi lần nhân k với 2 → số lần lặp của while là khoảng log₂(n).
    # Mỗi lần while, vòng for bên trong chạy n lần
    #Tổng số bước ≈ (số vòng while) × n
# Bai 7
def snippet_7(arr):
    count = 0
    for x in arr:
        if x in arr: # kiểm tra x có trong arr
            count += 1
    return count

    # Độ phức tạp O(n²)
    # Vì vòng for chạy n lần
    # Mỗi lần, phép x in arr phải duyệt cả list → tốn O(n)
    # Tổng thời gian ≈ n × n
# Bai 8
def snippet_8(arr):
    s = set(arr)
    count = 0
    for x in arr:
        if x in s:
            count += 1
    return count

     # Độ phức tạp O(n)
     #Tạo set(arr) từ list arr tốn bao nhiêu? (số phần tử = n → O(n)).
     # Vì Vòng for: n lần, mỗi lần x in s là O(1) trung bình.
     # Tổng thời gian: O(n) + n × O(1)

#=======================================================================

# Bài 3 – Tối ưu thuật toán từ O(n²) xuống O(n)
import time
import random
def two_sum_quadratic(arr, target):
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] + arr[j] == target:
             return (i, j)
    return None

    # Độ phức tạp O(n²)
    # Vì có 2 vòng for lồng nhau 
    
def two_sum_linear(arr, target):
    seen = {} 
    for i in range(len(arr)):
        complement = target - arr[i]
        if complement in seen :
            return(seen[complement],i)
        seen[arr[i]] = i 
    return None

arr = list(range(100000))
random.shuffle(arr)

start = time.time()
cach1 = two_sum_quadratic(arr,9876 )
time1 = time.time() - start
print(time1)

target = arr[123] + arr[9876]
start = time.time()
print(two_sum_linear(arr, target))
print("O(n) time 2:", time.time() - start)

# (50, 124)
# Time 1 : 0.019534587860107422
# Time 2 : 0.0001838207244873047