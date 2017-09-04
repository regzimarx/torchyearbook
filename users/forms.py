from django import forms

from .models import User

class RegisterForm(forms.ModelForm):
    """ Form for registration """

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password')
        widgets = {
            'password': forms.PasswordInput()
        }

    def save(self):
        User.objects.create_user(
            self.cleaned_data.get('email'),
            self.cleaned_data.get('first_name'),
            self.cleaned_data.get('last_name'),
            self.cleaned_data.get('password'),
        )


class LoginForm(forms.Form):
    """ Form for login """

    email = forms.EmailField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput())


class AccountForm(forms.ModelForm):
    """ Form for account """

    email = forms.EmailField(required=False)
    middle_name = forms.CharField(required=False)
    affiliations = forms.CharField(widget=forms.Textarea, required=False)
    awards = forms.CharField(widget=forms.Textarea, required=False)

    class Meta:
        model = User
        fields = ('email', 'first_name', 'middle_name', 'last_name', 'nick_name',
            'department', 'course', 'birthdate', 'mobile_number', 'age', 'father_name',
            'mother_maiden_name', 'address', 'affiliations', 'awards',)
