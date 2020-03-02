from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms



class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=50,required=True,widget=forms.EmailInput())

    class Meta:
        model = User
        fields = ['email','username','password1','password2']