""""
Forms.py
"""
from django import forms



class NameForm(forms.Form):
    numDays = forms.CharField(label="Projected Values After This Many Days:", max_length=3)

class addForm(forms.Form):
    name = forms.CharField(max_length=100)
    expiration = forms.CharField(max_length=3)
    quality = forms.CharField(max_length=3)

class updateForm(forms.Form):
    name = forms.CharField(max_length=100)
    expiration = forms.CharField(max_length=3)
    quality = forms.CharField(max_length=3)
