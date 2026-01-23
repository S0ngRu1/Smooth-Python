arr = [0,1,2,3,4,5,6,7,8,9]
slicer = slice(2,8)
print(f"切片结果: {arr[slicer]}")

arr[1:4] = [99]
print(f"修改后数组: {arr}")

board = [['_'] *3 for _ in range(3)] 
print("初始棋盘:")
for row in board:
    print(row)
print()
board[0][0:2] = ['X', 'O']
print("修改后棋盘:")
for row in board:
    print(row)
print()

board = [['_'] *3]*3 
print("初始棋盘:")
for row in board:
    print(row)
print()
board[0][0:2] = ['X', 'O']
print("修改后棋盘:")
for row in board:
    print(row)
print()

t = (1,2,[30,40])
print(f"初始元组: {t}")
# t[2] += [50,60]# This will raise a TypeError
print(f"修改后元组: {t}")