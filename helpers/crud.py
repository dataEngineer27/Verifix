import logging
import uuid

from sqlalchemy import and_
from sqlalchemy.orm import Session
import models
from sqlalchemy.exc import IntegrityError



def add_departments(db: Session, department_list):
    department_list = department_list['corporateItemDtoes']['corporateItemDto']
    i = 0
    for department in department_list:
        i += 1
        id = department['id'] if 'id' in department else None
        parent_id = department['parentId'] if 'parentId' in department else None
        code = department['code'] if 'code' in department else None
        name = department['name'] if 'name' in department else None
        object_type = department['type'] if 'type' in department else None
        tax_payer_id = department['taxpayerIdNumber'] if 'taxpayerIdNumber' in department else None
        query = models.Departments(id=id,
                                   parent_id=parent_id,
                                   code=code,
                                   name=name,
                                   type=object_type,
                                   tax_payer_id=tax_payer_id)
        try:
            db.add(query)
            db.commit()
            print(f"Was inserted {i}-department:  {name}")
        except IntegrityError as e:
            print(f"Was occured error on {i}-department")
            db.rollback()
    print("Length of departments: ", len(department_list))


def add_stores(db: Session, store_list):
    store_list = store_list['corporateItemDtoes']['corporateItemDto']
    i = 0
    for store in store_list:
        i += 1
        id = store['id'] if 'id' in store else None
        department_id = store['parentId'] if 'parentId' in store else None
        code = store['code'] if 'code' in store and store['code'] is not None else None
        name = store['name'] if 'name' in store else None
        type = store['type'] if 'type' in store else None

        query = models.Stores(id=id,
                              department_id=department_id,
                              code=code,
                              name=name,
                              type=type
                              )
        try:
            db.add(query)
            db.commit()
            print(f"Was inserted {i}-store:  {name}")
        except IntegrityError as e:
            print(f"Was occured error on {i}-store")
            db.rollback()  # Rollback the transaction
    print("Length of stores: ", len(store_list))


def add_store_remainings(db: Session, item, current_datetime):
    store_id = item['store'] if 'store' in item else None
    product_id = item['product'] if 'product' in item else None
    amount = item['amount'] if 'amount' in item else None
    sum = item['name'] if 'name' in item else None

    query = models.StoreRemains(store_id=store_id,
                                nomenclature_id=product_id,
                                datetime=current_datetime,
                                amount=amount,
                                sum=sum
                                )
    try:
        db.add(query)
        db.commit()
        print(f"Was inserted item:  {product_id} to {store_id}")
    except IntegrityError as e:
        print(f"Was occured error")
        db.rollback()  # Rollback the transaction


def add_categories(db: Session, category_list):
    for category in category_list:
        query = models.Categories(id=category['id'],
                                  deleted=category['deleted'],
                                  name=category['name'])
        try:
            db.add(query)
            db.commit()
            print(f"Was added category: ", category['name'])
        except IntegrityError as e:
            print(f"Error of category: ", e)
            db.rollback()


def add_groups(db: Session, group_list):
    i = 0
    for group in group_list:
        i += 1
        if group['visibilityFilter'] is not None:
            department_list = group['visibilityFilter']['departments']
        else:
            department_list = None
        query = models.Groups(id=group['id'],
                              deleted=group['deleted'],
                              parent_id=group['parent'],
                              name=group['name'],
                              num=group['num'],
                              code=group['code'],
                              category_id=group['category'],
                              accountingCategory_id=group['accountingCategory'],
                              departments_visibility=department_list
                              )
        try:
            db.add(query)
            db.commit()
            print(f"Was added group-{i}: ", group['name'])
        except IntegrityError as e:
            print(f"Error of group-{i}: ", e)
            db.rollback()
    print("Length of groups: ", len(group_list))


