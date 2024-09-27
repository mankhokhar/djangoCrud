from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect, HttpResponse

from django.template.loaders.app_directories import get_app_template_dirs

# Create your views here.


def signup_view(request):
    signup_form = UserCreationForm()
    print(get_app_template_dirs('templates'))

    return HttpResponse('Hello World')
    # return render(request, 'users/userSignup.html', {'signup_form': signup_form})
