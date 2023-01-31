from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from .models import UserProfileModel, Results, TempInputModel
from .forms import NewUserForm, TempInputForm, InputForm
from django.contrib import messages

from django.views.generic.detail import DetailView
from django.contrib.auth.mixins import UserPassesTestMixin
from django.views.generic.list import ListView, MultipleObjectMixin

from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required
# from getSymptoms import *
from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
import pandas as pd
import operator as op

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
    # full_name = user.full_name
    # tokens = user.tokens
    return render(request, template_name='profile.html',
                  context={'user': user})


@login_required
def reports_view(request):
    user = get_object_or_404(UserProfileModel, username=request.user.username)
    reports_list = Results.objects.filter(created_by=user)
    return render(request, template_name="reports.html",
                  context={"reports_list": reports_list})


'''
@login_required
class AccountInformationView(UserPassesTestMixin, DetailView):
    model = UserProfileModel
    template_name = 'profile.html'

    def get_object(self, queryset=None):
        return get_object_or_404(UserProfileModel, username=self.kwargs.get('user'), pk=self.request.user.pk)
'''


### Dynamic search is bidirectional
# TODO Modify this function for searching
@login_required
def input_symptoms_view(request):
    user1 = get_object_or_404(UserProfileModel, username=request.user.username)

    tk = user1.tokens

    # create a form instance and populate it with data from the request:
    form = InputForm(request.POST, initial={'user': request.user.id})
    # create the django object in memory, but don't save to the database

    if tk >= 1:
        # temporary saves dirty input
        if request.method == 'POST':

            # check whether it's valid:
            if form.is_valid():
                obj = form.save(commit=False)
                obj.user = request.user
                obj.save()

                # process the data in form.cleaned_data as required
                # ...

                UserProfileModel.objects.filter(username=request.user.username).update(tokens=(tk - 1))
                # redirect to a new URL:
                return HttpResponseRedirect('/reports')


        # if a GET (or any other method) we'll create a blank form
        else:
            form = InputForm()
    else:
        # Better be a error page
        print("user has no tokens")
        return HttpResponseRedirect('/profile')

    template_name = 'input_symptoms.html'
    context = {'form': form, 'user1': user1}
    return render(request, template_name, context)





@login_required
def PassCleanData_view(request):

    input_info_from_user = get_object_or_404(TempInputModel, user=request.user.id)

    def is_in(full_str, sub_str):
        if op.contains(full_str, sub_str):
            return 0
        else:
            return -1

    def feed_back_choice(input_info_from_user):  # input: skin, pain

        """
        get the input from users and give them possible choices to choose of symptoms.
        :param input_info_from_user: user type the keywords of symptoms in the blank (type: list,separate with comma)
        :return: possible/suggested choices of symptoms from the database.
        """
        testing_file = pd.read_csv("Testing.csv")
        testing_file = testing_file.drop(['prognosis'], axis=1)
        symptoms = list(testing_file.columns)

        symptom_list = []
        for name in symptoms:
            symptom_list.append(name.replace('_', ' '))

        input_list = input_info_from_user.split(',')

        # provide possible choices of symptoms to the users to choose.
        feedback_choice = []
        for input_sym in input_list:
            for symptom in symptom_list:
                if is_in(symptom, input_sym) == 0:
                    feedback_choice.append(symptom)
        return feedback_choice


    # if this is a POST request we need to process the form data


    # if a GET (or any other method) we'll create a blank form

    template_name = 'choice_for_users.html'
    context = {'feed_back_choice': feed_back_choice}
    return render(request, template_name, context)


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
