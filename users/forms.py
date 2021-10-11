from django import forms 
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User 
from . models import Accounts

class UserRegisterForm(UserCreationForm):
	email = forms.EmailField()
	class Meta:
		model = User 
		fields = ['first_name', 'last_name', 'username', 'email', 'password1']

class ProfileUpdateForm(forms.ModelForm):
	email = forms.EmailField()
	class Meta():
		model = User 
		fields = ['username', 'email']

class ProfilePictureUpdateForm(forms.ModelForm):
	class Meta():
		model = Accounts
		fields = ['profile_picture']
