from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship

from .database import Base

class Journal(Base):
    __tablename__ = "journals"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=True)
    content = Column(String, nullable=False)
    status = Column(Boolean, server_default='False')# false for draft, true for completed
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")



class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True, index=True)
    password = Column(String, nullable=False)
    username = Column(String, unique=True, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))



class Mood(Base):
    __tablename__ = "moods"

    id = Column(Integer, primary_key=True, nullable=False)
    title = Column(String, nullable=True)
    content = Column(String, nullable=False)
    status = Column(Boolean, server_default='False')# false for draft, true for completed
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)

    owner = relationship("User")