def add_nomenclatures(db: Session, nomenclature_list):
    i = 0
    for nomenclature in nomenclature_list:
        i += 1
        id = nomenclature['id'] if 'id' in nomenclature else None
        group_id = nomenclature['parent'] if 'parent' in nomenclature else None
        category_id = nomenclature['category'] if 'category' in nomenclature else None
        accounting_category = nomenclature['accountingCategory'] if 'accountingCategory' in nomenclature else None
        name = nomenclature['name'] if 'name' in nomenclature else None
        num = nomenclature['num'] if 'num' in nomenclature else None
        code = nomenclature['code'] if 'code' in nomenclature and nomenclature['code'] else None
        main_unit = nomenclature['mainUnit'] if 'mainUnit' in nomenclature else None
        price = nomenclature['defaultSalePrice'] if 'defaultSalePrice' in nomenclature else None
        place_type = nomenclature['placeType'] if 'placeType' in nomenclature else None
        included_in_menu = nomenclature['defaultIncludedInMenu'] if 'defaultIncludedInMenu' in nomenclature else None
        product_type = nomenclature['type'] if 'type' in nomenclature else None
        unit_weight = nomenclature['unitWeight'] if 'unitWeight' in nomenclature else None
        query = models.Nomenclatures(id=id,
                                     group_id=group_id,
                                     category_id=category_id,
                                     accounting_category=accounting_category,
                                     name=name,
                                     num=num,
                                     code=code,
                                     main_unit=main_unit,
                                     price=price,
                                     place_type=place_type,
                                     included_in_menu=included_in_menu,
                                     type=product_type,
                                     unit_weight=unit_weight
                                     )
        try:
            db.add(query)
            db.commit()
            print(f"Was added {i}-product: ", name)
        except IntegrityError as e:
            print(f"Error of {i}-product: ", e)
            db.rollback()  # Rollback the transaction

    print(f"Amount of products: {i}")


def add_units(db: Session, unit_list):
    global type
    i = 0
    for unit in unit_list:
        i += 1
        id = unit['id'] if 'id' in unit else None
        type = unit['rootType'] if 'rootType' in unit else None
        deleted = unit['deleted'] if 'deleted' in unit else None
        code = unit['code'] if 'code' in unit else None
        name = unit['name'] if 'name' in unit else None
        query = models.ReferenceUnits(id=id,
                                      type=type,
                                      deleted=deleted,
                                      code=code,
                                      name=name
                                      )
        try:
            db.add(query)
            db.commit()
            print(f"Was added {i}-unit: ", name)
        except IntegrityError as e:
            print(f"Error of {i}-unit: ", e)
            db.rollback()  # Rollback the transaction
    print(f"Added {i} units for this unit_type: {type}")


def add_roles(db: Session, role_list):
    for role in role_list['employeeRoles']['role']:
        id = role['id'] if 'id' in role else None
        code = role['code'] if 'code' in role else None
        name = role['name'] if 'name' in role else None
        deleted = role['deleted'] if 'deleted' in role else False
        deleted = False if deleted == 'false' else True
        query = models.EmployeeRoles(id=id,
                                     code=code,
                                     name=name,
                                     deleted=deleted
                                     )
        try:
            db.add(query)
            db.commit()
            print("Was added role: ", name)
        except IntegrityError as e:
            print(f"Error of role: ", e)
            db.rollback()


