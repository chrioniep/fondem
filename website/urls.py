from django.urls import path
from django.views.generic import TemplateView
from .views import EventList, EventDetail


app_name='website'

urlpatterns = [
    path('', TemplateView.as_view(template_name='index.html'), name='home'),
    path('about/', TemplateView.as_view(template_name='about.html'), name='about'),
    path('contact/', TemplateView.as_view(template_name="contact.html"), name='contact'),
    path('news/', EventList.as_view(), name='news'),
    path('single-news/<slug>', EventDetail.as_view(), name='single-news'),
    path('gallery/', TemplateView.as_view(template_name='gallery.html'), name='gallery'),
    path('causes/', TemplateView.as_view(template_name='causes.html'), name='causes'),
]
