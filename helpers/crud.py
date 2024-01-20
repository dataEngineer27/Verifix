from datetime import datetime

from sqlalchemy import and_
from sqlalchemy.orm import Session
import models
from sqlalchemy.exc import IntegrityError


def add_timesheet(db: Session, timesheet_list):
    timesheet_list = timesheet_list
    i = 0
    for division in timesheet_list:
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
    print("Length of divisions: ", len(timesheet_list))


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
        employee_id = item['employee_id'] if 'employee_id' in item and item['employee_id'] else None
        staff_id = item['staff_id'] if 'staff_id' in item and item['staff_id'] else None
        created_on = item['created_on'] if 'created_on' in item and item['created_on'] else None
        modified_on = item['modified_on'] if 'modified_on' in item and item['modified_on'] else None
        employee_number = item['employee_number'] if 'employee_number' in item and item['employee_number'] else None
        employee_code = item['employee_code'] if 'employee_code' in item and item['employee_code'] else None
        employee_name = item['employee_name'] if 'employee_name' in item and item['employee_name'] else None
        first_name = item['first_name'] if 'first_name' in item and item['first_name'] else None
        last_name = item['last_name'] if 'last_name' in item and item['last_name'] else None
        middle_name = item['middle_name'] if 'middle_name' in item and item['middle_name'] else None
        gender = item['gender'] if 'gender' in item and item['gender'] else None
        birthday = item['birthday'] if 'birthday' in item and item['birthday'] else None
        address = item['address'] if 'address' in item and item['address'] else None
        main_phone = item['main_phone'] if 'main_phone' in item and item['main_phone'] else None
        tin = item['tin'] if 'tin' in item and item['tin'] else None
        iapa = item['iapa'] if 'iapa' in item and item['iapa'] else None
        npin = item['npin'] if 'npin' in item and item['npin'] else None
        hiring_date = item['hiring_date'] if 'hiring_date' in item and item['hiring_date'] else None
        dismissal_date = item['dismissal_date'] if 'dismissal_date' in item and item['dismissal_date'] else None
        position_id = item['position_id'] if 'position_id' in item and item['position_id'] else None
        division_id = item['division_id'] if 'division_id' in item and item['division_id'] else None
        job_id = item['job_id'] if 'job_id' in item and item['job_id'] else None
        rank_id = item['rank_id'] if 'rank_id' in item and item['rank_id'] else None
        schedule_id = item['schedule_id'] if 'schedule_id' in item and item['schedule_id'] else None
        employee_kind_code = item['employee_kind_code'] if ('employee_kind_code' in item and
                                                            item['employee_kind_code']) else None
        employee_kind_name = item['employee_kind_name'] if ('employee_kind_name' in item and
                                                            item['employee_kind_name']) else None
        employee_state = item['employee_state'] if 'employee_state' in item and item['employee_state'] else None
        fte_id = item['fte_id'] if 'fte_id' in item and item['fte_id'] else None
        query = models.Employees(employee_id=employee_id,
                                 staff_id=staff_id,
                                 created_on=datetime.strptime(created_on, "%d.%m.%Y %H:%M:%S") if created_on else None,
                                 modified_on=datetime.strptime(modified_on, "%d.%m.%Y %H:%M:%S") if modified_on else None,
                                 employee_number=employee_number,
                                 employee_code=employee_code,
                                 employee_name=employee_name,
                                 first_name=first_name,
                                 last_name=last_name,
                                 middle_name=middle_name,
                                 gender=gender,
                                 birthday=datetime.strptime(birthday, "%d.%m.%Y").date() if birthday else None,
                                 address=address,
                                 main_phone=main_phone,
                                 tin=tin,
                                 iapa=iapa,
                                 npin=npin,
                                 hiring_date=datetime.strptime(hiring_date, "%d.%m.%Y").date() if hiring_date else None,
                                 dismissal_date=datetime.strptime(dismissal_date, "%d.%m.%Y").date() if dismissal_date else None,
                                 position_id=position_id,
                                 division_id=division_id,
                                 job_id=job_id,
                                 rank_id=rank_id,
                                 schedule_id=schedule_id,
                                 employee_kind_code=employee_kind_code,
                                 employee_kind_name=employee_kind_name,
                                 employee_state=employee_state,
                                 fte_id=fte_id
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
