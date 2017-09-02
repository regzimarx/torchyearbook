from django.conf.urls import url

from .views import IndexView, LoginView, RegisterView, AccountView, LogoutView

urlpatterns = [
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^login/', LoginView.as_view(), name='login'),
    url(r'^register/', RegisterView.as_view(), name='register'),
    url(r'^account/', AccountView.as_view(), name='account'),
    url(r'^logout/', LogoutView.as_view(), name='logout'),
]