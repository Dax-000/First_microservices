from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import mapped_column, declarative_base, Mapped, Session
from datetime import datetime


engine = create_engine("sqlite:///logs.db")  # , echo=True)
Base = declarative_base()


class Request(Base):
    __tablename__ = 'history'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=True)
    name: Mapped[str] = mapped_column(nullable=False, default="noname")
    date: Mapped[datetime] = mapped_column(default=datetime.now)


Base.metadata.create_all(engine)
session = Session(engine)


def add(name):
    session.add(Request(name=name))
    session.commit()

