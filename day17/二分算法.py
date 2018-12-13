#-*- coding:utf-8 -*-
# 二分查找算法，必须处理有序的列表
# 需求：查找元素的索引位置，并返回
def find_func(l,aim,start=0,end=None):
    end = len(l) if end is None else end    # 为了处理end每次为len（l）且每次需要先定义l的问题
    mid_index = (end-start) // 2 + start
    if start <= end:                # 为了处理元素不在列表中的情况，这种场景的数据一直递归下去后，最后是start<end,元素不在列表中
        if aim == l[mid_index]:
            return ('%s的索引位置为:%s')%(aim,mid_index)          # 必须有返回
        elif aim < l[mid_index]:
            return find_func(l,aim,start=start,end =mid_index-1)   # 递归：必须有返回给下一次递归使用

        else:
            return find_func(l,aim,start=mid_index+1,end=end)      # 递归：必须有返回给下一次递归使用
    else:
        return ('找不到，该元素不在列表中')
l = [2,3,5,10,15,16,18,22,26,31,32,35,41,42,43,55,56,66,67,69,72,76,82,83,88]
res =find_func(l,66)
print(res)


