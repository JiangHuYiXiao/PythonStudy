# 1、绝对导入
import glance.cmd.manage
# 或者
from glance.cmd import manage

# 2、相对导入
from . import manage

# 3、导入所有：
'''
__all__ = ['manage']
'''