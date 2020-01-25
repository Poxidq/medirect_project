# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
# from .models import CustomUser

# class CustomUserCreationForm(UserCreationForm):

#     class Meta(UserCreationForm.Meta):
#         model = CustomUser
#         fields = UserCreationForm.Meta.fields

# class CustomUserChangeForm(UserChangeForm):

#     class Meta:
#         model = CustomUser
#         fields = UserChangeForm.Meta.fields
from django import forms
from django.contrib.auth.models import User

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget=forms.PasswordInput)

class UserRegistrationForm(forms.ModelForm):
	password = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Password', widget=forms.PasswordInput)

	class Meta:
		model = User
		fields = ('username', 'first_name', 'email')

	def clean_password2(self): # проверка на идентичность двух паролей
		cd = self.cleaned_data
		if cd['password'] != cd['password2']:
			raise forms.ValidationError( _ ('Invalid value: %s ') % value)
		return cd['password2']
