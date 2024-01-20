from sqlalchemy import Column, Integer, String, ForeignKey, DECIMAL, DateTime, Date, Boolean, BIGINT, Text, JSON
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
    employee_id = Column(Integer, primary_key=True)
    staff_id = Column(Integer, nullable=True)
    created_on = Column(DateTime, nullable=True)
    modified_on = Column(DateTime, nullable=True)
    employee_number = Column(String, nullable=True)
    employee_code = Column(String, nullable=True)
    employee_name = Column(String, nullable=True)
    first_name = Column(String, nullable=True)
    last_name = Column(String, nullable=True)
    middle_name = Column(String, nullable=True)
    gender = Column(String, nullable=True)
    birthday = Column(Date, nullable=True)
    address = Column(Text, nullable=True)
    main_phone = Column(String, nullable=True)
    tin = Column(String, nullable=True)
    iapa = Column(String, nullable=True)
    npin = Column(String, nullable=True)
    hiring_date = Column(Date, nullable=True)
    dismissal_date = Column(Date, nullable=True)
    position_id = Column(Integer, nullable=True)
    division_id = Column(Integer, nullable=True)
    job_id = Column(Integer, nullable=True)
    rank_id = Column(Integer, nullable=True)
    schedule_id = Column(Integer, nullable=True)
    employee_kind_code = Column(String, nullable=True)
    employee_kind_name = Column(String, nullable=True)
    employee_state = Column(String, nullable=True)
    fte_id = Column(Integer, nullable=True)
    last_update = Column(DateTime(timezone=True), default=func.now())


class Divisions(Base):
    __tablename__ = 'divisions'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    parent_id = Column(Integer, nullable=True)
    opened_date = Column(Date, nullable=True)
    closed_date = Column(Date, nullable=True)
    code = Column(String, nullable=True)
    state = Column(String, nullable=True)
    last_update = Column(DateTime(timezone=True), default=func.now())


class Timesheet(Base):
    __tablename__ = 'timesheets'
    id = Column(BIGINT, autoincrement=True, primary_key=True)
    staff_id = Column(Integer, nullable=False)
    employee_id = Column(Integer, index=True, nullable=False)
    date = Column(Date, nullable=False)
    day_kind = Column(String, nullable=True)
    plan_time = Column(Integer, nullable=True)
    done_marks = Column(Integer, nullable=True)
    planned_marks = Column(Integer, nullable=True)
    begin_time = Column(DateTime, nullable=True)
    end_time = Column(DateTime, nullable=True)
    break_begin_time = Column(DateTime, nullable=True)
    break_end_time = Column(DateTime, nullable=True)
    input_time = Column(DateTime, nullable=False)
    output_time = Column(DateTime, nullable=False)
    facts = Column(ARRAY(JSON), nullable=True)
    last_update = Column(DateTime(timezone=True), default=func.now())

