from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, unique=True)
    ID = models.AutoField()

    class Memberships(models.TextChoices):
        PATIENT = 'L1', _('Patient')
        DOCTOR = 'L2', _('Doctor')
        COMPANY = 'L3', _('Company')

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    # portfolio_site = models.URLField(blank=True)
    phone_number = models.CharField(max_length=14, unique=True)
    email = models.EmailField(blank=False, unique=True)
    __password__ = models.CharField(max_length=16)

    __access_level__ = models.CharField(choices=Memberships.choices, default=Memberships.PATIENT)
    #record_history = models.ForeignKey('Results', on_delete=models.CASCADE)

    # hidden, number of times that a user can use the website
    tokens = models.PositiveSmallIntegerField(default=2)

    # Unique Identifier to be used for One-Step Login
    USERNAME_FIELD = ID
    EMAIL_FIELD = email
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    def __str__(self):
        return self.user.username


class Results(models.Model):
    result = models.TextField()
