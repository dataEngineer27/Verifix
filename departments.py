# from helpers.database import SessionLocal
from helpers import crud, micro, database


def departments():
    session = database.SessionLocal()
    key = micro.login()
    try:
        department_list = micro.department_list(key=key)
    except:
        key = micro.login()
        department_list = micro.department_list(key=key)
    crud.add_departments(db=session, department_list=department_list)
    micro.logout(key=key)


if __name__ == '__main__':
    departments()
