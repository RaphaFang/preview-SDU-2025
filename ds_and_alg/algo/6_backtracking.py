# permutations
def permute(nums):
    result = []

    def backtrack(path, used):
        if len(path) == len(nums):
            result.append(path[:])  # 加入 path 的拷貝（不能是 path 本身）
            return
        for i in range(len(nums)):
            if used[i]:   # 會在這邊檢查下面的 [False, False, False]
                continue  # 跳過已使用的元素
            path.append(nums[i])
            used[i] = True
            backtrack(path, used)
            path.pop()
            used[i] = False

    backtrack([], [False]*len(nums))
    return result
# print(permute([1, 2, 3]))

# 這思考很複雜
# 直接把他想像成有三層 for
    # [T,T,T] ->  [F,T,T], index -> 0 
    #     [F,T,T] -> [F,F,T], index -> 1 (重要：這loop從 index 2 接續，所以會向下塞 [1,3]，下面的for 會變成[1,3,2])
    #         [F,F,T] -> [F,F,F], index -> 2 (這loop結束)
    #             這邊會pop index 2, 改成 [F,F,T]
    #         這邊會pop index 1, 改成 [F,T,T]


# ------------------------------------------------------------------------
# iteration 的方式
def permute_iter(nums):
    result = [[]]
    for num in nums:
        new_result = []
        for perm in result:
            for i in range(len(perm) + 1):
                # 在 perm 的每個位置插入 num
                new_perm = perm[:i] + [num] + perm[i:]
                new_result.append(new_perm)
        result = new_result
    return result
# print(permute_iter([1, 2, 3]))


# ------------------------------------------------------------------------
# | 寫法 | 複雜度 | 可擴展性（剪枝、限制條件） | 可讀性 |
# | ------------ | ------------ | ----------- | --------------- |
# | Backtracking | O(n × n!) | ✅ 很容易剪枝或加限制 | ✅ |
# | Iterative（插入） | O(n × n!) | ❌ 難剪枝、不靈活 | ❌ |
# | `itertools.permutations` | O(n!) | ❌ 黑箱，不可修改 | ✅（快速原型） |

# ------------------------------------------------------------------------
from itertools import permutations

per = permutations([1, 2, 2, 3])
# print(list(per))

# 這問題是他沒辦法排除重複
# (1, 2, 2, 3) same
# (1, 2, 3, 2)
# (1, 2, 2, 3) same
# (1, 2, 3, 2)
# (1, 3, 2, 2) 
# (1, 3, 2, 2)

# ------------------------------------------------------------------------
import pandas as pd
df = pd.DataFrame({'col': [1, 2, 3]})
perms = list(permutations(df['col']))
# print(perms)


# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def combination(nums):
    result = []

    def backtrack(start, path):
        result.append(path[:])  # 記錄目前子集（複製）
        for i in range(start, len(nums)):
            path.append(nums[i])
            backtrack(i + 1, path)  # 往下遞迴，i+1 是為了避免重複
            path.pop()

    backtrack(0, [])
    return result

# print(combination([1, 2, 3]))

# 這邏輯跟上面的permutation 是類似的，一樣疊 for loop ，接著一層一層到底 1,2,3 ，退掉
# 在用上 range 到下一 index，接著接上 1,3

# ------------------------------------------------------------------------
# ------------------------------------------------------------------------
def solve_n_queens(n):
    result = []

    def backtrack(row, cols, diag1, diag2, path):
        if row == n:
            # 將 path 轉為棋盤文字
            board = []
            for col in path:
                row_str = "." * col + "Q" + "." * (n - col - 1)
                board.append(row_str)
            result.append(board)
            return

        for col in range(n):
            if col in cols or (row - col) in diag1 or (row + col) in diag2:
                continue  # 剪枝：欄位 or 斜線被占用

            # 做選擇
            cols.add(col)
            diag1.add(row - col)  # 主對角線 ↘
            diag2.add(row + col)  # 副對角線 ↙
            path.append(col)

            backtrack(row + 1, cols, diag1, diag2, path)

            # 撤銷選擇
            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)
            path.pop()

    backtrack(0, set(), set(), set(), [])
    return result

for board in solve_n_queens(4):
    for row in board:
        print(row)
    print()
