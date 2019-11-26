# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/26 10:59
# @Software       : Python_study
# @Python_verison : 3.7
# 1、数字：
    # int
    # bigint
    # tinyint
    # float
    # double
    # decimal  十进制，最精确，当我们存储的数据要求精度高时可以定义这个数据类型（10,9）第一个表示数字总个数，后面一个表示小数点后个数。

# 2、字符：
    # char          固定长度，不管存的数据有么有这么长，没有就补充空，效率高，但是浪费内存
    # vachar        不固定长度，效率低但是节省内存
    # text          text与char和varchar不同的是，text不可以有默认值，其最大长度是2的16次方-1
    # enum     枚举类型
    # set      集合类型

# 3、时间：

    # DATE
        # YYYY - MM - DD（1000 - 01 - 01 / 9999 - 12 - 31）

    # TIME
        # HH: MM:SS（'-838:59:59' / '838:59:59'）

    # YEAR
        # YYYY（1901 / 2155）

    # DATETIME
        # YYYY - MM - DD
        # HH: MM:SS（1000 - 01 - 01 00: 00:00 / 9999 - 12 - 31 23: 59:59）
