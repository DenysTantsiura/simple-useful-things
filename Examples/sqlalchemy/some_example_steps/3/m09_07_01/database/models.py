from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, func, event
from sqlalchemy.orm import declarative_base, relationship

from database.db import engine

Base = declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    login = Column(String(25), unique=True)
    password = Column(String(25))


class Todo(Base):
    __tablename__ = 'todos'
    id = Column(Integer, primary_key=True)
    title = Column(String(150), nullable=False, index=True)
    description = Column(String(150), nullable=False, index=True)
    created_at = Column(DateTime, default=func.now())  # коли створено запис
    updated_at = Column(DateTime, default=func.now())  # коли оновлено запис. (хук... івент - @event)
    user_id = Column('user_id', Integer, ForeignKey('users.id'))  # 'user_id' для назви колонки в БД, а user_id - для використання в коді Пайтона
    user = relationship(User)


@event.listens_for(Todo, 'before_update')
def update_updated_at(mapper, conn, target):  # мапер - спец об'єкт, конекшн, Todo
    target.updated_at = func.now()  # для оновлення при оновленні а не при створенні лише.


Base.metadata.create_all(engine)
