from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

User_Model = get_user_model()


class RegistrationForm(UserCreationForm):
    class Meta:
        model = User_Model
        fields = [
            "username",
            "email",
            "first_name",
            "last_name",
            "password1",
            "password2",
        ]

class LoginForm(AuthenticationForm):
    class Meta:
        model = User_Model
        fields = [
            "username","password1"
        ]