from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView
from app.models import *
class home(TemplateView):
    template_name = "app/home.html"


class School_list(ListView):
    template_name='app/School_list.html'
    model=School
    context_object_name='schools'
