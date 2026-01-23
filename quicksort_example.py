# -*- coding: utf-8 -*-
# @Time : 2026/1/23 19:34
# @Author : AI Assistant
# @File : quicksort_example.py
# @Description : 快速排序使用示例

from quicksort import quicksort, quicksort_inplace, quicksort_random_pivot

def main():
    """主函数：展示快速排序的使用"""
    print("快速排序使用示例")
    print("=" * 50)
    
    # 示例1：基本使用
    print("示例1：基本快速排序")
    arr1 = [64, 34, 25, 12, 22, 11, 90]
    print(f"原始数组: {arr1}")
    sorted_arr1 = quicksort(arr1)
    print(f"排序结果: {sorted_arr1}")
    print()
    
    # 示例2：原地排序
    print("示例2：原地快速排序")
    arr2 = [9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"原始数组: {arr2}")
    # 注意：原地排序会修改原数组
    arr2_copy = arr2.copy()
    quicksort_inplace(arr2_copy)
    print(f"排序结果: {arr2_copy}")
    print(f"原数组是否被修改: {arr2} (未修改)")
    print()
    
    # 示例3：随机基准排序
    print("示例3：随机基准快速排序")
    arr3 = [3, 6, 8, 10, 1, 2, 1]
    print(f"原始数组: {arr3}")
    sorted_arr3 = quicksort_random_pivot(arr3)
    print(f"排序结果: {sorted_arr3}")
    print()
    
    # 示例4：各种边缘情况
    print("示例4：边缘情况测试")
    
    # 空列表
    empty_arr = []
    print(f"空列表: {empty_arr} -> {quicksort(empty_arr)}")
    
    # 单个元素
    single_arr = [42]
    print(f"单个元素: {single_arr} -> {quicksort(single_arr)}")
    
    # 重复元素
    duplicate_arr = [5, 5, 5, 5, 5]
    print(f"重复元素: {duplicate_arr} -> {quicksort(duplicate_arr)}")
    
    # 已排序数组
    sorted_input = [1, 2, 3, 4, 5]
    print(f"已排序数组: {sorted_input} -> {quicksort(sorted_input)}")
    
    # 逆序数组
    reverse_arr = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    print(f"逆序数组: {reverse_arr} -> {quicksort(reverse_arr)}")
    print()
    
    # 示例5：性能比较
    print("示例5：三种算法结果一致性验证")
    test_array = [7, 2, 1, 6, 8, 5, 3, 4]
    
    result1 = quicksort(test_array.copy())
    result2 = quicksort_inplace(test_array.copy())
    result3 = quicksort_random_pivot(test_array.copy())
    
    print(f"测试数组: {test_array}")
    print(f"基本快速排序结果: {result1}")
    print(f"原地快速排序结果: {result2}")
    print(f"随机基准快速排序结果: {result3}")
    print(f"所有结果是否一致: {result1 == result2 == result3}")
    print()
    
    # 示例6：实际应用场景
    print("示例6：实际应用场景")
    
    # 对学生成绩排序
    grades = [85, 92, 78, 90, 88, 95, 76, 89]
    print(f"学生成绩: {grades}")
    sorted_grades = quicksort(grades)
    print(f"排序后的成绩: {sorted_grades}")
    print(f"最高分: {sorted_grades[-1]}")
    print(f"最低分: {sorted_grades[0]}")
    print(f"中位数: {sorted_grades[len(sorted_grades)//2]}")
    print()
    
    # 对字符串排序（按字母顺序）
    words = ["apple", "banana", "cherry", "date", "elderberry"]
    print(f"单词列表: {words}")
    sorted_words = quicksort(words)
    print(f"按字母顺序排序: {sorted_words}")
    print()
    
    print("=" * 50)
    print("快速排序算法总结:")
    print("1. 时间复杂度: 平均 O(n log n)，最坏 O(n²)")
    print("2. 空间复杂度: 基本版本 O(n)，原地版本 O(log n)")
    print("3. 稳定性: 不稳定排序算法")
    print("4. 适用场景: 大规模数据、内存敏感场景")
    print("=" * 50)

if __name__ == "__main__":
    main()