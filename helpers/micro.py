import requests
import os
import xmltodict
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth


load_dotenv()
PASSWORD = os.environ.get('PASSWORD')
LOGIN = os.environ.get('LOGIN')
BASE_URL = os.environ.get('BASE_URL')


def login():
    data = requests.get(f"{BASE_URL}/resto/api/auth?login={LOGIN}&pass={PASSWORD}")
    key = data.text
    return key


def logout(key):
    data = requests.get(f"{BASE_URL}/resto/api/logout?key={key}")
    print(data.text)


# def department_list(key):
#     departments = requests.get(f"{BASE_URL}/resto/api/corporation/departments?key={key}&includeDeleted=true")
#     root = ET.fromstring(departments.content)
#     corporate_item_dtos = root.findall('corporateItemDto')
#     return corporate_item_dtos


def department_list(key):
    url = f"{BASE_URL}/resto/api/corporation/departments?key={key}"
    res = requests.get(url=url)
    data_xml = res.text
    data_dict = xmltodict.parse(data_xml)
    return data_dict


def store_list(key):
    url = f"{BASE_URL}/resto/api/corporation/stores?key={key}&includeDeleted=true"
    res = requests.get(url=url)
    data_xml = res.text
    data_dict = xmltodict.parse(data_xml)
    return data_dict


def store_remainings(key, date, time):
    url = f"{BASE_URL}/resto/api/v2/reports/balance/stores?key={key}&timestamp={date}T15:50:00"
    res = requests.get(url=url)
    return res.json()


def category_list(key):
    categories = requests.get(f"{BASE_URL}/resto/api/v2/entities/products/category/list?key={key}")
    return categories.json()


def nomenclature_groups(key):
    groups = requests.get(f"{BASE_URL}/resto/api/v2/entities/products/group/list?key={key}")
    return groups.json()


# def nomenclature_list(key):
#     tools = requests.get(f"{BASE_URL}/resto/api/v2/entities/products/list?includeDeleted=true&key={key}")
#     root = ET.fromstring(tools.content)
#     product_item_dtos = root.findall('productDto')
#     return product_item_dtos

def unit_list(root_type, key):
    units = requests.get(f"{BASE_URL}/resto/api/v2/entities/list?rootType={root_type}&key={key}")
    return units.json()


def nomenclature_list(key):
    nomenclatures = requests.get(f"{BASE_URL}/resto/api/v2/entities/products/list?key={key}")
    return nomenclatures.json()


def employee_roles(key):
    url = f"{BASE_URL}/resto/api/employees/roles?key={key}"
    res = requests.get(url=url)
    data_xml = res.text
    data_dict = xmltodict.parse(data_xml)
    return data_dict


def employee_list(credentials, body, headers):
    url = f"{BASE_URL}/core/employee$list"
    response = requests.post(url=url, data=body, auth=HTTPBasicAuth(username=credentials['username'],
                                                                    password=credentials['password']),
                             headers=headers)
    data_json = response.json()
    return data_json


def shift_list(key, department_id):
    employee_shift = requests.get(f"{BASE_URL}/resto/api/v2/cashshifts/list?openDateFrom=2023-01-01&openDateTo=2023-12-31&departmentId={department_id}&status=ACCEPTED&key={key}")
    return employee_shift.json()


def shift_payments(key, current_date):
    url = f"{BASE_URL}/resto/api/v2/reports/olap?key={key}"
    data_json = {
        "reportType": "SALES",
        "buildSummary": "false",
        "groupByColFields": [
            "Department.Id",
            "SessionID",
            "OrderType.Id",
            "UniqOrderId.Id",
            "CardNumber",
            "OrderDiscount.GuestCard",
            "Bonus.CardNumber",
            "PayTypes.Group",
            "PayTypes.GUID",
            "PayTypes",
            "PaymentTransaction.Id",
            "Cashier.Id",
            "DishId",
            "SoldWithDish.Id",
            "SoldWithItem.Id",
            "DishMeasureUnit",
            "OrderDiscount.Type.IDs",
            "OrderIncrease.Type.IDs",
            "CloseTime",
            "Counteragent.Name",
            "OrderNum",
            "DishName",
            "DishAmountInt",
            "GuestNum"
        ],
        "aggregateFields": [
            "DishSumInt",
            "DiscountSum",
            "IncreaseSum",
            "fullSum",
            "DishDiscountSumInt"
        ],
        "filters": {
            "OpenDate.Typed": {
                "filterType": "DateRange",
                "periodType": "CUSTOM",
                "from": current_date,  # "2023-01-01"
                "to": current_date,  # "2023-01-01"
                "includeLow": True,
                "includeHigh": True
            },
            "CloseTime": {
                "filterType": "DateRange",
                "periodType": "CUSTOM",
                "from": f"{current_date}T00:00:00",
                "to": f"{current_date}T23:59:59",
                "includeLow": True,
                "includeHigh": True
            }
        }
    }
    payment_list = requests.post(url=url, json=data_json)
    return payment_list.json()


def store_incomings(key, date):
    url = f"{BASE_URL}/resto/api/v2/reports/olap?key={key}"
    data_json = {
        "reportType": "TRANSACTIONS",
        "buildSummary": "false",
        "groupByColFields": [
            "Store",
            "DateSecondary.DateTimeTyped",
            "DateTime.Typed",
            "Document",
            "Product.Id",
            "Product.MeasureUnit",
            "Counteragent.Id",
            "Account.CounteragentType"
        ],
        "aggregateFields": [
            "Amount.In",
            "Sum.Incoming"
        ],
        "filters": {
            "DateTime.DateTyped": {
                "filterType": "DateRange",
                "periodType": "CUSTOM",
                "from": f"{date}",
                "to": f"{date}",
                "includeLow": True,
                "includeHigh": True
            },
            "TransactionType": {
                "filterType": "IncludeValues",
                "values": ["INVOICE"]
            }
        }
    }
    incoming_list = requests.post(url=url, json=data_json)
    return incoming_list.json()


def department_revenue(key, department):
    url = f"{BASE_URL}/resto/api/reports/sales?key={key}&department={department}&dateFrom=01.10.2023&dateTo=15.12.2023&dishDetails=true&allRevenue=true"
    # root = ET.fromstring(department_data.content)
    # corporate_item_dtos = root.findall('dayDishValue')
    # return corporate_item_dtos
    res = requests.get(url=url)
    data_xml = res.text
    data_dict = xmltodict.parse(data_xml)
    return data_dict


def product_expenses(key, department):
    url = f"{BASE_URL}/resto/api/reports/productExpense?key={key}&department={department}&dateFrom=01.01.2023&dateTo=30.11.2023"
    # root = ET.fromstring(response.content)
    # expense_data = root.findall("dayDishValue")
    res = requests.get(url=url)
    try:
        data_xml = res.text
        data_dict = xmltodict.parse(data_xml)
    except:
        return None
    return data_dict
