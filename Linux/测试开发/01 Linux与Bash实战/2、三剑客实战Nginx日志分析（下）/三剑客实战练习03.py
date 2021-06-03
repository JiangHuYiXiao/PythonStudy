# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/10/23 8:52
# @Software       : 测试开发
# @Python_verison : 3.7
# 练习1：查找出nginx.logz中的所有404或者500
'''
-E,因为使用了扩展正则|所以必须使用-E,
-n 显示行号
方法1：
jianghu@ubuntu:~$ grep -En '\s404\s|\s500\s' nginx.log |wc -l

方法2：
jianghu@ubuntu:~$ awk '/ 404 | 500 /{print$9}' nginx.log |wc -l

方法3：
~表示
jianghu@ubuntu:~$ awk '$9~/404|500/{print$9}' nginx.log |wc -l
'''


# 练习2：查找访问量最高的三个ip

'''
sort:排序
unique-c：分组
sort -nr：倒序
head -3 ：前三个数
jianghu@ubuntu:~$ awk '{print$1}' nginx.log |sort|uniq -c|sort -nr|head -3

'''


# 练习3：将topics后面的数字替换成具体的数
# 216.244.66.241 - - [05/Dec/2018:00:11:46 +0000] "GET /topics/10079/replies/119591/edit HTTP/1.1" 301 5 "-" "Mozilla/5.0 (compatible; DotBot/1.1; http://www.opensiteexplorer.org/dotbot, help@moz.com)" 0.001 0.001 .
'''
s///g
s#/topics/10079#/topics/number#g
jianghu@ubuntu:~$ grep '/topics/' nginx.log | sed 's@/topics/[0-9]*@/topics/number@g'
'''

# 练习4：将ip地址横排排列在一行
    # 解析：N表示将下一行追加到此行
    #:1表示第一行,t1和1是一起使用的
    # 如果追加到第二行是:2;t2
'''
jianghu@ubuntu:~$ awk '{print$1}' nginx.log | sed ':1;N;s/\n/|/g;t1'^C
'''

