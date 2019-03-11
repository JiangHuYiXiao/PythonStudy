# -*- coding:utf-8 -*-
'''
角色:
学校、学员、课程、讲师

要求:
1. 创建北京、上海 2 所学校

2. 创建linux , python , go 3个课程 ， linux\py 在北京开， go 在上海开

3. 课程包含，周期，价格

4. 班级关联课程、讲师

5. 创建学员时，选择学校，关联班级

5. 创建讲师角色时要关联学校

6. 提供三个角色视图

　　6.1 学员视图， 登陆， 查看课程、查看班级

　　6.2 讲师视图， 讲师可查看自己教学的班级、课程。

　　　　　　　　　 进阶需求：可管理自己的班级， 查看班级学员列表 ， 修改所管理的学员的成绩

　　6.3 管理视图，创建讲师， 创建班级，创建课程

7. 上面的操作产生的数据都通过pickle序列化保存到文件里
'''