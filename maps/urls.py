from django.urls import path
from . import views
app_name = 'maps'

urlpatterns = [
    path('top/', views.top, name='top'),
]