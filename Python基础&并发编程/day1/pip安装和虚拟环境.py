# -*- coding:utf-8 -*-
# @Author         : 江湖一笑
# @Time           : 2021/8/11 8:22
# @Software       : Python_study
# @Python_verison : 3.7

# 安装pip
    # python2.7之前版本安装pip需要切换到easy_install.exe目录下执行easy_install.exe pip
    # Python 2.7.9 + 或 Python 3.4+ 以上版本都自带 pip 工具。
    # 安装后，使用pip --version查看匹配的安装是否成功以及对应的版本信息

# 使用pip安装库
    # 安装pip后，后面我们需要安装其他python库的时候就只需要使用pip进行安装就可以例如：pip install selenium，这样是默认安装最新的selenium版本。
    # 如果需要安装指定的selenium版本则需要使用命令：pip install selenium==3.10.0

# 使用pip卸载库：
    # pip uninstall <包名>


# 虚拟环境创建:
    # 在 python3.3 之前，只能通过 virtualenv 创建虚拟环境，首先需要安装 virtualenv
    # pip install virtualenv
    # 安装完后，在当前目录下创建一个名为 myvenv 的虚拟环境:
    # virtualenv --no-site-packages myvenv
    # 参数 --no-site-packages 的意思是创建虚拟环境时，不复制主环境中安装的第三方包，也就是创建一个 “干净的” 虚拟环境

# Python3.3 之后，可以用模块 venv 代替 virtualenv 工具，好处是不用单独安装，3.3 及之后的版本，都可以通过安装好的 Python 来创建虚拟环境:
# python -m venv myvenv
# 可以在当前目录创建一个名为 myvenv 的虚拟环境

# 激活虚拟环境
# windows：myvenv\Scripts\activate.bat

# 关闭虚拟环境：
# deactivate


# 使用pycharm创建虚拟环境
    # new project
    # new environment using,
    # location设置环境地址
    # interpreter编译器
    # inherit global site-package  使用现有环境的所有库
    # make available all to projects   应用到所有项目中    一般这两个选项不勾选
