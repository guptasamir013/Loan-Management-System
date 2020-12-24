from django.shortcuts import redirect
from django.http import HttpResponse

def allowed_groups(allowed_list = []):
    def decorator(func):
        def wrapper(request, *args, **kwargs):
            group = None
            if request.user.groups.exists():
                group = request.user.groups.all()[0].name
            if group in allowed_list:
                return func(request, *args, **kwargs)

            return HttpResponse("Not Authorized")
        return wrapper
    return decorator
