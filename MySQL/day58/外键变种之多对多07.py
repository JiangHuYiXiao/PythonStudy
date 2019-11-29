# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/11/29 8:46
# @Software       : Python_study
# @Python_verison : 3.7
'''

drop table if exists t_userinfo;
CREATE TABLE t_userinfo (
	id INT auto_increment PRIMARY KEY,
	user_id INT NOT NULL,
	user_name VARCHAR (20) NOT NULL,
	UNIQUE uq1 (user_id)
) ENGINE = INNODB DEFAULT charset = utf8;

insert into t_userinfo(user_id,user_name) values(12,'李明'),(13,'曹操'),(14,'刘备'),(15,'孙权'),(16,'曹冲');


drop table if exists t_hostinfo;
CREATE TABLE t_hostinfo (
	host_id INT auto_increment PRIMARY KEY,
	host_ip CHAR (20) NOT NULL,
	UNIQUE uq2 (host_id)
) ENGINE = INNODB DEFAULT charset = utf8;

insert into t_hostinfo(host_id,host_ip) values(1,'192.168.3.6'),(2,'192.168.31.6'),(4,'192.168.3.62'),(6,'192.168.3.64'),(7,'192.168.3.6666');


drop table if exists t_user_host_relation;
CREATE TABLE t_user_host_relation (
	id INT auto_increment PRIMARY KEY,
	user_host_id INT NOT NULL,
	host_user_id INT NOT NULL,
	UNIQUE uq3 (user_host_id, host_user_id),
	CONSTRAINT fk_user_host_relation1 FOREIGN KEY(user_host_id) REFERENCES t_userinfo(user_id),
	CONSTRAINT fk_user_host_relation2 FOREIGN KEY(host_user_id) REFERENCES t_hostinfo(host_id)
) ENGINE = INNODB DEFAULT charset = utf8;
insert into t_user_host_relation(user_host_id,host_user_id) values(12,1),(16,1),(14,6),(13,4),(15,6),(15,4);
select * from t_user_host_relation order by id asc;

'''