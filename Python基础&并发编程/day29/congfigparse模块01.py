# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2019/9/5 15:51
# @Software       : PythonStudy
# @Python_verison : 3.7
# configparse是一个管理配置文件的模块，有自己的规律，必须用中括号括起来，生成的文件格式是ini

# 如果想用python生成一个这样的文档怎么做呢？
# import configparser
#
# config = configparser.ConfigParser()
#
# config["DEFAULT"] = {'ServerAliveInterval': '45',
#                       'Compression': 'yes',
#                      'CompressionLevel': '9',
#                      'ForwardX11':'yes'
#                      }
#
# config['bitbucket.org'] = {'User':'hg'}
#
# config['topsecret.server.com'] = {'Host Port':'50022','ForwardX11':'no'}
#
# with open('example.ini', 'w') as configfile:
#
#    config.write(configfile)



# 查找
# import configparser
#
# config = configparser.ConfigParser()
#
# #---------------------------查找文件内容,基于字典的形式
#
# # print(config.sections())        #  []
# #
# config.read('example.ini')
#
# print(config.sections())        #   ['bitbucket.org', 'topsecret.server.com']
#
# print('bytebong.com' in config) # False
# print('bitbucket.org' in config) # True
#
#
# print(config['bitbucket.org']["user"])  # hg
#
# print(config['DEFAULT']['Compression']) #yes
#
# print(config['topsecret.server.com']['ForwardX11'])  #no
#
#
# print(config['bitbucket.org'])          #<Section: bitbucket.org>
#
# for key in config['bitbucket.org']:     # 注意,有default会默认default的键
#     print(key)
#
# print(config.options('bitbucket.org'))  # 同for循环,找到'bitbucket.org'下所有键
#
# print(config.items('bitbucket.org'))    #找到'bitbucket.org'下所有键值对
#
# print(config.get('bitbucket.org','compression')) # yes       get方法Section下的key对应的value


# 增删改操作
import configparser

config = configparser.ConfigParser()

config.read('example.ini')          # 读文件

config.add_section('yuan')          # 增加一个section



config.remove_section('bitbucket.org')          # 删除一个section
config.remove_option('topsecret.server.com',"forwardx11")           # 删除一个配置项


config.set('topsecret.server.com','k1','11111')   # 在section，topsecret.server.com中增加一个配置项
config.set('yuan','k2','22222')

config.write(open('new2.ini', "w"))         # 写进文件，所有的修改都在一个新的文件里面