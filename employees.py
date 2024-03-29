from helpers.database import SessionLocal
from helpers import crud, micro, config


def employees():
    session = SessionLocal()
    credentials = {
        "username": config.USERNAME,
        "password": config.PASSWORD
    }
    body = {
        "employee_ids": []
    }
    response = micro.employee_list(credentials=credentials, body=body, headers={})
    employee_list = response["data"]
    crud.add_employees(db=session, employee_list=employee_list)
    next_page = response["meta"]["next_cursor"]
    while next_page != "-1":
        print("next_cursor:", next_page)
        headers = {"Content-Type": "application/json", "cursor": str(next_page)}
        response = micro.employee_list(credentials=credentials, body=body, headers=headers)
        employee_list = response["data"]
        crud.add_employees(db=session, employee_list=employee_list)
        next_page = response["meta"]["next_cursor"]


if __name__ == '__main__':
    employees()
