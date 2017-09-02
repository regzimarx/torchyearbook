from django.shortcuts import render, redirect
from django.views.generic import TemplateView, View
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

from .forms import RegisterForm, LoginForm, AccountForm
from .models import User

class IndexView(TemplateView):
    """ View for index """

    def get(self, request):
        return render(request, 'users/index.html', {})


class LoginView(TemplateView):
    """ View for login """

    def get(self, request):
        form = LoginForm()
        context_data = {}
        context_data['form'] = form
        return render(request, 'users/login.html', context_data)

    def post(self, request):
        context_data = {}
        form = LoginForm(request.POST)

        if form.is_valid():
            user = authenticate(request, username=request.POST.get('email'),
                password=request.POST.get('password'))
            if user:
                login(request, user)
                return redirect('account')
            messages.warning(request, 'No account is associated with the credentials provided.')

        context_data['form'] = form
        return render(request, 'users/login.html', context_data)


class RegisterView(TemplateView):
    """ View for register """
    def get(self, request):
        form = RegisterForm()
        context_data = {}
        context_data['form'] = form
        return render(request, 'users/register.html', context_data)

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
        context_data = {}
        context_data['form'] = form
        return render(request, 'users/register.html', context_data)


class AccountView(TemplateView):
    """ view for account """
    def get(self, request):
        context_data = {}
        user = User.objects.get(pk=request.user.id)
        form = AccountForm(initial=user.__dict__)
        context_data['form'] = form
        return render(request, 'users/account.html', context_data)

    def post(self, request):
        context_data = {}
        form = AccountForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('account')
        import pdb; pdb.set_trace()
        context_data['form'] = form
        return render(request, 'users/account.html', context_data)


class LogoutView(View):
    """ View for logout """
    def get(self, request):
        logout(request)
        return redirect('index')