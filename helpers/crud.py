from datetime import datetime

from sqlalchemy import and_
from sqlalchemy.orm import Session
import models
from sqlalchemy.exc import IntegrityError


def add_divisions(db: Session, division_list):
    division_list = division_list
    i = 0
    for division in division_list:
        i += 1
        id = division['division_id'] if 'division_id' in division and division['division_id'] else None
        name = division['name'] if 'name' in division and division['name'] else None
        parent_id = division['parent_id'] if 'parent_id' in division and division['parent_id'] else None
        opened_date = division['opened_date'] if 'opened_date' in division and division['opened_date'] else None
        closed_date = division['closed_date'] if 'closed_date' in division and division['closed_date'] else None
        code = division['code'] if 'code' in division and division['code'] else None
        state = division['state'] if 'state' in division and division['state'] else None
        query = models.Divisions(id=id,
                                 name=name,
                                 parent_id=parent_id,
                                 opened_date=datetime.strptime(opened_date, "%d.%m.%Y").date() if opened_date else None,
                                 closed_date=datetime.strptime(closed_date, "%d.%m.%Y").date() if closed_date else None,
                                 code=code,
                                 state=state
                                 )
        try:
            db.add(query)
            db.commit()
            print(f"Was inserted {i}-division:  {name}")
        except IntegrityError as e:
            print(f"Was occured error on {i}-division\n{e}")
            db.rollback()
    print("Length of divisions: ", len(division_list))


def add_employees(db: Session, employee_list):
    for item in employee_list:
        id = item['employee_id'] if 'employee_id' in item and item['employee_id'] else None
        first_name = item['first_name'] if 'first_name' in item and item['first_name'] else None
        last_name = item['last_name'] if 'last_name' in item and item['last_name'] else None
        middle_name = item['middle_name'] if 'middle_name' in item and item['middle_name'] else None
        phone_number = item['phone_number'] if 'phone_number' in item and item['phone_number'] else None
        email = item['email'] if 'email' in item and item['email'] else None
        birthday = item['birthday'] if 'birthday' in item and item['birthday'] else None
        gender = item['gender'] if 'gender' in item and item['gender'] else None
        address = item['address'] if 'address' in item and item['address'] else None
        tin = item['tin'] if 'tin' in item and item['tin'] else None
        iapa = item['iapa'] if 'iapa' in item and item['iapa'] else None
        npin = item['npin'] if 'npin' in item and item['npin'] else None
        state = item['state'] if 'state' in item and item['state'] else None
        has_identification_photo = item['has_identification_photo'] if ('has_identification_photo' in item and
                                                                        item['has_identification_photo']) else None
        query = models.Employees(id=id,
                                 first_name=first_name,
                                 last_name=last_name,
                                 middle_name=middle_name,
                                 phone_number=phone_number,
                                 email=email,
                                 birthday=datetime.strptime(birthday, "%d.%m.%Y").date() if birthday else None,
                                 gender=gender,
                                 address=address,
                                 tin=tin,
                                 iapa=iapa,
                                 npin=npin,
                                 state=state,
                                 has_identification_photo=has_identification_photo
                                 )
        try:
            db.add(query)
            db.commit()
            print("Was added employee: ", first_name)
        except IntegrityError as e:
            print(f"\nError of employee:\n{e}\n")
            db.rollback()  # Rollback the transaction


def get_product(db: Session, id):
    query = db.query(models.Nomenclatures).get(id)
    return query


def get_all_departments(db: Session):
    query = db.query(models.Departments).all()
    return query


def get_all_shifts(db: Session):
    query = db.query(models.ShiftList).all()
    return query


def get_all_stores(db: Session):
    query = db.query(models.Stores).all()
    return query


def get_payment_item(db: Session, shift_id, payment_id, nomenclature_id):
    payment_item = db.query(models.Payments).filter(and_(models.Payments.shift_id == shift_id,
                                                         models.Payments.payment_id == payment_id,
                                                         models.Payments.nomenclature_id == nomenclature_id)
                                                    ).first()
    return payment_item


def get_store_remaining_item(db: Session, store_id, nomenclature_id, datetime):
    remaining_item = db.query(models.StoreRemains).filter(and_(models.StoreRemains.store_id == store_id,
                                                               models.StoreRemains.nomenclature_id == nomenclature_id,
                                                               models.StoreRemains.datetime == datetime)
                                                          ).first()
    return remaining_item


def get_store_incoming_item(db: Session, store_name, nomenclature_id, doc_number):
    incoming_item = db.query(models.StoreIncomings).filter(and_(models.StoreIncomings.store_name == store_name,
                                                                models.StoreIncomings.nomenclature_id == nomenclature_id,
                                                                models.StoreIncomings.doc_number == doc_number)
                                                           ).first()
    return incoming_item


def get_revenue_item(db: Session, date, department_id, nomenclature_id):
    revenue_item = db.query(models.DepartmentRevenue).filter(and_(models.DepartmentRevenue.date == date,
                                                                  models.DepartmentRevenue.department_id == department_id,
                                                                  models.DepartmentRevenue.nomenclature_id == nomenclature_id)
                                                             ).first()
    return revenue_item


def get_last_added_payment(db: Session):
    last_payment = db.query(models.Payments).order_by(models.Payments.last_update.desc()).first()
    # last_added_shift = last_payment.shift_id
    return last_payment


def get_last_added_incoming(db: Session):
    last_incoming = db.query(models.StoreIncomings).order_by(models.StoreIncomings.last_update.desc()).first()
    return last_incoming


def get_last_added_store_remaining(db: Session):
    last_item = db.query(models.StoreRemains).order_by(models.StoreRemains.last_update.desc()).first()
    return last_item


def update_department(db: Session, id):
    obj = db.query(models.Departments).get(id)
    obj.is_added = 1
    db.commit()


def update_all_departments_is_added(db: Session, departments):
    for department in departments:
        obj = db.query(models.Departments).get(department.id)
        obj.is_added = 0
        db.commit()


def update_shift(db: Session, id):
    obj = db.query(models.ShiftList).get(id)
    obj.is_added = 1
    db.commit()
