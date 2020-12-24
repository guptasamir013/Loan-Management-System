from .models import *
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomerForm(ModelForm):
    class Meta:
        model = Customer
        exclude = ('user',)

class UpdateUserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username"]


class StaffForm(ModelForm):
    class Meta:
        model = Staff
        fields = ['pic', 'education', 'phone']

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = "__all__"
