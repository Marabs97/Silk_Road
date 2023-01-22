from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from MyApp.models import UserProfileModel, Results, Supervisor

# Register your models here.
admin.site.register(UserProfileModel)
admin.site.register(Results)
admin.site.register(Supervisor)

