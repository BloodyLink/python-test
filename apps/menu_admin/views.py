from django.shortcuts import render

from datetime import date

from .menu_service import MenuService


class MenuManager():
    
    def __init__(self):
        self.menuService = MenuService()

    def saveMenu(self, description, date):
        return self.menuService.saveMenu(
            description=description,
            date=date,
        )

    def getMenuByDate():
        self.menuService.getMenuByDate(date.today())