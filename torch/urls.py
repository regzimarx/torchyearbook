from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'', include('users.urls', namespace='account')),
    url(r'', include('management.urls', namespace='management')),
    url(r'^admin/', admin.site.urls),
]
