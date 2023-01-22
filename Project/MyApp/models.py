from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.conf import settings
from django.db.models.signals import post_save


# Create your models here.


class UserProfileModel(models.Model):
    # user = models.OneToOneField(AbstractUser, on_delete=models.CASCADE, unique=True)
    ID = models.AutoField(primary_key=True)

    class Memberships(models.TextChoices):
        PATIENT = 'L1', 'Patient'
        DOCTOR = 'L2', 'Doctor'
        COMPANY = 'L3', 'Company'

    first_name = models.CharField(max_length=30)
    middle_name = models.CharField(max_length=30, blank=True, null=True)
    last_name = models.CharField(max_length=30)
    gender = models.CharField(max_length=20, choices=(('Male', 'Male'), ('Female', 'Female')), default="Male")

    # portfolio_site = models.URLField(blank=True)
    phone_number = models.CharField(max_length=14, unique=True)
    email = models.EmailField(blank=False, unique=True)
    password = models.CharField(max_length=16)

    access_level = models.CharField(max_length=3, choices=Memberships.choices, default=Memberships.PATIENT)
    # record_history = models.ForeignKey('Results', on_delete=models.CASCADE)

    # hidden, number of times that a user can use the website
    tokens = models.PositiveSmallIntegerField(default=2)

    # Unique Identifier to be used for One-Step Login

    # EMAIL_FIELD = email
    REQUIRED_FIELDS = ['first_name', 'last_name', 'phone_number', 'email', 'password']

    class Meta:
        verbose_name_plural = "List of Members"
        ordering = ['last_name']

    def full_name(self):
        return str(
            f"{self.first_name}{' ' + self.middle_name if not self.middle_name is None else ''} {self.last_name}")

    def __str__(self):
        return str(f"{self.ID}.{self.first_name}  {self.last_name}")


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

    result = models.TextField()

    created_by = models.ForeignKey(UserProfileModel, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    # Requires a ForeignKey to entered symptoms

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
