
from .auth import auth

from .user import user



# 将所有蓝图放入列表中，方便批量注册
blueprints = [auth, user]