from django.shortcuts import render, redirect
from django.views.generic import View, ListView, DetailView
from .models import Event
from .forms import DashboardForm
# Create your views here.


    

class EventList(ListView):
    model = Event
    template_name = "news.html"
    context_object_name = "events"
    paginate_by = 3


class EventDetail(DetailView):

    model = Event
    template_name = "single_news.html"
    context_object_name = 'event_detail'
