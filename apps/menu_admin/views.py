from django.shortcuts import render
from django.http import HttpResponseRedirect

from datetime import (
    date,
    datetime as dt,
)

from .menu_service import MenuService
from .forms import (
    MenuInsertForm,
    OrderInsertForm,
)

menuService = MenuService()

def saveMenu(description, meals, date):
    return menuService.saveMenu(
        description=description,
        meals=meals,
        date=date,
    )

def getMenuByDate():
    menuService.getMenuByDate(date.today())

def insertMenuForm(request):
    form = MenuInsertForm()
    response = None
    if request.method == 'POST':
        response = saveMenu(
            description=request._post['menu'],
            meals=request._post.getlist('meals'),
            date=request._post['date'],
        )
    dict = {
        'form': form,
        'message': response
        }
    return render(request, 'insert_menu.html', context=dict)

def saveMeal(description):
    return menuService.saveMeal(description=description)

def insertOrderForm(request, uuid):
    insertForm = OrderInsertForm()
    form = insertForm.getForm(uuid=uuid)
    dict = {
        'form': form,
        'date': dt.today().strftime('%Y-%m-%d'),
    }
    return render(request, 'insert_order.html', context=dict)
