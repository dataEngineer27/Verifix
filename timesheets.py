from helpers.database import SessionLocal
from helpers import crud, micro, config


def time_sheets():
    session = SessionLocal()
    credentials = {
        "username": config.USERNAME,
        "password": config.PASSWORD
    }
    body = {
        "period_begin_date": "29.12.2023",
        "period_end_date": "29.12.2023",
        "division_ids": [],
        "employee_ids": []
    }
    response = micro.timesheet_list(credentials=credentials, body=body, headers={})
    timesheet_list = response["data"]
    for employee in timesheet_list:
        crud.add_employee_timesheets(db=session, employee_timesheets=employee)
    next_page = response["meta"]["next_cursor"]
    while next_page != "-1":
        print("next_cursor:", next_page)
        headers = {"Content-Type": "application/json", "cursor": str(next_page)}
        response = micro.timesheet_list(credentials=credentials, body=body, headers=headers)
        timesheet_list = response["data"]
        for employee in timesheet_list:
            crud.add_employee_timesheets(db=session, employee_timesheets=employee)
        next_page = response["meta"]["next_cursor"]


if __name__ == '__main__':
    time_sheets()
