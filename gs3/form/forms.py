from pyexpat import model
from django import forms
class StudentRegistrartion(forms.Form):
    user_name = forms.CharField()
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput)