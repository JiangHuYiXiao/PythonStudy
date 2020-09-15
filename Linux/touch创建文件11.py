# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/9/15 9:00
# @Software       : Python_study
# @Python_verison : 3.7
# linux的touch命令不常用，一般在使用make的时候可能会用到，用来修改文件时间戳，或者新建一个不存在的文件。

# 1．命令格式：

# touch [选项]... 文件...

# 2．命令参数：

# -a   或--time=atime或--time=access或--time=use 　只更改存取时间。

# -c   或--no-create 　不建立任何文档。

# -d 　使用指定的日期时间，而非现在的时间。

# -f 　此参数将忽略不予处理，仅负责解决BSD版本touch指令的兼容性问题。

# -m   或--time=mtime或--time=modify 　只更改变动时间。

# -r 　把指定文档或目录的日期时间，统统设成和参考文档或目录的日期时间相同。

# -t 　使用指定的日期时间，而非现在的时间。

# 3．命令功能：

# touch命令参数可更改文档或目录的日期时间，包括存取时间和更改时间。