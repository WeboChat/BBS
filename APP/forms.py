from django import forms

from models import UserModel

class RegisterFrom(forms.ModelForm):
    class Meta():
        model = UserModel
        fields = ['name', 'sex', 'password', 'icon']

    password = forms.CharField(max_length=128)
