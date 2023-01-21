from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db.models.signals import post_save

# Create your models here.


class UserProfileModel(AbstractUser):
    #user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE, unique=True)
    #ID = models.AutoField()

    class Memberships(models.TextChoices):
        PATIENT = 'L1', 'Patient'
        DOCTOR = 'L2', 'Doctor'
        COMPANY = 'L3', 'Company'

    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15)

    # portfolio_site = models.URLField(blank=True)
    phone_number = models.CharField(max_length=14, unique=True)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=16)

    access_level = models.CharField(max_length=3, choices=Memberships.choices, default=Memberships.PATIENT)
    #record_history = models.ForeignKey('Results', on_delete=models.CASCADE)

    # hidden, number of times that a user can use the website
    tokens = models.PositiveSmallIntegerField(default=2)

    # Unique Identifier to be used for One-Step Login
    #USERNAME_FIELD = phone_number
    #EMAIL_FIELD = email
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'email', 'password']


class Results(models.Model):
    '''
    patient = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    '''

    result = models.TextField()
    
    created_by = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.created_by


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