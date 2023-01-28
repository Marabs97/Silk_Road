from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import UserProfileModel, Results
from .forms import NewUserForm
from django.contrib import messages

from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.list import ListView, MultipleObjectMixin

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# from getSymptoms import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView

# Create your views here.


def index(request):
    return render(request, 'home.html')


# '@login_required
# def profile(request):
#    return render(request, "user_profile.html")


def redirect_index(request):
    __doc__ = '''When this function is called, it redirects user to index page.'''
    return HttpResponseRedirect('home')


class SignUpView(CreateView):
    form_class = NewUserForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"


@login_required
def profile_view(request):
    user = get_object_or_404(UserProfileModel, username=request.user.username)
    #full_name = user.full_name
    #tokens = user.tokens
    return render(request, template_name='profile.html',
                  context={'user': user})


@login_required
def reports_view(request):
    user = get_object_or_404(UserProfileModel, username=request.user.username)
    reports_list = Results.objects.filter(created_by=user)
    return render(request, template_name="reports.html",
                  context={"reports_list": reports_list})

@login_required
class AccountInformationView(UserPassesTestMixin, DetailView):
    model = UserProfileModel
    template_name = 'profile.html'

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfileModel, username=self.kwargs.get('user'), pk=self.request.user.pk)


'''
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
'''
