from django import forms

from .menu_service import MenuService


class MenuInsertForm(forms.Form):
    options = list(MenuService.getAllmeals().values_list())
    meals = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=options,
    )
    date = forms.DateField()


class CompanyInsertForm(forms.Form):
    name = forms.CharField()
    slack_webhook = forms.CharField()


class OrderInsertForm(forms.Form):

    def getForm(uuid=None):
        if uuid:
            todays_menu = MenuService.getMenuByUuid(uuid)
            options = list(todays_menu.meal_set.all())
            customer_name = forms.CharField()
            custom_spec = forms.CharField()
            meal = forms.ChoiceField(choices=options)