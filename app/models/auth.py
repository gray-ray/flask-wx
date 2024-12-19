
from . import db

from sqlalchemy.orm import Mapped, mapped_column

from sqlalchemy import String, Integer, ForeignKey,DateTime, TEXT,VARCHAR

import uuid

from datetime import datetime, timezone


class Auth(db.Model):
  __tablename__ = 'auth'

  id: Mapped[str] = mapped_column(String(36), primary_key=True, nullable=False, unique=True,default=lambda: str(uuid.uuid4()))

  user_id: Mapped[int] = mapped_column(Integer,ForeignKey('users.id'),nullable=False)

  token:Mapped[str] = mapped_column(VARCHAR(500),unique=True, nullable=False)

  expires_at:Mapped[str] = mapped_column(String(50), nullable=False)

  created_at:Mapped[datetime] = mapped_column(DateTime, default=lambda: datetime.now(timezone.utc))

  def __repr__(self):
      return f"<Auth {self.id} user_id={self.user_id}>"