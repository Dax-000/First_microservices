from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import mapped_column, declarative_base, Mapped, Session

from datetime import datetime


date_fmt = '%d-%m-%Y %H:%M:%S.%f'

engine = create_engine("sqlite:///logs.db")  # , echo=True)
Base = declarative_base()


class Request(Base):
    __tablename__ = 'history'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=True)
    name: Mapped[str] = mapped_column(nullable=False, default="noname")
    date: Mapped[str] = mapped_column(default=datetime.now().strftime(date_fmt))


Base.metadata.create_all(engine)
session = Session(engine)


def add(name):
    session.add(Request(name=name))
    session.commit()


def get_all():
    history = session.execute(select(Request.name, Request.date)).mappings().fetchall()
    return history
