""""
Forms.py
"""
from django import forms



class NameForm(forms.Form):
    """NameForm"""
    numDays = forms.CharField(label="Projected Values After This Many Days:", max_length=3)

class addForm(forms.Form):
    """Addform"""
    name = forms.CharField(max_length=100)
    expiration = forms.CharField(max_length=3)
    quality = forms.CharField(max_length=3)

class updateForm(forms.Form):
    """updateForm"""
    name = forms.CharField(max_length=100)
    expiration = forms.CharField(max_length=3)
    quality = forms.CharField(max_length=3)
