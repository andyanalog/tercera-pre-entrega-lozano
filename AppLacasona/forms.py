from django import forms

class ProfesorFormulario(forms.Form):
    email = forms.EmailField()