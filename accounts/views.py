from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group
from .decorators import *
import pandas as pd
import pickle
# Create your views here.

@login_required(login_url="accounts-login-user")
def home(request):
    if request.method=="POST":
        if "staff_id" in request.POST:
            return redirect("accounts-profile-staff", pk=request.POST.get("staff_id"))
        else:
            return redirect("accounts-profile-customer", pk=request.POST.get("customer_id"))
    return render(request, "accounts/home.html", {})

@login_required(login_url="accounts-login-user")
@allowed_groups(allowed_list=['staff'])
def register_customer(request):
    form1 = UserCreationForm()
    form2 = CustomerForm()

    if request.method=="POST":
        form1 = UserCreationForm(request.POST)
        form2 = CustomerForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            group = Group.objects.get(name="customer")
            group.user_set.add(user)
            group.save()
            customer = form2.save(commit=False)
            customer.user = user
            customer.save()
            return redirect("accounts-home")

    context = {
        "form1":form1,
        "form2":form2,
    }

    return render(request, "accounts/register_customer.html", context)

@login_required(login_url="accounts-login-user")
@allowed_groups(allowed_list=['customer', 'staff', "admin"])
def profile_customer(request, pk):
    try:
        customer = Customer.objects.get(id=pk)
        applications = customer.application_set.all()
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        context = {
            "customer":customer,
            "admin_group":True if group=="admin" else False,
            "staff_group":True if group=="staff" else False,
            'applications':applications,
        }
        return render(request, "accounts/profile_customer.html", context)
    except:
        return HttpResponse("No Such Customer")

@login_required(login_url="accounts-login-user")
@allowed_groups(allowed_list=['staff'])
def update_customer(request, pk):
    try:
        customer = Customer.objects.get(id=pk)
        form1 = UpdateUserForm(instance = customer.user)
        form2 = CustomerForm(instance = customer)

        if request.method=="POST":
            form1 = UpdateUserForm(request.POST, instance = customer.user)
            form2 = CustomerForm(request.POST, request.FILES, instance = customer)

            if form1.is_valid() and form2.is_valid():
                user = form1.save()
                customer = form2.save(commit=False)
                customer.user = user
                customer.save()
                return redirect("accounts-home")

        context = {
            "form1":form1,
            "form2":form2,
        }

        return render(request, "accounts/update_customer.html", context)
    except:
        return HttpResponse("No Such Customer")

@login_required(login_url="accounts-login-user")
@allowed_groups(allowed_list=['staff'])
def delete_customer(request, pk):
    try:
        customer = Customer.objects.get(id=pk)
        user = customer.user
        user.delete()
        return redirect("accounts-home")
    except:
        return HttpResponse("No Such Customer")

@login_required(login_url="accounts-login-user")
@allowed_groups(allowed_list=['admin'])
def register_staff(request):
    form1 = UserCreationForm()
    form2 = StaffForm()

    if request.method=="POST":
        form1 = UserCreationForm(request.POST)
        form2 = StaffForm(request.POST, request.FILES)
        if form1.is_valid() and form2.is_valid():
            user = form1.save()
            group = Group.objects.get(name="staff")
            group.user_set.add(user)
            group.save()
            staff = form2.save(commit=False)
            staff.user = user
            staff.save()
            return redirect("accounts-home")

    context = {
        "form1":form1,
        "form2":form2,
    }

    return render(request, "accounts/register_staff.html", context)

@login_required(login_url="accounts-login-user")
@allowed_groups(allowed_list=['staff', "admin"])
def profile_staff(request, pk):
    try:
        staff = Staff.objects.get(id=pk)
        group = None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name

        context = {
            "staff":staff,
            "admin_group":True if group=="admin" else False,
            "staff_group":True if group=="staff" else False,
        }
        return render(request, "accounts/profile_staff.html", context)
    except:
        return HttpResponse("No Such Staff")

