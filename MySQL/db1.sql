/*
Navicat MySQL Data Transfer

Source Server         : mysql
Source Server Version : 50505
Source Host           : localhost:3306
Source Database       : db1

Target Server Type    : MYSQL
Target Server Version : 50505
File Encoding         : 65001

Date: 2019-11-29 14:57:32
*/

SET FOREIGN_KEY_CHECKS=0;

-- ----------------------------
-- Table structure for addrs
-- ----------------------------
DROP TABLE IF EXISTS `addrs`;
CREATE TABLE `addrs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(20) DEFAULT NULL,
  `age` char(4) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of addrs
-- ----------------------------
INSERT INTO `addrs` VALUES ('1', 'zhongguojizhang', '18');
INSERT INTO `addrs` VALUES ('2', 'zhongguojizhang1', '18');

-- ----------------------------
-- Table structure for addrs_info
-- ----------------------------
DROP TABLE IF EXISTS `addrs_info`;
CREATE TABLE `addrs_info` (
  `id` int(11) NOT NULL,
  `name` varchar(32) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of addrs_info
-- ----------------------------

-- ----------------------------
-- Table structure for ats_info
-- ----------------------------
DROP TABLE IF EXISTS `ats_info`;
CREATE TABLE `ats_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(30) NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`department_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ats_info
-- ----------------------------

-- ----------------------------
-- Table structure for ats_t
-- ----------------------------
DROP TABLE IF EXISTS `ats_t`;
CREATE TABLE `ats_t` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(30) NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`,`department_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of ats_t
-- ----------------------------

-- ----------------------------
-- Table structure for t1
-- ----------------------------
DROP TABLE IF EXISTS `t1`;
CREATE TABLE `t1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `NAME` varchar(10) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t1
-- ----------------------------
INSERT INTO `t1` VALUES ('1', 'jianghuyix');
INSERT INTO `t1` VALUES ('2', 'jianghu');
INSERT INTO `t1` VALUES ('3', '32');
INSERT INTO `t1` VALUES ('4', 'sdf');
INSERT INTO `t1` VALUES ('5', 'w4r');

