from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from MyApp.models import UserProfileModel, Results

# Register your models here.
admin.site.register(UserProfileModel, UserAdmin)
admin.site.register(Results)
