# 作者: 学不会
# 2026年10月19日17时32分45秒
# xxx@qq.com
import random
import time


class sort:
    def __init__(self, arr_len, num_range):
        self.arr = []
        # self.arr = [3, 87, 2, 93, 78, 56, 61, 38, 12, 40]
        self.arr_len = arr_len
        self.num_range = num_range
        self.__creat_num_range()

    def __creat_num_range(self):
        """
        生成随机数
        :return:
        """
        for i in range(self.arr_len):
            self.arr.append(random.randint(0, self.num_range))

    def bubble_sort(self):
        """
        冒泡排序
        :return:
        """
        # for i in range(self.arr_len, 1, -1):  # 外层循环控制循环次数
        #     flag = True# 哨兵，用于判断是否需要交换
        #     for j in range(i - 1):  # 内层循环控制比较次数
        #
        #         if self.arr[j] > self.arr[j + 1]:
        #             self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
        #             flag = False
        #     if flag:
        #         break

        # 用while循环
        i = self.arr_len - 1
        while i > 0:
            flag = True
            j = 0
            while j < i:
                if self.arr[j] > self.arr[j + 1]:
                    self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j]
                    flag = False
                j += 1
            if flag:
                break
            i -= 1

    def select_sort(self):
        """
        选择排序
        :return:
        """
        arr = self.arr
        for i in range(self.arr_len - 1):
            min_pos = i
            for j in range(i + 1, self.arr_len):
                if arr[j] < arr[min_pos]:
                    min_pos = j

            arr[min_pos], arr[i] = arr[i], arr[min_pos]

    def insert_sort(self):
        """
        插入排序
        :return:
        """
        arr = self.arr
        for i in range(1, self.arr_len):
            insert_value = arr[i]
            j = i - 1
            while j >= 0:
                if arr[j] > insert_value:
                    arr[j + 1] = arr[j]
                else:
                    break
                j -= 1
            arr[j + 1] = insert_value

    def shell_sort(self):
        """
        希尔排序
        :return:
        """
        arr = self.arr
        gap = self.arr_len >> 1
        while gap > 0:
            for i in range(gap, self.arr_len):
                insert_value = arr[i]
                j = i - gap
                while j >= 0:
                    if arr[j] > insert_value:
                        arr[j + gap] = arr[j]
                    else:
                        break
                    j -= gap
                arr[j + gap] = insert_value
            gap = gap >> 1

    def partition(self, low, high):
        """
        把列表一分为二，左边的数都比分割值要小，右边的都比分割值要大，分割值位置确定
        :param low:
        :param high:
        :return: 分割值的下标
        """
        arr = self.arr
        pivot = low
        random_pos=random.randint(low, high)
        arr[random_pos], arr[low] = arr[low], arr[random_pos]  # 交换随机数和第一个数
        for i in range(low, high):
            if arr[i] < arr[high]:
                arr[i], arr[pivot] = arr[pivot], arr[i]
                pivot += 1
        arr[pivot], arr[high] = arr[high], arr[pivot]
        return pivot

    def quick_sort(self, low, high):
        """
        快速排序
        :return:
        """
        # arr = self.arr
        if low < high:
            pivot = self.partition(low, high)
            self.quick_sort(low, pivot - 1)
            self.quick_sort(pivot + 1, high)

    def adjust_max_heap(self, root_pos, arr_len):
        """
        调整某一颗子树为大根堆
        :param root_pos: 被调整子树的父亲的下标
        :param arr_len: 当前列表的长度
        :return:
        """
        arr = self.arr
        dad = root_pos
        son = dad * 2 + 1
        while son < arr_len:
            # 左右孩子进行比较,且右子树大
            if son + 1 < arr_len and arr[son] < arr[son + 1]:
                son += 1
            if arr[son] > arr[dad]:
                arr[son], arr[dad] = arr[dad], arr[son]
                dad = son
                son = dad * 2 + 1
            else:
                break

    def heap_sort(self):
        arr = self.arr

        for dad_pos in range(self.arr_len // 2 - 1, -1, -1):
            self.adjust_max_heap(dad_pos, self.arr_len)

        # 交换堆顶元素和列表最后一个元素

        arr[0], arr[self.arr_len-1] = arr[self.arr_len-1], arr[0]
        for i_len in range(self.arr_len - 1, 1, -1):
            self.adjust_max_heap(0,i_len)  # 继续调整剩余元素为大根堆
            arr[0], arr[i_len - 1] = arr[i_len - 1], arr[0]  # 交换顶部元素，与当前无序列表的最后一个元素


    def cal_sort_time(self,sort_metnod):
        start=time.time()
        sort_metnod()
        end=time.time()
        return end-start




if __name__ == "__main__":
    s = sort(100000, 100)
    # print(s.arr)
    # s.bubble_sort()
    # s.select_sort()
    # s.insert_sort()
    # s.shell_sort()
    # s.quick_sort(0, s.arr_len - 1)
    # print(s.heap_sort())
    # print(s.arr)
    print(s.cal_sort_time(s.heap_sort))