-- ----------------------------
-- Table structure for t1_department
-- ----------------------------
DROP TABLE IF EXISTS `t1_department`;
CREATE TABLE `t1_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `t1_department_name` varchar(30) NOT NULL,
  `t1_department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `t1_department_id` (`t1_department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t1_department
-- ----------------------------
INSERT INTO `t1_department` VALUES ('1', '研发部', '11');
INSERT INTO `t1_department` VALUES ('2', '考勤部', '12');
INSERT INTO `t1_department` VALUES ('3', '假期部', '13');

-- ----------------------------
-- Table structure for t1_foreign_key
-- ----------------------------
DROP TABLE IF EXISTS `t1_foreign_key`;
CREATE TABLE `t1_foreign_key` (
  `t1_id` int(11) NOT NULL AUTO_INCREMENT,
  `t1_pid` int(11) NOT NULL,
  `t1_name` varchar(20) NOT NULL,
  PRIMARY KEY (`t1_id`,`t1_pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t1_foreign_key
-- ----------------------------

-- ----------------------------
-- Table structure for t1_user_info
-- ----------------------------
DROP TABLE IF EXISTS `t1_user_info`;
CREATE TABLE `t1_user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `t1_user_name` varchar(20) NOT NULL,
  `t1_user_department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `fk_t1_user_department` (`t1_user_department_id`),
  CONSTRAINT `fk_t1_user_department` FOREIGN KEY (`t1_user_department_id`) REFERENCES `t1_department` (`t1_department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t1_user_info
-- ----------------------------
INSERT INTO `t1_user_info` VALUES ('6', 'huhu', '11');
INSERT INTO `t1_user_info` VALUES ('7', 'jiangjiang', '12');
INSERT INTO `t1_user_info` VALUES ('8', 'kao', '13');
INSERT INTO `t1_user_info` VALUES ('9', 'zhu', '13');
INSERT INTO `t1_user_info` VALUES ('10', 'niu', '13');

-- ----------------------------
-- Table structure for t2_foreign_key
-- ----------------------------
DROP TABLE IF EXISTS `t2_foreign_key`;
CREATE TABLE `t2_foreign_key` (
  `t2_id` int(11) NOT NULL AUTO_INCREMENT,
  `t2_pid` int(11) NOT NULL,
  `t2_name` varchar(20) NOT NULL,
  PRIMARY KEY (`t2_id`),
  KEY `fk_t2_t1` (`t2_id`,`t2_pid`),
  CONSTRAINT `fk_t2_t1` FOREIGN KEY (`t2_id`, `t2_pid`) REFERENCES `t1_foreign_key` (`t1_id`, `t1_pid`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t2_foreign_key
-- ----------------------------

-- ----------------------------
-- Table structure for t_blog_user
-- ----------------------------
DROP TABLE IF EXISTS `t_blog_user`;
CREATE TABLE `t_blog_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(30) NOT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq1` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_blog_user
-- ----------------------------
INSERT INTO `t_blog_user` VALUES ('1', 'zibaoba', '11');
INSERT INTO `t_blog_user` VALUES ('2', '人生', '365');
INSERT INTO `t_blog_user` VALUES ('7', 'jiangtao_jiang', '110');
INSERT INTO `t_blog_user` VALUES ('8', 'tao_jiang', '111');
INSERT INTO `t_blog_user` VALUES ('9', 'jiangtao', '112');
INSERT INTO `t_blog_user` VALUES ('10', 'jianghu', '115');
INSERT INTO `t_blog_user` VALUES ('11', 'taotao', '113');
INSERT INTO `t_blog_user` VALUES ('12', 'taobao', '114');

-- ----------------------------
-- Table structure for t_bolg_user
-- ----------------------------
DROP TABLE IF EXISTS `t_bolg_user`;
CREATE TABLE `t_bolg_user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(30) NOT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_bolg_user
-- ----------------------------

-- ----------------------------
-- Table structure for t_class
-- ----------------------------
DROP TABLE IF EXISTS `t_class`;
CREATE TABLE `t_class` (
  `class_id` int(11) NOT NULL AUTO_INCREMENT,
  `caption` varchar(20) NOT NULL,
  PRIMARY KEY (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_class
-- ----------------------------
INSERT INTO `t_class` VALUES ('1', '三年二班');
INSERT INTO `t_class` VALUES ('2', '三年三班');
INSERT INTO `t_class` VALUES ('3', '一年二班');
INSERT INTO `t_class` VALUES ('4', '二年九班');

-- ----------------------------
-- Table structure for t_cnblogs
-- ----------------------------
DROP TABLE IF EXISTS `t_cnblogs`;
CREATE TABLE `t_cnblogs` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `blog_addr` varchar(40) NOT NULL,
  `cnblogs_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `blog_addr` (`blog_addr`),
  UNIQUE KEY `cnblogs_user_id` (`cnblogs_user_id`),
  CONSTRAINT `fk_user_cnblogs` FOREIGN KEY (`cnblogs_user_id`) REFERENCES `t_blog_user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_cnblogs
-- ----------------------------
INSERT INTO `t_cnblogs` VALUES ('5', 'yixifsdfu', '111');
INSERT INTO `t_cnblogs` VALUES ('6', 'sdf', '112');

-- ----------------------------
-- Table structure for t_course
-- ----------------------------
DROP TABLE IF EXISTS `t_course`;
CREATE TABLE `t_course` (
  `course_id` int(11) NOT NULL AUTO_INCREMENT,
  `course_name` char(10) NOT NULL,
  `c_teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`course_id`),
  KEY `fk_course_teacher` (`c_teacher_id`),
  CONSTRAINT `fk_course_teacher` FOREIGN KEY (`c_teacher_id`) REFERENCES `t_teacher` (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_course
-- ----------------------------
INSERT INTO `t_course` VALUES ('1', '生物', '1');
INSERT INTO `t_course` VALUES ('2', '物理', '2');
INSERT INTO `t_course` VALUES ('3', '物理', '3');
INSERT INTO `t_course` VALUES ('4', '美术', '3');

-- ----------------------------
-- Table structure for t_department
-- ----------------------------
DROP TABLE IF EXISTS `t_department`;
CREATE TABLE `t_department` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `department_name` varchar(30) NOT NULL,
  `department_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `department_id` (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=14 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_department
-- ----------------------------
INSERT INTO `t_department` VALUES ('1', '研发部', '1');
INSERT INTO `t_department` VALUES ('2', '运维部', '2');
INSERT INTO `t_department` VALUES ('3', '销售部', '3');
INSERT INTO `t_department` VALUES ('4', '后勤部', '4');
INSERT INTO `t_department` VALUES ('5', '市场部', '5');
INSERT INTO `t_department` VALUES ('6', 'x', '22');
INSERT INTO `t_department` VALUES ('7', '测试部', '6');
INSERT INTO `t_department` VALUES ('11', '测试部', '60');
INSERT INTO `t_department` VALUES ('12', '测试部', '7');
INSERT INTO `t_department` VALUES ('13', '需求部', '8');

-- ----------------------------
-- Table structure for t_hostinfo
-- ----------------------------
DROP TABLE IF EXISTS `t_hostinfo`;
CREATE TABLE `t_hostinfo` (
  `host_id` int(11) NOT NULL AUTO_INCREMENT,
  `host_ip` char(20) NOT NULL,
  PRIMARY KEY (`host_id`),
  UNIQUE KEY `uq2` (`host_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_hostinfo
-- ----------------------------
INSERT INTO `t_hostinfo` VALUES ('1', '192.168.3.6');
INSERT INTO `t_hostinfo` VALUES ('2', '192.168.31.6');
INSERT INTO `t_hostinfo` VALUES ('4', '192.168.3.62');
INSERT INTO `t_hostinfo` VALUES ('6', '192.168.3.64');
INSERT INTO `t_hostinfo` VALUES ('7', '192.168.3.6666');

-- ----------------------------
-- Table structure for t_index1
-- ----------------------------
DROP TABLE IF EXISTS `t_index1`;
CREATE TABLE `t_index1` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num` int(11) NOT NULL,
  `name1` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq1` (`num`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_index1
-- ----------------------------
INSERT INTO `t_index1` VALUES ('10', '1', '江西');
INSERT INTO `t_index1` VALUES ('11', '2', '江湖');

-- ----------------------------
-- Table structure for t_index2
-- ----------------------------
DROP TABLE IF EXISTS `t_index2`;
CREATE TABLE `t_index2` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `num` int(11) NOT NULL,
  `name1` varchar(30) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq1` (`name1`,`num`)
) ENGINE=InnoDB AUTO_INCREMENT=16 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_index2
-- ----------------------------
INSERT INTO `t_index2` VALUES ('12', '1', '江哥');
INSERT INTO `t_index2` VALUES ('13', '2', '江姐');
INSERT INTO `t_index2` VALUES ('11', '2', '江湖');
INSERT INTO `t_index2` VALUES ('10', '1', '江西');

-- ----------------------------
-- Table structure for t_score
-- ----------------------------
DROP TABLE IF EXISTS `t_score`;
CREATE TABLE `t_score` (
  `score_id` int(11) NOT NULL AUTO_INCREMENT,
  `score_student_id` int(11) NOT NULL,
  `score_course_id` int(11) NOT NULL,
  `score_number` int(11) NOT NULL,
  PRIMARY KEY (`score_id`),
  UNIQUE KEY `uq` (`score_student_id`,`score_course_id`),
  KEY `fk_score_course` (`score_course_id`),
  CONSTRAINT `fk_score_course` FOREIGN KEY (`score_course_id`) REFERENCES `t_course` (`course_id`),
  CONSTRAINT `fk_score_student` FOREIGN KEY (`score_student_id`) REFERENCES `t_student` (`s_id`)
) ENGINE=InnoDB AUTO_INCREMENT=53 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_score
-- ----------------------------
INSERT INTO `t_score` VALUES ('1', '1', '1', '10');
INSERT INTO `t_score` VALUES ('2', '1', '2', '9');
INSERT INTO `t_score` VALUES ('5', '1', '4', '66');
INSERT INTO `t_score` VALUES ('6', '2', '1', '8');
INSERT INTO `t_score` VALUES ('8', '2', '3', '68');
INSERT INTO `t_score` VALUES ('9', '2', '4', '99');
INSERT INTO `t_score` VALUES ('10', '3', '1', '77');
INSERT INTO `t_score` VALUES ('11', '3', '2', '66');
INSERT INTO `t_score` VALUES ('12', '3', '3', '87');
INSERT INTO `t_score` VALUES ('13', '3', '4', '99');
INSERT INTO `t_score` VALUES ('14', '4', '1', '79');
INSERT INTO `t_score` VALUES ('15', '4', '2', '11');
INSERT INTO `t_score` VALUES ('16', '4', '3', '67');
INSERT INTO `t_score` VALUES ('17', '4', '4', '100');
INSERT INTO `t_score` VALUES ('18', '5', '1', '79');
INSERT INTO `t_score` VALUES ('19', '5', '2', '11');
INSERT INTO `t_score` VALUES ('20', '5', '3', '67');
INSERT INTO `t_score` VALUES ('21', '5', '4', '100');
INSERT INTO `t_score` VALUES ('22', '6', '1', '9');
INSERT INTO `t_score` VALUES ('23', '6', '2', '100');
INSERT INTO `t_score` VALUES ('24', '6', '3', '67');
INSERT INTO `t_score` VALUES ('25', '6', '4', '100');
INSERT INTO `t_score` VALUES ('26', '7', '1', '9');
INSERT INTO `t_score` VALUES ('27', '7', '2', '100');
INSERT INTO `t_score` VALUES ('28', '7', '3', '67');
INSERT INTO `t_score` VALUES ('29', '7', '4', '88');
INSERT INTO `t_score` VALUES ('30', '8', '1', '9');
INSERT INTO `t_score` VALUES ('31', '8', '2', '100');
INSERT INTO `t_score` VALUES ('32', '8', '3', '67');
INSERT INTO `t_score` VALUES ('33', '8', '4', '88');
INSERT INTO `t_score` VALUES ('34', '9', '1', '91');
INSERT INTO `t_score` VALUES ('35', '9', '2', '88');
INSERT INTO `t_score` VALUES ('36', '9', '3', '67');
INSERT INTO `t_score` VALUES ('37', '9', '4', '22');
INSERT INTO `t_score` VALUES ('38', '10', '1', '90');
INSERT INTO `t_score` VALUES ('39', '10', '2', '77');
INSERT INTO `t_score` VALUES ('40', '10', '3', '43');
INSERT INTO `t_score` VALUES ('41', '10', '4', '87');
INSERT INTO `t_score` VALUES ('42', '11', '1', '90');
INSERT INTO `t_score` VALUES ('43', '11', '2', '77');
INSERT INTO `t_score` VALUES ('44', '11', '3', '43');
INSERT INTO `t_score` VALUES ('45', '11', '4', '87');
INSERT INTO `t_score` VALUES ('46', '12', '1', '90');
INSERT INTO `t_score` VALUES ('47', '12', '2', '77');
INSERT INTO `t_score` VALUES ('48', '12', '3', '43');
INSERT INTO `t_score` VALUES ('49', '12', '4', '87');
INSERT INTO `t_score` VALUES ('52', '13', '3', '87');

-- ----------------------------
-- Table structure for t_student
-- ----------------------------
DROP TABLE IF EXISTS `t_student`;
CREATE TABLE `t_student` (
  `s_id` int(11) NOT NULL AUTO_INCREMENT,
  `gender` char(2) NOT NULL,
  `s_class_id` int(11) NOT NULL,
  `sname` varchar(20) NOT NULL,
  PRIMARY KEY (`s_id`),
  KEY `fk_student_class` (`s_class_id`),
  CONSTRAINT `fk_student_class` FOREIGN KEY (`s_class_id`) REFERENCES `t_class` (`class_id`)
) ENGINE=InnoDB AUTO_INCREMENT=17 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_student
-- ----------------------------
INSERT INTO `t_student` VALUES ('1', '男', '1', '理解');
INSERT INTO `t_student` VALUES ('2', '女', '1', '钢蛋');
INSERT INTO `t_student` VALUES ('3', '男', '1', '张三');
INSERT INTO `t_student` VALUES ('4', '男', '1', '张一');
INSERT INTO `t_student` VALUES ('5', '女', '1', '张二');
INSERT INTO `t_student` VALUES ('6', '男', '1', '张四');
INSERT INTO `t_student` VALUES ('7', '女', '2', '铁锤');
INSERT INTO `t_student` VALUES ('8', '男', '2', '李三');
INSERT INTO `t_student` VALUES ('9', '男', '2', '李一');
INSERT INTO `t_student` VALUES ('10', '女', '2', '李二');
INSERT INTO `t_student` VALUES ('11', '男', '2', '李四');
INSERT INTO `t_student` VALUES ('12', '女', '3', '如花');
INSERT INTO `t_student` VALUES ('13', '男', '3', '刘三');
INSERT INTO `t_student` VALUES ('14', '男', '3', '刘一');
INSERT INTO `t_student` VALUES ('15', '女', '3', '刘二');
INSERT INTO `t_student` VALUES ('16', '男', '3', '刘四');

-- ----------------------------
-- Table structure for t_teacher
-- ----------------------------
DROP TABLE IF EXISTS `t_teacher`;
CREATE TABLE `t_teacher` (
  `teacher_id` int(11) NOT NULL AUTO_INCREMENT,
  `tname` varchar(18) NOT NULL,
  PRIMARY KEY (`teacher_id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_teacher
-- ----------------------------
INSERT INTO `t_teacher` VALUES ('1', '张磊老师');
INSERT INTO `t_teacher` VALUES ('2', '李平老师');
INSERT INTO `t_teacher` VALUES ('3', '刘海燕老师');
INSERT INTO `t_teacher` VALUES ('4', '朱云海老师');
INSERT INTO `t_teacher` VALUES ('5', '李杰老师');

-- ----------------------------
-- Table structure for t_user
-- ----------------------------
DROP TABLE IF EXISTS `t_user`;
CREATE TABLE `t_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `uname` varchar(20) NOT NULL,
  `depart_id` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_user
-- ----------------------------

-- ----------------------------
-- Table structure for t_userinfo
-- ----------------------------
DROP TABLE IF EXISTS `t_userinfo`;
CREATE TABLE `t_userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `user_name` varchar(20) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq1` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_userinfo
-- ----------------------------
INSERT INTO `t_userinfo` VALUES ('6', '12', '李明');
INSERT INTO `t_userinfo` VALUES ('7', '13', '曹操');
INSERT INTO `t_userinfo` VALUES ('8', '14', '刘备');
INSERT INTO `t_userinfo` VALUES ('9', '15', '孙权');
INSERT INTO `t_userinfo` VALUES ('10', '16', '曹冲');

-- ----------------------------
-- Table structure for t_user_host_relation
-- ----------------------------
DROP TABLE IF EXISTS `t_user_host_relation`;
CREATE TABLE `t_user_host_relation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_host_id` int(11) NOT NULL,
  `host_user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `uq3` (`user_host_id`,`host_user_id`),
  KEY `fk_user_host_relation2` (`host_user_id`),
  CONSTRAINT `fk_user_host_relation1` FOREIGN KEY (`user_host_id`) REFERENCES `t_userinfo` (`user_id`),
  CONSTRAINT `fk_user_host_relation2` FOREIGN KEY (`host_user_id`) REFERENCES `t_hostinfo` (`host_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_user_host_relation
-- ----------------------------
INSERT INTO `t_user_host_relation` VALUES ('1', '12', '1');
INSERT INTO `t_user_host_relation` VALUES ('4', '13', '4');
INSERT INTO `t_user_host_relation` VALUES ('3', '14', '6');
INSERT INTO `t_user_host_relation` VALUES ('6', '15', '4');
INSERT INTO `t_user_host_relation` VALUES ('5', '15', '6');
INSERT INTO `t_user_host_relation` VALUES ('2', '16', '1');

-- ----------------------------
-- Table structure for t_user_info
-- ----------------------------
DROP TABLE IF EXISTS `t_user_info`;
CREATE TABLE `t_user_info` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `user_name` varchar(30) NOT NULL,
  `user_department_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  KEY `fk_user_department` (`user_department_id`),
  CONSTRAINT `fk_user_department` FOREIGN KEY (`user_department_id`) REFERENCES `t_department` (`department_id`)
) ENGINE=InnoDB AUTO_INCREMENT=10 DEFAULT CHARSET=utf8;

-- ----------------------------
-- Records of t_user_info
-- ----------------------------
INSERT INTO `t_user_info` VALUES ('1', '11', '小明', '1');
INSERT INTO `t_user_info` VALUES ('2', '12', '小可', '2');
INSERT INTO `t_user_info` VALUES ('3', '13', '的函', '1');
INSERT INTO `t_user_info` VALUES ('4', '14', 'kobe', '3');
INSERT INTO `t_user_info` VALUES ('5', '15', '小妹', '4');
INSERT INTO `t_user_info` VALUES ('6', '16', '科比', '3');
INSERT INTO `t_user_info` VALUES ('7', '9', 'king', '5');
INSERT INTO `t_user_info` VALUES ('8', '10', 'job', '3');
INSERT INTO `t_user_info` VALUES ('9', '111', 'dd', null);

-- ----------------------------
-- Table structure for user_info
-- ----------------------------
DROP TABLE IF EXISTS `user_info`;
CREATE TABLE `user_info` (
  `id` int(11) DEFAULT NULL,
  `name` char(1) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- ----------------------------
-- Records of user_info
-- ----------------------------
INSERT INTO `user_info` VALUES ('22', 'x');