def add_employees(db: Session, employee_list):
    for item in employee_list['employees']['employee']:
        id = item['employee_id'] if 'employee_id' in item else None
        first_name = item['first_name'] if 'first_name' in item else None
        last_name = item['last_name'] if 'last_name' in item else None
        middle_name = item['middle_name'] if 'middle_name' in item else None
        phone_number = item['phone_number'] if 'phone_number' in item else None
        email = item['email'] if 'email' in item else None
        birthday = item['birthday'] if 'birthday' in item else None
        gender = item['gender'] if 'gender' in item else None
        address = item['address'] if 'address' in item else None
        tin = item['tin'] if 'tin' in item else None
        iapa = item['iapa'] if 'iapa' in item else None
        npin = item['npin'] if 'npin' in item else None
        state = item['state'] if 'state' in item else None
        has_identification_photo = item['has_identification_photo'] if 'has_identification_photo' in item else None
        query = models.Employees(id=id,
                                 first_name=first_name,
                                 last_name=last_name,
                                 middle_name=middle_name,
                                 phone_number=phone_number,
                                 email=email,
                                 birthday=birthday,
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


def add_shifts(db: Session, shift_list, department_id):
    for shift in shift_list:
        query = models.ShiftList(id=shift['id'],
                                 session_number=shift['sessionNumber'],
                                 fiscal_number=shift['fiscalNumber'],
                                 cash_reg_number=shift['cashRegNumber'],
                                 cash_reg_serial=shift['cashRegSerial'],
                                 open_date=shift['openDate'],
                                 close_date=shift['closeDate'],
                                 accepted_date=shift['acceptDate'],
                                 manager_id=shift['managerId'],
                                 responsible_user_id=shift['responsibleUserId'],
                                 session_start_cash=shift['sessionStartCash'],
                                 pay_orders=shift['payOrders'],
                                 sum_write_off_orders=shift['sumWriteoffOrders'],
                                 sales_cash=shift['salesCash'],
                                 sales_credit=shift['salesCredit'],
                                 sales_card=shift['salesCard'],
                                 pay_in=shift['payIn'],
                                 pay_out=shift['payOut'],
                                 pay_income=shift['payIncome'],
                                 cash_remain=shift['cashRemain'],
                                 cash_diff=shift['cashDiff'],
                                 session_status=shift['sessionStatus'],
                                 conception_id=shift['conceptionId'],
                                 point_of_sale_id=shift['pointOfSaleId'],
                                 department_id=department_id
                                 )
        try:
            db.add(query)
            db.commit()
            print(f"department: {department_id} ---> {shift['sessionNumber']}")
        except IntegrityError as e:
            print("ERROR WAS OCCURED: ", e)
            db.rollback()  # Rollback the transaction


def add_shift_payments(db: Session, payment):
    order_id = payment['UniqOrderId.Id'] if 'UniqOrderId.Id' in payment else None
    order_num = payment['OrderNum'] if 'OrderNum' in payment else None
    payment_id = payment['PaymentTransaction.Id'] if 'PaymentTransaction.Id' in payment and payment['PaymentTransaction.Id'] else None
    close_time = payment['CloseTime'] if 'CloseTime' in payment else None
    nomenclature_id = payment['DishId'] if 'DishId' in payment else None
    nomenclature = payment['DishName'] if 'DishName' in payment else None
    shift_id = payment['SessionID'] if 'SessionID' in payment else None
    cashier_id = payment['Cashier.Id'] if 'Cashier.Id' in payment else None
    soldwithdish_id = payment['SoldWithDish.Id'] if 'SoldWithDish.Id' in payment else None
    soldwithitem_id = payment['SoldWithItem.Id'] if 'SoldWithItem.Id' in payment else None
    department_id = payment['Department.Id'] if 'Department.Id' in payment else None
    ordertype_id = payment['OrderType.Id'] if 'OrderType.Id' in payment else None
    paymenttype_id = payment['PayTypes.GUID'] if 'PayTypes.GUID' in payment else None
    paymenttype_group = payment['PayTypes.Group'] if 'PayTypes.Group' in payment else None
    payment_type = payment['PayTypes'] if 'PayTypes' in payment else None
    measure_unit = payment['DishMeasureUnit'] if 'DishMeasureUnit' in payment else None
    nomenclature_amount = payment['DishAmountInt'] if 'DishAmountInt' in payment else None
    nomenclature_sum_with_discount = payment['DishDiscountSumInt'] if 'DishDiscountSumInt' in payment else None
    nomenclature_sum = payment['DishSumInt'] if 'DishSumInt' in payment else None
    guest_num = payment['GuestNum'] if 'GuestNum' in payment else None
    guestcard_num = payment['OrderDiscount.GuestCard'] if 'OrderDiscount.GuestCard' in payment else None
    card_num = payment['CardNumber'] if 'CardNumber' in payment else None
    bonuscard_num = payment['Bonus.CardNumber'] if 'Bonus.CardNumber' in payment else None
    counteragent = payment['Counteragent.Name'] if 'Counteragent.Name' in payment else None
    orderdiscount_type_id = payment['OrderDiscount.Type.IDs'].split(", ") if 'OrderDiscount.Type.IDs' in payment and payment['OrderDiscount.Type.IDs'] else None
    orderincrease_type_id = payment['OrderIncrease.Type.IDs'].split(", ") if 'OrderIncrease.Type.IDs' in payment and payment['OrderIncrease.Type.IDs'] else None
    discount_sum = payment['DiscountSum'] if 'DiscountSum' in payment else None
    increase_sum = payment['IncreaseSum'] if 'IncreaseSum' in payment else None
    full_sum = payment['fullSum'] if 'fullSum' in payment else None

    query = models.Payments(department_id=department_id,
                            shift_id=shift_id,
                            order_type_id=ordertype_id,
                            order_id=order_id,
                            order_num=order_num,
                            payment_type_id=paymenttype_id,
                            payment_id=payment_id,
                            payment_type_group=paymenttype_group,
                            payment_type=payment_type,
                            nomenclature_id=nomenclature_id,
                            nomenclature=nomenclature,
                            nomenclature_sum=nomenclature_sum,
                            nomenclature_amount=nomenclature_amount,
                            nomenclature_sum_with_discount=nomenclature_sum_with_discount,
                            discount_sum=discount_sum,
                            increase_sum=increase_sum,
                            full_sum=full_sum,
                            measure_unit=measure_unit,
                            close_time=close_time,
                            sold_with_dish_id=soldwithdish_id,
                            sold_with_item_id=soldwithitem_id,
                            cashier_id=cashier_id,
                            guest_num=guest_num,
                            guest_card=guestcard_num,
                            card_num=card_num,
                            bonus_card=bonuscard_num,
                            counteragent=counteragent,
                            order_discount_type_id=orderdiscount_type_id,
                            order_increase_type_id=orderincrease_type_id,
                            )
    try:
        db.add(query)
        db.commit()
        # print(f"Added payment: {payment_id} of {close_time}")
    except Exception as e:
        print(f"ERROR of {payment_id} - {close_time}\n{e}")
        logging.error("Произошла ошибка: %s", str(e), exc_info=True)
        db.rollback()


def add_store_incoming(db: Session, item):
    doc_number = item['Document'] if 'Document' in item and item['Document'] else None
    incoming_date = item['DateTime.Typed'] if 'DateTime.Typed' in item and item['DateTime.Typed'] else None
    transaction_date = item['DateSecondary.DateTimeTyped'] if 'DateSecondary.DateTimeTyped' in item and item['DateSecondary.DateTimeTyped'] else None
    counteragent_id = item['Counteragent.Id'] if 'Counteragent.Id' in item and item['Counteragent.Id'] else None
    counteragent_type = item['Account.CounteragentType'] if 'Account.CounteragentType' in item and item['Account.CounteragentType'] else None
    store_name = item['Store'] if 'Store' in item and item['Store'] else None
    sum = item['Sum.Incoming'] if 'Sum.Incoming' in item and item['Sum.Incoming'] else None
    measureunit = item['Product.MeasureUnit'] if 'Product.MeasureUnit' in item and item['Product.MeasureUnit'] else None
    nomenclature_id = item['Product.Id'] if 'Product.Id' in item and item['Product.Id'] else None
    amount = item['Amount.In'] if 'Amount.In' in item and item['Amount.In'] else None

    query = models.StoreIncomings(doc_number=doc_number,
                                  incoming_date=incoming_date,
                                  transaction_date=transaction_date,
                                  counteragent_id=counteragent_id,
                                  counteragent_type=counteragent_type,
                                  store_name=store_name,
                                  sum=sum,
                                  measureunit=measureunit,
                                  nomenclature_id=nomenclature_id,
                                  amount=amount)
    try:
        db.add(query)
        db.commit()
        print("Добавлен вещь в склад")
    except IntegrityError as e:
        print("ERROR : \n", e)
        db.rollback()


def add_department_revenue(db: Session, item, department_id):
    date = item['date'] if "date" in item and item['date'] else None
    nomenclature_id = item['productId'] if "productId" in item and item['productId'] else None
    sum = item['value'] if "value" in item and item['value'] else None
    query = models.DepartmentRevenue(department_id=department_id,
                                     nomenclature_id=nomenclature_id,
                                     date=date,
                                     sum=sum)
    db.add(query)
    db.commit()


# def add_product_expense(db: Session, product_expense_list, department):  # not_found_products
#     for i in product_expense_list:
#         product_id = i['productId'] if "productId" in i and i['productId'] else None
#         # try:
#         product_details = get_product(db=db, id=product_id)
#         group_id = product_details.group_id
#         category_id = product_details.category_id
#         main_unit = product_details.main_unit
#         # except:
#         #     not_found_products[f"{department}"] = product_id
#         #     group_id = None
#         #     category_id = None
#         #     main_unit = None
#         date = i['date'] if "date" in i and i['date'] else None
#         name = i['productName'] if "productName" in i and i['productName'] else None
#         quantity = i['value'] if "value" in i and i['value'] else None
#         query = models.ProductExpense(nomenclature_id=product_id,
#                                       category_id=category_id,
#                                       group_id=group_id,
#                                       department_id=department,
#                                       date=date,
#                                       name=name,
#                                       quantity=quantity,
#                                       main_unit=main_unit)
#         try:
#             db.add(query)
#             db.commit()
#             # print("Added expense: ", product_id, date)
#         except IntegrityError as e:
#             db.rollback()
#             # print("ERROR: \n", e)
#
#     # return not_found_products


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
