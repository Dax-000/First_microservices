from sqlalchemy import create_engine, select, delete
from sqlalchemy.orm import mapped_column, declarative_base, Mapped, Session

from datetime import datetime
from os import getenv


date_fmt = '%d-%m-%Y %H:%M:%S.%f'

# конфиги postgresql из docker-compose
host = getenv('POSTGRES_HOST')
port = getenv('POSTGRES_PORT')
dbname = getenv('POSTGRES_DBNAME')
user = getenv('POSTGRES_USER')
password = getenv('POSTGRES_PASSWORD')

url = f"postgresql://{user}:{password}@{host}:{port}/{dbname}"
engine = create_engine(url)  # , echo=True)
Base = declarative_base()


class Request(Base):
    __tablename__ = 'history_py'
    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True, nullable=True)
    name: Mapped[str] = mapped_column(nullable=False, default="noname")
    date: Mapped[str] = mapped_column(default=datetime.utcnow().strftime(date_fmt))


Base.metadata.create_all(engine)
session = Session(engine)


def add(name):
    try:
        session.add(Request(name=name))
        session.commit()
    except Exception as e:
        print(e)


def get_all():
    history = session.execute(select(Request.name, Request.date)).mappings().fetchall()
    return history
