# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2020/9/15 8:43
# @Software       : Python_study
# @Python_verison : 3.7
# 使用管道命令|我们可以将需要存储的文件内容放到管道中，而不需要放到文件中，方便处理
# ls -alh /etc |more            查看bin目录下的文件

'''
jianghu@ubuntu:/$ ls -alh /etc|more
总用量 1.4M
drwxr-xr-x 145 root root    12K 9月  10 14:20 .
drwxr-xr-x  26 root root   4.0K 1月  26  2018 ..
drwxr-xr-x   3 root root   4.0K 4月  21  2016 acpi
-rw-r--r--   1 root root   3.0K 4月  21  2016 adduser.conf
drwxr-xr-x   2 root root    20K 12月 30  2017 alternatives
-rw-r--r--   1 root root    401 12月 29  2014 anacrontab
-rw-r--r--   1 root root    112 1月  10  2014 apg.conf
drwxr-xr-x   6 root root   4.0K 4月  21  2016 apm
drwxr-xr-x   3 root root   4.0K 12月 30  2017 apparmor
drwxr-xr-x   8 root root   4.0K 1月  26  2018 apparmor.d
drwxr-xr-x   5 root root   4.0K 1月   9  2018 apport
-rw-r--r--   1 root root    389 4月  18  2016 appstream.conf
drwxr-xr-x   6 root root   4.0K 7月  29  2016 apt
drwxr-xr-x   3 root root   4.0K 4月  21  2016 aptdaemon
drwxr-xr-x   2 root root   4.0K 4月  21  2016 at-spi2
drwxr-xr-x   3 root root   4.0K 4月  21  2016 avahi
-rw-r--r--   1 root root   2.2K 9月   1  2015 bash.bashrc
-rw-r--r--   1 root root     45 8月  13  2015 bash_completion
drwxr-xr-x   2 root root   4.0K 1月   9  2018 bash_completion.d
-rw-r--r--   1 root root    367 1月  27  2016 bindresvport.blacklist
drwxr-xr-x   2 root root   4.0K 4月  12  2016 binfmt.d
drwxr-xr-x   2 root root   4.0K 12月 30  2017 bluetooth
drwxr-xr-x   2 root root   4.0K 5月  17  2016 bonobo-activation
-rw-r--r--   1 root root     33 4月  21  2016 brlapi.key
drwxr-xr-x   7 root root   4.0K 4月  21  2016 brltty
-rw-r--r--   1 root root    23K 4月  11  2016 brltty.conf
drwxr-xr-x   3 root root   4.0K 4月  21  2016 ca-certificates
-rw-r--r--   1 root root   8.3K 12月 30  2017 ca-certificates.conf
-rw-r--r--   1 root root   7.7K 4月  21  2016 ca-certificates.conf.dpkg-old
drwxr-xr-x   2 root root   4.0K 4月  21  2016 calendar
drwxr-s---   2 root dip    4.0K 4月  21  2016 chatscripts
drwxr-xr-x   2 root root   4.0K 8月   4  2016 compizconfig
drwxr-xr-x   2 root root   4.0K 8月   4  2016 console-setup
drwxr-xr-x   2 root root   4.0K 4月  21  2016 cracklib
drwxr-xr-x   2 root root   4.0K 8月   4  2016 cron.d
drwxr-xr-x   2 root root   4.0K 1月   9  2018 cron.daily
drwxr-xr-x   2 root root   4.0K 4月  21  2016 cron.hourly
drwxr-xr-x   2 root root   4.0K 4月  21  2016 cron.monthly
--更多--
'''