@login_required(login_url="accounts-login-user")
@allowed_groups(allowed_list=['admin'])
def update_staff(request, pk):
    try:
        staff = Staff.objects.get(id=pk)
        form1 = UpdateUserForm(instance = staff.user)
        form2 = StaffForm(instance = staff)

        if request.method=="POST":
            form1 = UpdateUserForm(request.POST, instance = staff.user)
            form2 = StaffForm(request.POST, request.FILES, instance = staff)

            if form1.is_valid() and form2.is_valid():
                user = form1.save()
                staff = form2.save(commit=False)
                staff.user = user
                staff.save()
                return redirect("accounts-home")

        context = {
            "form1":form1,
            "form2":form2,
        }

        return render(request, "accounts/update_staff.html", context)
    except:
        return HttpResponse("No Such Staff")

@login_required(login_url="accounts-login-user")
@allowed_groups(allowed_list=['admin'])
def delete_staff(request, pk):
    try:
        staff = Staff.objects.get(id=pk)
        user = staff.user
        user.delete()
        return redirect("accounts-home")
    except:
        return HttpResponse("No Such Staff")

def login_user(request):
    if request.method=="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("accounts-home")

    return render(request, "accounts/login_user.html", {})

@login_required(login_url="accounts-login-user")
def logout_user(request):
    logout(request)
    return redirect("accounts-home")


@login_required(login_url="accounts-login-user")
@allowed_groups(allowed_list=['staff'])
def create_application(request, pk):
    try:
        customer = Customer.objects.get(id=pk)
        form = ApplicationForm(initial={'customer':customer, 'staff':request.user.staff})
        if request.method=="POST":
            form = ApplicationForm(request.POST)
            if form.is_valid():
                form.save()
                return redirect("accounts-home")
        return render(request, "accounts/create_application.html", {"form":form})
    except:
        return HttpResponse("No Such Customer")


def predict(application):
    if application.status != "pending":
        return False

    customer = application.customer

    gender = customer.gender
    married = customer.married
    dependents = customer.dependents
    education = customer.education
    self_employed = customer.self_employed
    income = customer.income
    property_area = customer.property_area
    loan_amount = application.amount
    credit_history = 1 if customer.application_set.filter(status="appoved").count()>=1 else 0

    test_X = pd.DataFrame({"Gender":[gender, "Male", "Female", "Male"],"Married":[married, "Yes", "No", "Yes"],"Dependents":[dependents, 1, 1, 1], "Education":[education, "Graduate", "Not Graduate", "Graduate"], "Self_Employed":[self_employed, "Yes", "No", "Yes"], "ApplicantIncome":[income, 1, 1, 1], "LoanAmount":[loan_amount, 1, 1, 1], "Credit_History":[credit_history, 1, 1, 1], "Property_Area":[property_area, "Urban", "Rural", "Semiurban"]})
    test_X = pd.get_dummies(test_X)
    print(test_X.columns)
    model = pickle.load(open("static/accounts/models/loan_predictor.pickle", 'rb'))
    return model.predict(test_X)[0]

@login_required(login_url="accounts-login-user")
@allowed_groups(allowed_list=['customer', 'staff', 'admin'])
def read_application(request, pk):
    try:
        application = Application.objects.get(id=pk)
        prediction = predict(application)
        group=None
        if request.user.groups.exists():
            group = request.user.groups.all()[0].name
        context = {
            "application":application,
            "admin_group":True if group=="admin" else False,
            "staff_group":True if group=="staff" else False,
            "customer_group":True if group=="customer" else False,
            'prediction':prediction,
        }
        return render(request, "accounts/application.html", context)
    except:
        return HttpResponse("No Such Application")

@login_required(login_url="accounts-login-user")
@allowed_groups(allowed_list=['staff'])
def update_application(request, pk):
    try:
        application = Application.objects.get(id=pk)
        form = ApplicationForm(instance=application)

        if request.method=="POST":
            form = ApplicationForm(request.POST, instance=application)
            if form.is_valid():
                form.save()
                return redirect("accounts-home")
        return render(request, "accounts/update_application.html", {"form":form})
    except:
        return HttpResponse("No Such Application")

@login_required(login_url="accounts-login-user")
@allowed_groups(allowed_list=['staff'])
def delete_application(request, pk):
    try:
        application = Application.objects.get(id=pk)
        application.delete()
        return redirect("accounts-home")
    except:
        return HttpResponse("No such Application")
