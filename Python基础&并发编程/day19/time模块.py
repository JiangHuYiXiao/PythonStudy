# -*- coding:utf-8 -*-
# 一、时间分类：
# 各种时间之间的转换
# timestamp--localmaltime->struct_time--strftime->Format String
# Format String--strptime->struct_time--mktime->timestamp
# 1、时间戳时间（timestamp）：float类型，从1970年1月1日 的00:00:00开始按照秒计时的偏移量，是一个浮点数
import time
timestamp1 = time.time()
print(timestamp1)          # 输出时间戳时间

# 2、结构化时间（struct_time）：元组类型，struct_time元组有九个元素（年，月，日，时，分，秒，一年中第几周，一年中第几天，是否是夏令时）是为了能够操作时间
struct_time1 = time.localtime(timestamp1)
print(struct_time1)         # time.struct_time(tm_year=2019, tm_mon=1, tm_mday=8, tm_hour=19, tm_min=6, tm_sec=6, tm_wday=1, tm_yday=8, tm_isdst=0)

# 3、格式化时间（Format String）：字符串类型，年-月-日 时:分:秒,是为了给人能够看的懂的时间
# 格式化时间的格式存在下面这些
'''
%y 两位数的年份表示（00-99）
%Y 四位数的年份表示（000-9999）
%m 月份（01-12）
%d 月内中的一天（0-31）
%H 24小时制小时数（0-23）
%I 12小时制小时数（01-12）
%M 分钟数（00=59）
%S 秒（00-59）
%a 本地简化星期名称
%A 本地完整星期名称
%b 本地简化的月份名称
%B 本地完整的月份名称
%c 本地相应的日期表示和时间表示
%j 年内的一天（001-366）
%p 本地A.M.或P.M.的等价符
%U 一年中的星期数（00-53）星期天为星期的开始
%w 星期（0-6），星期天为星期的开始
%W 一年中的星期数（00-53）星期一为星期的开始
%x 本地相应的日期表示
%X 本地相应的时间表示
%Z 当前时区的名称
%% %号本身
'''
Formattime1 =time.strftime('%Y-%m-%d %H:%M:%S',struct_time1)
print(Formattime1)


fomat_time2 = '2018-01-08 19:12:39'
struct_time2 = time.strptime(fomat_time2,'%Y-%m-%d %H:%M:%S')
print(struct_time2)
timestamp2 = time.mktime(struct_time2)
print(timestamp2)

