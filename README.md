# Sorting-algorithm-visualization
排序算法的可视化
=========
冒泡排序
算法思想：从数组中第一个数开始，依次遍历数组中的每一个数，通过相邻比较交换，每一轮循环下来找出剩余未排序数的中的最大数并”冒泡”至数列的顶端。

时间复杂度：O(n2)
空间复杂度：O(1)
稳定性：稳定
def bubble_sort(array):      
  for i in range(len(array)):          
    for j in range(i, len(array)):              
      if array[i] > array[j]:  
        array[i], array[j] = array[j], array[i]
    return array

插入排序
算法思想：从数组中第一个数开始，依次遍历数组中的每一个数，通过相邻比较交换，每一轮循环下来找出剩余未排序数的中的最大数并”冒泡”至数列的顶端。

时间复杂度：O(n2)
空间复杂度：O(1)
稳定性：稳定
def bubble_sort(array):      
  for i in range(len(array)):          
    for j in range(i, len(array)):              
      if array[i] > array[j]:  
        array[i], array[j] = array[j], array[i]
    return array
选择排序
算法思想：从所有记录中选出最小的一个数据元素与第一个位置的记录交换；然后在剩下的记录当中再找最小的与第二个位置的记录交换，循环到只剩下最后一个数据元素为止。

时间复杂度：O(n2)
空间复杂度：O(1)
稳定性：不稳定
def select_sort(array): 
    for i in range(len(array)): 
        x = i  # min index 
        for j in range(i, len(array)): 
            if array[j] < array[x]: 
                x = j 
        array[i], array[x] = array[x], array[i] 
    return array 
插入排序
算法思想：从待排序的n个记录中的第二个记录开始，依次与前面的记录比较并寻找插入的位置，每次外循环结束后，将当前的数插入到合适的位置。

时间复杂度：O(n2)
空间复杂度：O(1)
稳定性：稳定

