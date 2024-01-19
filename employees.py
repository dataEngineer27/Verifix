from helpers.database import SessionLocal
from helpers import crud, micro
from helpers.config import USERNAME, PASSWORD

credentials = {
    "username": USERNAME,
    "password": PASSWORD
}


def employees():
    session = SessionLocal()
    body = {
        "employee_ids": []
    }
    response = micro.employee_list(credentials=credentials, body=body, headers=None)
    employee_list = response["data"]
    crud.add_employees(db=session, employee_list=employee_list)
    next_page = response["meta"]["next_cursor"]
    while next_page != "-1":
        headers = {'Content-Type': 'application/json', 'cursor': next_page}
        response = micro.employee_list(credentials=credentials, body=body, headers=headers)
        employee_list = response["data"]
        crud.add_employees(db=session, employee_list=employee_list)
        next_page = response["meta"]["next_cursor"]


if __name__ == '__main__':
    employees()
