from django.db import models

# Create your models here.
from django.http import HttpResponse


def about_me(request):
    return HttpResponse("This would be the about page")
