from django import forms

from .models import Meal

class MenuInsertForm(forms.Form):
    options = list(Meal.objects.all().values_list())
    meals = forms.MultipleChoiceField(
        widget=forms.CheckboxSelectMultiple,
        choices=options,
    )
    date = forms.DateField()

class CompanyInsertForm(forms.Form):
    name = forms.CharField()
    slack_webhook = forms.CharField()

class OrderInsertForm(forms.Form):
    customer_name = forms.CharField()
    custom_spec = forms.CharField()
    menu_id = forms.IntegerField()