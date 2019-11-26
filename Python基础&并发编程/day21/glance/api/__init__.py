'''
1、绝对导入：
import glance.api.policy
import glance.api.versions
# 或者
from glance.api import policy
from glance.api import versions

'''
# 2、相对导入：
from . import policy
from . import versions

# 3、导入所有：
'''
#在__init__.py中定义
x=10

def func():
    print('from api.__init.py')

__all__=['x','func','policy','versions']
'''