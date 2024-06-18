from django.urls import path
from django.contrib.auth import views as auth_views
app_name = "accounts"

urlpatterns = [

    # Django Auth Stuff
    path('login', auth_views.LoginView.as_view(
        template_name='accounts/login.html'),
        name='login')

]
