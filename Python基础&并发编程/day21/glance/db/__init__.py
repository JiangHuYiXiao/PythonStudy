# 1、绝对导入
import glance.db.models

# 或者
from glance.db import models

# 2、相对导入

from . import models

# 3、导入所有
__all__ = ['models']