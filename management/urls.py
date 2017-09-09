from django.conf.urls import url

from .views import ProfilesListView

urlpatterns = [
    url(r'^list/', ProfilesListView.as_view(), name='list')
]