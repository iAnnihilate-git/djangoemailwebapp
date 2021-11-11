from django import forms

class EmailForm(forms.Form):
    to = forms.CharField()
    msg = forms.CharField()
    subject = forms.CharField()
