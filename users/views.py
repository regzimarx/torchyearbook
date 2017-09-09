from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm, LoginForm, AccountForm
from .models import User

class IndexView(TemplateView):
    """ View for index
    """

    template_name = 'users/index.html'


class LoginView(TemplateView):
    """ View for login
    """

    template_name = 'users/login.html'

    def get_context_data(self):
        context = super(LoginView, self).get_context_data()
        context['form'] = LoginForm()
        return context

    def post(self, request):
        context_data = {}
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request, username=request.POST.get('email'),
                password=request.POST.get('password'))
            if user:
                login(request, user)
                return redirect('account:profile')
            messages.warning(request, 'No account is associated with the credentials provided.')

        context_data['form'] = form
        return render(request, 'users/login.html', context_data)


class RegisterView(TemplateView):
    """ View for register """

    template_name = 'users/register.html'

    def get_context_data(self):
        context = super(RegisterView, self).get_context_data()
        form = RegisterForm()
        context['form'] = RegisterForm()
        return context

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context_data = {}
        context_data['form'] = form
        return render(request, 'users/register.html', context_data)


class ProfileView(TemplateView):
    """ view for account """

    template_name = 'users/profile.html'

    def get_context_data(self):
        context = super(ProfileView, self).get_context_data()
        user = User.objects.get(pk=self.request.user.id)
        context['user'] = user
        return context


class UpdateProfileView(TemplateView):
    """ View for updating profile """

    template_name = 'users/update_profile.html'

    def get_context_data(self):
        context = super(UpdateProfileView, self).get_context_data()
        user = User.objects.get(pk=self.request.user.id)
        context['form'] = AccountForm(initial=user.__dict__)
        return context

    def post(self, request):
        context_data = {}
        form = AccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account:profile')
        context_data['form'] = form
        return render(request, 'users/update_profile.html', context_data)


class LogoutView(View):
    """ View for logout """

    def get(self, request):
        logout(request)
        return redirect('account:index')