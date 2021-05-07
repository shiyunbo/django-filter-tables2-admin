#-*- coding:utf-8 -*-
from django import forms
from .models import User


class UserForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name')

        widgets = {
            'password':forms.PasswordInput(),
        }