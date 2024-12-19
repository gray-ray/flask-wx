
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


from .user import User

from .role import Role

from .associations import user_roles

from .auth import Auth

__all__ =  ["User", "Role", "user_roles", "Auth"]

