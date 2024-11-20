from sqlalchemy import Column, Integer, String, REAL, ForeignKey
from database import Base

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True, autoincrement=True)
    login = Column(String(50), unique=True, nullable=False)
    password = Column(String(50), nullable=False)
    ipn = Column(Integer, nullable=False)
    full_name = Column(String(50), nullable=False)
    contacs = Column(String(50), nullable=False)
    photo = Column(String(50), nullable=False)
    passport = Column(String(50), nullable=False)

    def __init__(self, login, password, ipn, full_name, contacs, photo, passport):
        self.login = login
        self.password = password
        self.ipn = ipn
        self.full_name = full_name
        self.contacs = contacs
        self.photo = photo
        self.passport = passport

    def __repr__(self):
        return f'<User {self.name!r}>'

    def upload(self, filename):
        pass

class Item(Base):
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    photo = Column(String(50), nullable=False)
    name = Column(String(50), nullable=False)
    description = Column(String(500), nullable=False)
    price_hour = Column(REAL, nullable=False)
    price_day = Column(REAL, nullable=False)
    price_week = Column(REAL, nullable=False)
    price_month = Column(REAL, nullable=False)
    owner = Column(String(50), nullable=True)
    def __init__(self, photo, name, description, price_hour, price_day, price_week, price_months, owner):
        self.photo = photo
        self.name = name
        self.description = description
        self.price_hour = price_hour
        self.price_day = price_day
        self.price_week = price_week
        self.price_month = price_months
        self.owner = owner
    def __repr__(self):
        return f'<Item {self.name!r}>'