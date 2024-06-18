from django.urls import path
from . import views
app_name = "projects"

urlpatterns = [
    path('home/', views.home, name="home"),
    path('convsec/', views.convsec, name="convsec"),
    path('beecell/', views.beecell, name="beecell")
]