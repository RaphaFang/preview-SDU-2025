import numpy as np
A = np.array([[1, 2, 3],
              [4, 5, 6]])

# print(A[0, 1])    # ➜ 2
# print(A[1])       # ➜ [4 5 6]
# print(A[:, 0])    # ➜ [1 4]（第一欄）

# -----------------------------------------------------------------
# ! boolean masking
a = np.array([[1, 3],
              [5, 7]])
mask = a > 4
print(mask)       # ➜ [[False False]
                    # [ True  True]]
print(a[mask])    # ➜ [5 7]
print(a[a>4])     #   [5 7]

# -----------------------------------------------------------------
# ! fancy indexing
a = np.array([10, 20, 30, 40, 50])
print(a[[0, 2, 4]])    # ➜ [10 30 50]

A = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

# 取 A[0,1], A[1,2], A[2,0]
print(A[[0,1,2], [1,2,0]])  # 這邊是先 0,1,2 接著填寫另一欄位的index
# ➜ [2 6 7]

# -----------------------------------------------------------------
A = np.array([[10, 20, 30],
              [40, 50, 60],
              [70, 80, 90]])

# 1. 取出第二列
A[1]
# 2. 取出所有列的第三欄
A[:, 2]
# 3. 取出所有元素大於 50 的值
A[A > 50]
# 4. 用 fancy indexing 取出 (0,1)、(2,2)、(1,0) 三個位置的值
A[[0,2,1],[1,2,0]]


# -----------------------------------------------------------------
# Boolean mask 是資料科學中最常用的資料篩選技巧之一，速度與可讀性都遠優於 loop。
# Fancy indexing 很靈活，但記憶體使用要注意(因為他會每個都開一個記憶體空間)，尤其是處理大陣列時。