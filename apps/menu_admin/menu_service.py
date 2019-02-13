from datetime import date

from .models import (
    Menu,
    Meal,
)


class MenuService():

    @staticmethod
    def saveMenu(description, meals, date):
        response = None
        try:
            menu = Menu(
                description = description,
                date = date,
            )
            menu.save()
            print('*********************')
            print(meals)
            for meal_id in meals:
                meal = Meal.objects.get(pk=meal_id)
                meal.menu.add(menu)
            response = 'Menu saved!'
        except Exception as e:
            response = 'There was a problem saving the menu: {error}'.format(error=e)
        return response

    @staticmethod
    def getMenuByDate(date):
        return Menu.objects.filter(date=date)

    @staticmethod
    def saveMeal(description):
        response = None
        try:
            meal = Meal(description = description)
            meal.save()
            response = 'Meal saved!'
        except Exception as e:
            response = 'There was a problem saving the meal: {error}'.format(error=e)
        return response