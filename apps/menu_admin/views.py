from django.shortcuts import render
from django.http import HttpResponseRedirect

from datetime import date

from .menu_service import MenuService
from .forms import MenuInsertForm

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