
from . import db

from sqlalchemy.orm import Mapped, mapped_column, relationship

from sqlalchemy import String, Integer,DateTime

from .associations import user_roles

from datetime import datetime, timezone

class User(db.Model): 
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(Integer,primary_key=True,)

    openid: Mapped[str] = mapped_column(String(50), unique=True, nullable=False)

    nickname: Mapped[str] = mapped_column(String(80), nullable=False, unique= True)

    avatar: Mapped[str] = mapped_column(String(200))

    create_time: Mapped[datetime] = mapped_column(DateTime,default= datetime.now(timezone.utc))

    # 与 Role 的多对多关系
    # roles: Mapped[list["Role"]] = relationship(
    #     "Role",
    #     secondary=user_roles,  # 中间表
    #     back_populates="users"  # 反向关系
    # )


    # def __init__(self, nickname, email):
    #     self.nickname = nickname
    #     self.email = email

    # 输出转换
    def to_dict(self):
        return {
            'id': self.id,
            'nickname': self.nickname,
            'openid': self.openid,
            'avatar': self.avatar,
            'create_time': self.create_time,
            # 'roles': [role.to_dict() for role in self.roles] 
        }


    # 删除用户
    def deleteSelf(self):
        db.session.delete(self)
        db.session.commit()
    
    

    # 日志打印调试， 约定方法
    def __repr__(self):
        return f"<User {self.id} {self.openid} {self.nickname}>"