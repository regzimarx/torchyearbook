from django.conf.urls import url

from .views import (
    IndexView,
    LoginView,
    RegisterView,
    ProfileView,
    LogoutView,
    UpdateProfileView,
)

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^profile/', ProfileView.as_view(), name='profile'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
    url(r'^update-profile/', UpdateProfileView.as_view(), name='update_profile')
]