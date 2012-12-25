from django import forms

class MemeForm(forms.Form):
    picture = forms.ImageField(required=False)