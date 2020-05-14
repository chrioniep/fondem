from django.urls import path
from .views import DashViewHome, DashViewUpdate, DashViewCreate, delete_event

app_name = 'dash'

urlpatterns = [
    path('', DashViewHome.as_view(), name='home'),
    path('create/', DashViewCreate.as_view(), name='create'),
    path('update/<slug>', DashViewUpdate.as_view(), name="update"),
    path('delete-event/<slug>', delete_event, name="delete")


]