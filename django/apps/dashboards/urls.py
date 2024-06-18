from django.urls import path
from . import views
app_name = "dashboards"

urlpatterns = [
    path('home/', views.home, name="home"),
    path('fg/', views.fg, name="fg"),
]