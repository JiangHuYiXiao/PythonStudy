#-*- coding:utf-8 -*-
# 二分查找算法，必须处理有序的列表

def find_func(l,aim,start=0,end=None):
    end = len(l) if end is None else end
    mid_index = (end-start) // 2 + start
    if start <= end:
        if aim == l[mid_index]:
            return mid_index
        elif aim < l[mid_index]:
            return find_func(l,aim,start=start,end =mid_index-1)

        else:
            return find_func(l,aim,start=mid_index+1,end=end)
    else:
        return ('找不到，该元素不在列表中')
l = [2,3,5,10,15,16,18,22,26,31,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
res =find_func(l,66)
print(res)


