from django import forms

from main.models import Class


class ClassForm(forms.Form):
    forms.ChoiceField(required=True)

    class Meta:
        fields = ['students']

