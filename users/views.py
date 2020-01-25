from django.shortcuts import render

from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required
from .forms import UserRegistrationForm, LoginForm

class HomePageView(TemplateView):
    template_name = 'forgot_password.html'

def register(request):
	if request.method == 'POST'
		user_form = UserRegistrationForm(request.POST)
		if user_form.is_valid():
			new_user = user_form.save(commit = False)
			new_user.set_password(user_form.cleaned_data['password'])
			new_user.save()
			return render(request, 'users/register_done.html', {'user_form': user_form})
	else:
		user_form = UserRegistrationForm()
	return render(request, 'users/register.html', {'user_form': user_form})
	
# Create your views here.
