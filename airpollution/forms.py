from allauth.account.forms import LoginForm, PasswordField
from django.contrib.auth import get_user_model

from django import forms
from django.contrib.auth.models import User

from django import forms
from django.conf import settings
from django.contrib.auth import get_user_model
from allauth.account.forms import SetPasswordField, PasswordField
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from . import models


class SignupForm(forms.Form):
    city = forms.CharField(max_length=20, label='city')

    class Meta:
            model = models.Profile # use this function for swapping user model
            # model = get_user_model()
            fields = ('city')

    def signup(self, request, user):
        up = user.profile
        up.city = self.cleaned_data['city']
        user.save()
        up.save()


class AirLoginForm(LoginForm):
    remember = forms.BooleanField(label=("Remember Me"),
                              required=False, initial=True)

    def __init__(self, *args, **kwargs):

        super(AirLoginForm, self).__init__(*args, **kwargs)
        self.fields['password'].login_widget = forms.PasswordInput(attrs={'placeholder': 'Password'})
        self.fields['password'].label = ""
        self.fields['login'].widget = forms.TextInput(attrs={'placeholder': 'e-mail or Login'})
        self.fields['login'].label = ""
        self.fields['remember'].widget =  forms.HiddenInput()
