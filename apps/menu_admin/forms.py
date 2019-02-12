from django import forms

class MenuInsertForm(forms.Form):
    menu = forms.CharField()
    date = forms.DateField()