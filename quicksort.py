# -*- coding: utf-8 -*-
# @Time : 2026/1/23 19:19
# @Author : AI Assistant
# @File : quicksort.py
# @Description : 快速排序算法实现

def quicksort(arr):
    """
    快速排序算法实现
    
    参数:
        arr (list): 待排序的列表
        
    返回:
        list: 排序后的列表
    """
    # 基本情况：如果列表长度小于等于1，直接返回
    if len(arr) <= 1:
        return arr
    
    # 选择基准元素（这里选择中间元素）
    pivot = arr[len(arr) // 2]
    
    # 分区操作
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    # 递归排序左右子数组并合并结果
    return quicksort(left) + middle + quicksort(right)


def quicksort_inplace(arr, low=0, high=None):
    """
    原地快速排序算法（节省内存）
    
    参数:
        arr (list): 待排序的列表
        low (int): 子数组的起始索引
        high (int): 子数组的结束索引
        
    返回:
        list: 原地排序后的列表
    """
    if high is None:
        high = len(arr) - 1
    
    if low < high:
        # 分区操作，获取基准元素的正确位置
        pivot_index = partition(arr, low, high)
        
        # 递归排序基准元素左右两侧的子数组
        quicksort_inplace(arr, low, pivot_index - 1)
        quicksort_inplace(arr, pivot_index + 1, high)
    
    return arr


def partition(arr, low, high):
    """
    分区函数，用于原地快速排序
    
    参数:
        arr (list): 待分区的列表
        low (int): 子数组的起始索引
        high (int): 子数组的结束索引
        
    返回:
        int: 基准元素的最终位置
    """
    # 选择最后一个元素作为基准
    pivot = arr[high]
    
    # i 指向小于基准的元素的边界
    i = low - 1
    
    for j in range(low, high):
        # 如果当前元素小于或等于基准
        if arr[j] <= pivot:
            i += 1
            # 交换 arr[i] 和 arr[j]
            arr[i], arr[j] = arr[j], arr[i]
    
    # 将基准元素放到正确的位置
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quicksort_random_pivot(arr):
    """
    使用随机基准的快速排序算法
    
    参数:
        arr (list): 待排序的列表
        
    返回:
        list: 排序后的列表
    """
    import random
    
    if len(arr) <= 1:
        return arr
    
    # 随机选择基准元素
    pivot = random.choice(arr)
    
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    
    return quicksort_random_pivot(left) + middle + quicksort_random_pivot(right)


def test_quicksort():
    """测试快速排序算法"""
    print("=" * 50)
    print("快速排序算法测试")
    print("=" * 50)
    
    # 测试用例
    test_cases = [
        ([], []),  # 空列表
        ([1], [1]),  # 单个元素
        ([5, 3, 8, 6, 2], [2, 3, 5, 6, 8]),  # 普通情况
        ([9, 8, 7, 6, 5, 4, 3, 2, 1], [1, 2, 3, 4, 5, 6, 7, 8, 9]),  # 逆序
        ([1, 2, 3, 4, 5], [1, 2, 3, 4, 5]),  # 已排序
        ([3, 3, 3, 3, 3], [3, 3, 3, 3, 3]),  # 重复元素
        ([64, 34, 25, 12, 22, 11, 90], [11, 12, 22, 25, 34, 64, 90]),  # 更多元素
    ]
    
    all_passed = True
    
    for i, (input_arr, expected) in enumerate(test_cases):
        # 测试基本快速排序
        result1 = quicksort(input_arr.copy())
        passed1 = result1 == expected
        
        # 测试原地快速排序
        arr_copy = input_arr.copy()
        result2 = quicksort_inplace(arr_copy)
        passed2 = result2 == expected
        
        # 测试随机基准快速排序
        result3 = quicksort_random_pivot(input_arr.copy())
        passed3 = result3 == expected
        
        all_passed = all_passed and passed1 and passed2 and passed3
        
        print(f"\n测试用例 {i + 1}: {input_arr}")
        print(f"期望结果: {expected}")
        print(f"基本快速排序: {result1} {'✓' if passed1 else '✗'}")
        print(f"原地快速排序: {result2} {'✓' if passed2 else '✗'}")
        print(f"随机基准快速排序: {result3} {'✓' if passed3 else '✗'}")
    
    print("\n" + "=" * 50)
    if all_passed:
        print("所有测试用例通过！ ✓")
    else:
        print("部分测试用例失败！ ✗")
    print("=" * 50)


def benchmark_quicksort():
    """性能基准测试"""
    import time
    import random
    
    print("\n" + "=" * 50)
    print("性能基准测试")
    print("=" * 50)
    
    # 生成测试数据
    sizes = [100, 1000, 5000, 10000]
    
    for size in sizes:
        # 生成随机数据
        data = [random.randint(0, 10000) for _ in range(size)]
        
        print(f"\n数据大小: {size}")
        
        # 测试基本快速排序
        start = time.time()
        result1 = quicksort(data.copy())
        time1 = time.time() - start
        
        # 测试原地快速排序
        start = time.time()
        result2 = quicksort_inplace(data.copy())
        time2 = time.time() - start
        
        # 测试随机基准快速排序
        start = time.time()
        result3 = quicksort_random_pivot(data.copy())
        time3 = time.time() - start
        
        print(f"基本快速排序: {time1:.6f} 秒")
        print(f"原地快速排序: {time2:.6f} 秒")
        print(f"随机基准快速排序: {time3:.6f} 秒")
        
        # 验证所有算法结果一致
        if result1 == result2 == result3:
            print("✓ 所有算法结果一致")
        else:
            print("✗ 算法结果不一致")


def main():
    """主函数"""
    print("快速排序算法实现")
    print("=" * 50)
    print("1. 基本快速排序 (quicksort)")
    print("2. 原地快速排序 (quicksort_inplace)")
    print("3. 随机基准快速排序 (quicksort_random_pivot)")
    print("4. 运行测试用例")
    print("5. 性能基准测试")
    print("=" * 50)
    
    try:
        choice = input("请选择操作 (1-5, 按回车键退出): ").strip()
        
        if choice == "1":
            # 基本快速排序示例
            arr = input("请输入要排序的数字，用空格分隔: ").strip()
            if arr:
                arr = list(map(int, arr.split()))
                print(f"原始数组: {arr}")
                sorted_arr = quicksort(arr)
                print(f"排序结果: {sorted_arr}")
        
        elif choice == "2":
            # 原地快速排序示例
            arr = input("请输入要排序的数字，用空格分隔: ").strip()
            if arr:
                arr = list(map(int, arr.split()))
                print(f"原始数组: {arr}")
                sorted_arr = quicksort_inplace(arr.copy())
                print(f"排序结果: {sorted_arr}")
        
        elif choice == "3":
            # 随机基准快速排序示例
            arr = input("请输入要排序的数字，用空格分隔: ").strip()
            if arr:
                arr = list(map(int, arr.split()))
                print(f"原始数组: {arr}")
                sorted_arr = quicksort_random_pivot(arr)
                print(f"排序结果: {sorted_arr}")
        
        elif choice == "4":
            # 运行测试
            test_quicksort()
        
        elif choice == "5":
            # 性能测试
            benchmark_quicksort()
        
        else:
            print("退出程序")
    
    except ValueError:
        print("错误: 请输入有效的数字！")
    except KeyboardInterrupt:
        print("\n程序被用户中断")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    main()