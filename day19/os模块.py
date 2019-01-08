# -*- coding:utf-8 -*-
import os

# 1、os.getcwd() 返回当前工作目录
print(os.getcwd())          # F:\PythonStudy\day19

# 2、os.chdir 改变当前脚本的工作目录
os.chdir(r'F:\PythonStudy\day18')  #r取消转义
print(os.getcwd())          # F:\PythonStudy\day18

# 3、os.curdir 返回当前脚本的工作目录，相当于.
print(os.curdir)            # .

# 4、os.pardir 返回当前脚本的父目录，相当于..
print(os.pardir)            # ..

print(os.getcwd())          # F:\PythonStudy\day19
os.chdir('..')
print(os.getcwd())          # F:\PythonStudy

# 5、os.mkdir('dirname')生成单级目录
os.mkdir('jianghu')

# 6、os.rmdir('dirname')生成单级目录
os.rmdir('jianghu')     # 若目录为空，则不能删除


# 7、os.makedirs()     生成多层递归目录
os.makedirs('jianghu/yixiao')

# 8、os.removedirs()     删除多层递归目录
os.removedirs('jianghu/yixiao')     # 若目录为空，则删除，并递归到上一级目录，如若也为空，则删除，依此类推

# 9、os.listdir()        # 列出指定目录下的文件和子目录包括隐藏文件，并以列表方式打印
print(os.listdir(r'F:\PythonStudy'))        # ['.git', '.idea', 'Day01', 'day10', 'day11', 'day12', 'day13', 'day14', 'day15', 'day16', 'day17', 'day18', 'day19', 'Day2', 'Day3', 'day4', 'day5', 'day6', 'day7', 'day8', 'day9', 'README.md', '_config.yml']

# 10、os.stat()获取文件信息、目录信息
print(os.stat(r'F:\PythonStudy\day19'))         # os.stat_result(st_mode=16895, st_ino=5348024557505658, st_dev=4021814972, st_nlink=1, st_uid=0, st_gid=0, st_size=4096, st_atime=1545987267, st_mtime=1545987267, st_ctime=1545042380)
# stat 结构:
# 
# st_mode: inode 保护模式
# st_ino: inode 节点号。
# st_dev: inode 驻留的设备。
# st_nlink: inode 的链接数。
# st_uid: 所有者的用户ID。
# st_gid: 所有者的组ID。
# st_size: 普通文件以字节为单位的大小；包含等待某些特殊文件的数据。
# st_atime: 上次访问的时间。
# st_mtime: 最后一次修改的时间。
# st_ctime: 由操作系统报告的"ctime"。在某些系统上（如Unix）是最新的元数据更改的时间，在其它系统上（如Windows）是创建时间（详细信息参见平台的文档）。

# 11、os.sep()        输出操作系统特定的路径分隔符，win下为'\',linux下为'/'
# print(os.sep)   # \

# 12、os.link()      输出当前平台使用的终止符，win下为'\t\n',linux下为'\n'
print(os.linesep)

# 13、os.pathsep       输出用户分割文件路径字符串，win下为;linux下为:
print(os.pathsep)   # ;

# 14、os.name          输出字符串，指示当前使用平台，win下为nt，linux下为posix
print(os.name)

# 15、运行shell命令
os.system('dir')      # 不需要打印，没有返回值，不能对结果进行操作

ret = os.popen('dir').read()     # 需要打印，有返回值，能对结果进行
print(ret)

