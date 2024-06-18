from django.urls import include, re_path
from django.contrib import admin

urlpatterns = [
    re_path(r'admin/', admin.site.urls),
    re_path("", include("apps.public.urls")),
    re_path(r'dashboards/', include('apps.dashboards.urls')),
    re_path(r'projects/', include('apps.projects.urls')),
    re_path(r'accounts/', include('apps.accounts.urls'))
]