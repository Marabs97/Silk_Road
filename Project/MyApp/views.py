from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .forms import NewUserForm
from django.contrib import messages


# Create your views here.

def index(request):
    return render(request, 'home.html')


# '@login_required
# def profile(request):
#    return render(request, "user_profile.html")


def redirect_index(request):
    __doc__ = '''When this function is called, it redirects user to index page.'''
    return HttpResponseRedirect('index')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = NewUserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            messages.error(request, "Unsuccessful registration. Invalid information.")
            print(user_form.errors)
    else:
        user_form = NewUserForm()

    return render(request, template_name='register.html',
                  context={'user_form': user_form, 'registered': registered})
