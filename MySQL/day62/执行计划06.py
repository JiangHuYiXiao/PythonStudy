# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/12/19 9:20
# @Software       : Python_study
# @Python_verison : 3.7
# 执行计划：
    # explain + 查询SQL - 用于显示SQL执行信息参数，根据参考信息可以进行SQL优化
'''
id
        查询顺序标识
            如：mysql> explain select * from (select nid,name from tb1 where nid < 10) as B;
            +----+-------------+------------+-------+---------------+---------+---------+------+------+-------------+
            | id | select_type | table      | type  | possible_keys | key     | key_len | ref  | rows | Extra       |
            +----+-------------+------------+-------+---------------+---------+---------+------+------+-------------+
            |  1 | PRIMARY     | <derived2> | ALL   | NULL          | NULL    | NULL    | NULL |    9 | NULL        |
            |  2 | DERIVED     | tb1        | range | PRIMARY       | PRIMARY | 8       | NULL |    9 | Using where |
            +----+-------------+------------+-------+---------------+---------+---------+------+------+-------------+
        特别的：如果使用union连接气值可能为null


    select_type
        查询类型
            SIMPLE          简单查询
            PRIMARY         最外层查询
            SUBQUERY        映射为子查询
            DERIVED         子查询
            UNION           联合
            UNION RESULT    使用联合的结果
            ...
    table
        正在访问的表名


    type
        查询时的访问方式，性能：all < index < range < index_merge < ref_or_null < ref < eq_ref < system/const
            ALL             全表扫描，对于数据表从头到尾找一遍
                            select * from tb1;
                            特别的：如果有limit限制，则找到之后就不在继续向下扫描
                                   select * from tb1 where email = 'seven@live.com'
                                   select * from tb1 where email = 'seven@live.com' limit 1;
                                   虽然上述两个语句都会进行全表扫描，第二句使用了limit，则找到一个后就不再继续扫描。

            INDEX           全索引扫描，对索引从头到尾找一遍
                            select nid from tb1;

            RANGE          对索引列进行范围查找
                            select *  from tb1 where name < 'alex';
                            PS:
                                between and
                                in
                                >   >=  <   <=  操作
                                注意：!= 和 > 符号


            INDEX_MERGE     合并索引，使用多个单列索引搜索
                            select *  from tb1 where name = 'alex' or nid in (11,22,33);

            REF             根据索引查找一个或多个值
                            select *  from tb1 where name = 'seven';

            EQ_REF          连接时使用primary key 或 unique类型
                            select tb2.nid,tb1.name from tb2 left join tb1 on tb2.nid = tb1.nid;



            CONST           常量
                            表最多有一个匹配行,因为仅有一行,在这行的列值可被优化器剩余部分认为是常数,const表很快,因为它们只读取一次。
                            select nid from tb1 where nid = 2 ; 走索引

            SYSTEM          系统
                            表仅有一行(=系统表)。这是const联接类型的一个特例。
                            select * from (select nid from tb1 where nid = 1) as A;
    possible_keys
        可能使用的索引

    key
        真实使用的

    key_len
        MySQL中使用索引字节长度

    rows
        mysql估计为了找到所需的行而要读取的行数 ------ 只是预估值

    extra
        该列包含MySQL解决查询的详细信息
        “Using index”
            此值表示mysql将使用覆盖索引，以避免访问表。不要把覆盖索引和index访问类型弄混了。
        “Using where”
            这意味着mysql服务器将在存储引擎检索行后再进行过滤，许多where条件里涉及索引中的列，当（并且如果）它读取索引时，就能被存储引擎检验，因此不是所有带where子句的查询都会显示“Using where”。有时“Using where”的出现就是一个暗示：查询可受益于不同的索引。
        “Using temporary”
            这意味着mysql在对查询结果排序时会使用一个临时表。
        “Using filesort”
            这意味着mysql会对结果使用一个外部索引排序，而不是按索引次序从表里读取行。mysql有两种文件排序算法，这两种排序方式都可以在内存或者磁盘上完成，explain不会告诉你mysql将使用哪一种文件排序，也不会告诉你排序会在内存里还是磁盘上完成。
        “Range checked for each record(index map: N)”
            这个意味着没有好用的索引，新的索引将在联接的每一行上重新估算，N是显示在possible_keys列中索引的位图，并且是冗余的。
'''