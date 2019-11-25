# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/25 9:03
# @Software       : Python_study
# @Python_verison : 3.7

# 3、阻塞IO:工作效率低，正常的程序，一次recv没有数据就等，有数据就不等。我们正常用这种
# 2、非阻塞IO:工作效率高，但是CPU负担大，需要多次recv，询问有没有数据，没有就一直询问，直到拿到数据。
# 3、多路复用IO:在有多个对象需要阻塞IO时，能够有效的减少阻塞带来的时间消耗，且在一定程度上能够减少CPU的负担。
# 4、异步IO: 工作效率高，CPU负担小，asynico模块，python写异步IO中比较少。