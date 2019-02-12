from datetime import date

from .models import Menu


class MenuService():

    @staticmethod
    def saveMenu(description, date):
        response = None
        try:
            menu = Menu(
                description = description,
                date = date,
            )
            menu.save()
            response = 'Menu saved!'
        except Exception as e:
            response = 'There was a problem saving the menu: {error}'.format(error=e)
        return response

    @staticmethod
    def getMenuByDate(date):
        return Menu.object.get(date=date)