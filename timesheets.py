from helpers.database import SessionLocal
from helpers import crud, micro, config


def time_sheets():
    session = SessionLocal()
    credentials = {
        "username": config.USERNAME,
        "password": config.PASSWORD
    }
    body = {
        "division_ids": []
    }
    response = micro.timesheet_list(credentials=credentials, body=body, headers={})
    timesheet_list = response["data"]
    crud.add_divisions(db=session, division_list=timesheet_list)
    next_page = response["meta"]["next_cursor"]
    while next_page != "-1":
        print("next_cursor:", next_page)
        headers = {"Content-Type": "application/json", "cursor": str(next_page)}
        response = micro.division_list(credentials=credentials, body=body, headers=headers)
        timesheet_list = response["data"]
        crud.add_divisions(db=session, division_list=timesheet_list)
        next_page = response["meta"]["next_cursor"]


if __name__ == '__main__':
    time_sheets()
