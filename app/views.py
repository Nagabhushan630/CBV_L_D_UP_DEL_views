from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from app.models import *
class home(TemplateView):
    template_name = "app/home.html"


class School_list(ListView):
    template_name='app/School_list.html'
    model=School
    context_object_name='schools'


class SchoolDetail(DetailView):
    model=School 
    context_object_name='sclobject'


class SchoolCreate(CreateView):
    model=School
    fields='__all__' 

class SchoolUpdate(UpdateView):
    model=School
    fields='__all__'

class SchoolDelete(DeleteView):
    model=School
    context_object_name=name='schoolobject'
    success_url=reverse_lazy('School_list')