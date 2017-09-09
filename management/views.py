from django.utils import timezone
from django.shortcuts import render
from django.views.generic import TemplateView

from users.models import User

class ProfilesListView(TemplateView):
    """ View for list of all profiles """

    template_name = 'management/list.html'

    def get_context_data(self):
        context = super(ProfilesListView, self).get_context_data()
        context['profiles'] = User.objects.filter(
            is_staff=False,
            date_joined__year=timezone.now().year
        )
        return context
