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
    menu = MenuService.getMenuByDate(date=date)
    companies = CompanyService.getCompanies()
    headers = {'Content-type': 'application/json'}
    meal_descriptions = []
    for meal in menu.meal_set.all().values():
        meal_descriptions.append(meal['description'])
    meal = '\n - '.join(meal_descriptions)

    message = f'''
    Hola!\n
    Dejo el menú de hoy {date} :)
    '''
    uuid = str(menu.uuid)
    link = f'http://localhost:8000/menu/{uuid}'
    data = {
        'attachments': [
            {
                'title': 'Ingresa aquí para pedir tu menu.',
                'title_link': link,
                'text': f'- {meal}',
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