from django import forms
from django.contrib.auth.forms import UserCreationForm
from MyApp.models import UserProfileModel


# Create your forms here.

class NewUserForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = UserProfileModel
        fields = ("first_name", "last_name", "email", "phone_number")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
