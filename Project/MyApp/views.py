from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from MyApp.forms import UserCreationForm


# Create your views here.

def index(request):
    return render(request, 'index.html')

#'@login_required
#def profile(request):
#    return render(request, "user_profile.html")



def redirect_index(request):
    __doc__ = '''When this function is called, it redirects user to index page.'''
    return HttpResponseRedirect('index')


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserCreationForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserCreationForm()
    return render(request,'register.html',
                          {'user_form': user_form,
                           'registered': registered})

