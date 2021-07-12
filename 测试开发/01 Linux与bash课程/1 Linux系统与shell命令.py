# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/7/9 9:02
# @Software       : Python_study
# @Python_verison : 3.7

# 1、Linux系统
'''
Linux系统是由unix演化而来
我们现在熟悉常用的redbat、ubantu、suse、centos都是Linux的发行版
'''



# 2、shell命令
'''
通过shell命令可以让用户去操作Linux系统
常见的shell有Bourne Shell、Bourne Again Shell、C Shell、K Shell
我们使用最多是Bourne Again Shell 也就是bash，也有的是用Bourne Shell也就是sh
windows 可以使用git-bash.exe使用shell命令
使用shell命令需要在文件中声明shell类型比如使用bash，
声明格式为：
#!/bin/bash
echo 'hello'    #表示输出hello，相当于我们python中的print

'''
# 3、shell命令执行
'''
方式1：
    chmod +x ./test.sh   # 使得脚本具有执行权限
    ./test.sh            # 执行脚本   因为有了执行权限后，在当前路径./下直接执行test.sh
    
方式2：
    /bin/sh test.sh     # 因为在根目录下有个bin，bin下面有sh.exe
'''