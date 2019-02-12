from django import forms

class MenuInsertForm(forms.Form):
    menu = forms.CharField()
    date = forms.DateField()

class CompanyInsertForm(forms.Form):
    name = forms.CharField()
    slack_webhook = forms.CharField()

class OrderInsertForm(forms.Form):
    customer_name = forms.CharField()
    custom_spec = forms.CharField()
    menu_id = forms.IntegerField()