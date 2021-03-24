import os
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship

Base = declarative_base()


class Test(Base):
    __tablename__ = 'test'

    id = Column('id', Integer, primary_key=True)
    username = Column('username', String, unique=True)


POSTGRES = {
    'user': os.environ.get('POSTGRES_USER'),
    'pw': os.environ.get('POSTGRES_PASSWORD'),
    'db': os.environ.get('POSTGRES_DB'),
    'host': os.environ.get('POSTGRES_HOSTDOCKER'),
    'port': os.environ.get('POSTGRES_PORT'),
}

SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
SECRET_KEY = 'oleh95top95top'
print(SQLALCHEMY_DATABASE_URI)
SQLALCHEMY_TRACK_MODIFICATIONS = False
engine = create_engine(SQLALCHEMY_DATABASE_URI, echo=True)
Base.metadata.create_all(bind=engine)
Session = sessionmaker(bind=engine)
session = Session()
user = Test()
user.id = 0
user.username = 'alice'
session.add(user)
session.commit()
session.close()
