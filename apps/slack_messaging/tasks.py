from __future__ import (
    absolute_import,
    unicode_literals,
)

import requests
import json
from datetime import datetime as dt

from celery import shared_task

from apps.menu_admin.menu_service import MenuService
from apps.menu_admin.company_service import CompanyService


@shared_task
def sendMenu(channel=None, menu=None):
    date = dt.today().strftime('%Y-%m-%d')
    menus = MenuService.getMenuByDate(date=date)
    companies = CompanyService.getCompanies()
    headers = {'Content-type': 'application/json'}
    menu_descriptions = []
    for menu in menus.values():
        menu_descriptions.append(menu['description'])
    plates = '\n - '.join(menu_descriptions)

    message = f'''
    Hola!\n
    Dejo el menú de hoy {date} :)
    '''

    data = {
        'attachments': [
            {
                'text': f'- {plates}',
                'pretext': message,
                'footer': 'Que tengan un lindo día!'
            }
        ]
    }
        
    for company in companies:
        url = company.slack_webhook
        res = requests.post(
            url,
            headers=headers,
            data=json.dumps(data),
            )

    return res.text