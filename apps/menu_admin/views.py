from django.shortcuts import render
from django.http import HttpResponseRedirect

from datetime import date

from .menu_service import MenuService
from .forms import MenuInsertForm

menuService = MenuService()

def saveMenu(description, date):
    return menuService.saveMenu(
        description=description,
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
            date=request._post['date'],
        )
    dict = {
        'form': form,
        'message': response
        }
    return render(request, 'insert_menu.html', context=dict)