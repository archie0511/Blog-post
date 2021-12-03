#froms .py becoz we want to add more fiels to the form which django has

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm(UserCreationForm):
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email','password1','password2']
    
# to make updates in user and profile on profile page
class UserUpdateForm(forms.ModelForm):   
    email=forms.EmailField()

    class Meta:
        model = User
        fields = ['username','email']

class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['image']       
    
