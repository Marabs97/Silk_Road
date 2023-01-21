from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from MyApp.models import UserProfileModel

# Register your models here.
admin.site.register(UserProfileModel, UserAdmin)
