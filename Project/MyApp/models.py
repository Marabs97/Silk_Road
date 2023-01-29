from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.conf import settings
from django.db.models.signals import post_save
from django.utils.translation import gettext_lazy as _
from .managers import CustomUserManager
from django.utils import timezone

# Create your models here.


class UserProfileModel(AbstractBaseUser, PermissionsMixin):
    #user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    username = models.CharField(_("username"), max_length=50, unique=True, blank=False, null=False)

    #ID1 = models.PositiveSmallIntegerField(auto_created=True, unique=True)

    class Memberships(models.TextChoices):
        PATIENT = 'L1', _('Patient')
        DOCTOR = 'L2', _('Doctor')
        COMPANY = 'L3', _('Company')

    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=20, choices=(('Male', 'Male'), ('Female', 'Female')), default="Male")

    # portfolio_site = models.URLField(blank=True)
    phone_number = models.CharField(max_length=14, unique=True)
    email = models.EmailField(blank=False, unique=True)
    #password = models.CharField(max_length=16)

    access_level = models.CharField(max_length=3, choices=Memberships.choices, default=Memberships.PATIENT)
    # record_history = models.ForeignKey('Results', on_delete=models.CASCADE)

    # hidden, number of times that a user can use the website
    tokens = models.PositiveSmallIntegerField(default=2)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)

    # Unique Identifier to be used for One-Step Login

    uid = models.UUIDField(
        default=None,
        blank=True,
        null=True,
        unique=True,
    )

    USERNAME_FIELD = 'username'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['email', 'phone_number']

    objects = CustomUserManager()

    class Meta:
        verbose_name_plural = "User Profiles"
        ordering = ['access_level', 'last_name']

    def full_name(self):
        return str(
            f"{self.first_name}{' ' + self.middle_name if self.middle_name is None else ''} {self.last_name}")

    def __str__(self):
        return str(f"{self.username}.{self.first_name}  {self.last_name} access level: {self.access_level}")


class Results(models.Model):
    '''
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )


    def number():
        count = Results.objects.count()
        if count is None:
            return 1
        else:
            return count + 1
    '''

    report_ID = models.AutoField(primary_key=True)
    input = models.TextField(default="Default")
    result = models.TextField()

    created_by = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # Requires a ForeignKey to entered symptoms

    class Meta:
        verbose_name_plural = "reports"
        ordering = ['report_ID']

    def __str__(self):
        return str(f"report {self.report_ID}")


'''
#access_level = models.IntegerField(choices=ACCESS_LEVEL_CHOICES, default=ACCESS_PATIENT)
ACCESS_PATIENT = 11
ACCESS_DOCTOR = 22
ACCESS_COMPANY = 33
ACCESS_LEVEL_CHOICES = [
    (ACCESS_PATIENT, "Patient"),
    (ACCESS_DOCTOR, "Doctor"),
    (ACCESS_COMPANY, "Company"),
]
'''


class Supervisor(models.Model):
    name = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE, related_name="+")
    #name = UserProfileModel.full_name
    list_patients = models.ManyToManyField(UserProfileModel)
    #access_level = models.CharField(UserProfileModel.access_level)

    def __str__(self):
        return str(f"{self.name} supervising profile")


### This is CORRECTED input from user, done by dynamic search in views
### Replace This with your Model(s)
#TODO Replace this Model with ML models to do the calculations and saves the results in ReportsModel
class InputModel(models.Model):
    user = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)

    # your input should be saved for data analysis processes and later on qualifications
    symptoms_list = models.TextField(max_length=500)
    date = models.DateTimeField(default=timezone.now)

    # your ML model goes here
    sample_output = 'symptoms_list'


    # this function saves the output in Reports Model
    def save(self, *args, **kwargs):
        output = str((self.sample_output, self.symptoms_list, "This is a text"))
        return Results.objects.create(input=output, created_by=self.user)


    def __str__(self):
        return str(self.date)

###