# 16、获取系统环境变量
print(os.environ)           # environ({'ALLUSERSPROFILE': 'C:\\ProgramData', 'ANALYSIS_PATH': 'D:\\Auto_Test\\LR12\\', 'ANT_HOME': 'D:\\Auto_Test\\apache-ant-1.9.13', 'APPDATA': 'C:\\Users\\Administrator\\AppData\\Roaming', 'CLASSPATH': 'C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;F:\\JiangHuYiXiao\\Git\\Install Git\\Git\\cmd\\C:\\Python27;D:\\Auto_Test\\apache-ant-1.9.13\\lib', 'COMMONPROGRAMFILES': 'C:\\Program Files\\Common Files', 'COMMONPROGRAMFILES(X86)': 'C:\\Program Files (x86)\\Common Files', 'COMMONPROGRAMW6432': 'C:\\Program Files\\Common Files', 'COMPUTERNAME': 'HSZC1712-0006', 'COMSPEC': 'C:\\Windows\\system32\\cmd.exe', 'FP_NO_HOST_CHECK': 'NO', 'HOMEDRIVE': 'C:', 'HOMEPATH': '\\Users\\Administrator', 'LG_PATH': 'D:\\Auto_Test\\LR12\\', 'LOCALAPPDATA': 'C:\\Users\\Administrator\\AppData\\Local', 'LOGONSERVER': '\\\\HSZC1712-0006', 'LOG_FILE': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp\\\\ihp_custom_batches.log', 'LR_PATH': 'D:\\Auto_Test\\LR12\\', 'NUMBER_OF_PROCESSORS': '4', 'OS': 'Windows_NT', 'PATH': 'C:\\Program Files (x86)\\Common Files\\Oracle\\Java\\javapath;C:\\ProgramData\\Oracle\\Java\\javapath;C:\\Windows\\system32;C:\\Windows;C:\\Windows\\System32\\Wbem;C:\\Windows\\System32\\WindowsPowerShell\\v1.0\\;F:\\JiangHuYiXiao\\Git\\Install Git\\Git\\cmd\\C:\\Python27;D:\\Auto_Test\\apache-ant-1.9.13\\bin;D:\\Auto_Test\\LR12\\strawberry-perl\\perl\\bin;C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\Scripts\\;C:\\Users\\Administrator\\AppData\\Local\\Programs\\Python\\Python37\\', 'PATHEXT': '.COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC', 'PROCESSOR_ARCHITECTURE': 'AMD64', 'PROCESSOR_IDENTIFIER': 'Intel64 Family 6 Model 94 Stepping 3, GenuineIntel', 'PROCESSOR_LEVEL': '6', 'PROCESSOR_REVISION': '5e03', 'PROGRAMDATA': 'C:\\ProgramData', 'PROGRAMFILES': 'C:\\Program Files', 'PROGRAMFILES(X86)': 'C:\\Program Files (x86)', 'PROGRAMW6432': 'C:\\Program Files', 'PSMODULEPATH': 'C:\\Windows\\system32\\WindowsPowerShell\\v1.0\\Modules\\', 'PUBLIC': 'C:\\Users\\Public', 'PYCHARM_HOSTED': '1', 'PYCHARM_MATPLOTLIB_PORT': '4515', 'PYTHONIOENCODING': 'UTF-8', 'PYTHONPATH': 'F:\\PyCharm 2018.2.2\\helpers\\pycharm_matplotlib_backend;F:\\PythonStudy', 'PYTHONUNBUFFERED': '1', 'SESSIONNAME': 'Console', 'SYSTEMDRIVE': 'C:', 'SYSTEMROOT': 'C:\\Windows', 'TEMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp', 'TMP': 'C:\\Users\\ADMINI~1\\AppData\\Local\\Temp', 'USERDOMAIN': 'HSZC1712-0006', 'USERNAME': 'Administrator', 'USERPROFILE': 'C:\\Users\\Administrator', 'VUGEN_PATH': 'D:\\Auto_Test\\LR12\\', 'WINDIR': 'C:\\Windows', 'WINDOWS_TRACING_FLAGS': '3', 'WINDOWS_TRACING_LOGFILE': 'C:\\BVTBin\\Tests\\installpackage\\csilogfile.log'})

# 17、和路径有关的都是在os模块
print(os.path)

# 18、os.path.abspath(path) 返回path规范化的绝对路径
print(os.path.abspath(os.getcwd()))     # F:\PythonStudy\day19

# 19、os.path.split(path) 将path分割成目录和文件名二元组返回
print(os.path.split(os.getcwd()))       # ('F:\\PythonStudy', 'day19')

# 20、os.path.dirname(path) 返回path的目录。其实就是os.path.split(path)的第一个元素
print(os.path.dirname(os.getcwd()))     # F:\PythonStudy

# 21、os.path.basename(path) 返回path的文件。其实就是os.path.split(path)的第二个元素
print(os.path.basename(os.getcwd()))     # day19

# 22、os.path.exists(path)  如果path存在，返回True；如果path不存在，返回False
print(os.path.exists('F:\PythonStudy'))     # True
# 23、os.path.isabs(path)  如果path是绝对路径，返回True
print(os.path.isabs('F:\PythonStudy'))     # True
# 24、os.path.isfile(path)  如果path是一个存在的文件，返回True。否则返回False
print(os.path.isfile('email1'))     # False
# 25、os.path.isdir(path)  如果path是一个存在的目录，则返回True。否则返回False
print(os.path.isdir('PythonStudy'))     # False
# 26、os.path.join(path1[, path2[, ...]])  将多个路径组合后返回，第一个绝对路径之前的参数将被忽略
print(os.path.join('c','user','didi'))          # c\user\didi
# 27、os.path.getatime(path)  返回path所指向的文件或者目录的最后访问时间
print(os.path.getatime('F:\PythonStudy\day19'))
# 28、os.path.getmtime(path)  返回path所指向的文件或者目录的最后修改时间
print(os.path.getmtime('F:\PythonStudy\day19'))
# 29、os.path.getsize(path) 返回path的大小
print(os.path.getsize('F:\PythonStudy\day19'))      # 4096,w文件夹的大小最多4096