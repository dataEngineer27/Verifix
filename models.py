from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime, Date, Boolean, BIGINT, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from sqlalchemy.dialects.postgresql import UUID, ARRAY
from datetime import datetime
import uuid
import pytz

timezonetash = pytz.timezone("Asia/Tashkent")

Base = declarative_base()


class Employees(Base):
    __tablename__ = 'employees'
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    middle_name = Column(String, nullable=True)
    phone_number = Column(String, nullable=True)
    email = Column(String, nullable=True)
    birthday = Column(Date, nullable=True)
    gender = Column(String, nullable=True)
    address = Column(Text, nullable=True)
    tin = Column(String, nullable=True)
    iapa = Column(String, nullable=True)
    npin = Column(BIGINT, nullable=True)
    state = Column(String, nullable=True)
    has_identification_photo = Column(String, nullable=True)
    last_update = Column(DateTime(timezone=True), default=func.now())

