import requests
import os
import xmltodict
from dotenv import load_dotenv
from requests.auth import HTTPBasicAuth
from helpers.config import BASE_URL


def employee_list(credentials, body, headers):
    url = f"{BASE_URL}/core/employee$list"
    response = requests.post(url=url, data=body, auth=HTTPBasicAuth(username=credentials['username'],
                                                                    password=credentials['password']),
                             headers=headers)
    data_json = response.json()
    return data_json


def division_list(credentials, body, headers):
    url = f"{BASE_URL}/core/division$list"
    response = requests.post(url=url, data=body, auth=HTTPBasicAuth(username=credentials['username'],
                                                                    password=credentials['password']),
                             headers=headers)
    data_json = response.json()
    return data_json


def timesheet_list(credentials, body, headers):
    url = f"{BASE_URL}/core/timesheet$export"
    response = requests.post(url=url, data=body, auth=HTTPBasicAuth(username=credentials['username'],
                                                                    password=credentials['password']),
                             headers=headers)
    data_json = response.json()
    return data_json

