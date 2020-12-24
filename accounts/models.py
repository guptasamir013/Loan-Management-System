from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Customer(models.Model):
    EDUCATION= [
        ('Graduate', 'Graduate'),
        ('Not Graduate', 'Not Graduate'),
    ]
    GENDER = [
        ('Male', 'Male'),
        ('Female', 'Female'),
    ]
    MARRIED = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    SELF_EMPLOYED = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    PROPERTY_AREA = [
        ('Rural', 'Rural'),
        ('Urban', 'Urban'),
        ('Semiurban', 'Semiurban'),
    ]
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    pic = models.ImageField(null=True, blank=True, upload_to="accounts/customers/")
    gender = models.CharField(max_length=100, blank=True, null=True, choices=GENDER)
    married = models.CharField(max_length=100, blank=True, null=True, choices=MARRIED)
    dependents = models.IntegerField(blank=True, null=True)
    education = models.CharField(max_length=100, blank=True, null=True, choices=EDUCATION)
    self_employed = models.CharField(max_length=100, blank=True, null=True, choices=SELF_EMPLOYED)
    income = models.IntegerField(blank=True, null=True)
    property_area = models.CharField(max_length=100, blank=True, null=True, choices=PROPERTY_AREA)

    def __str__(self):
        if self.user.username:
            return self.user.username
        else:
            return self.id

class Staff(models.Model):
    EDUCATION_LEVELS = [
        ('primary', 'primary'),
        ('secondary', 'secondary'),
        ('high', 'high'),
    ]
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    pic = models.ImageField(null=True, blank=True, upload_to="accounts/staff/")
    education = models.CharField(max_length=100, null=True, blank=True, choices=EDUCATION_LEVELS)
    phone = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        if self.user.username:
            return self.user.username
        else:
            return self.id

class Application(models.Model):
    LOAN_TYPES = [
        ('car', 'car'),
        ('education', 'education'),
        ('home', 'home'),
    ]
    APPLICATION_STATUS = [
        ('pending', 'pending'),
        ('approved', 'approved'),
        ('rejected', 'rejected'),
        ('completed', 'completed'),
    ]
    customer = models.ForeignKey(Customer, blank=True, null=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Staff, blank=True, null=True, on_delete=models.SET_NULL)
    type = models.CharField(max_length=100, blank=True, null=True, choices=LOAN_TYPES)
    amount = models.IntegerField(blank=True, null=True)
    status = models.CharField(max_length=100, blank=True, null=True, default="pending", choices=APPLICATION_STATUS)
