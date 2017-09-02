from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):

    def create_user(self, email, first_name, last_name, password, **kwargs):
        """ Create a user """

        if not email:
            raise ValueError('Email address is required.')

        account = self.model(
            email=self.normalize_email(email),
            first_name=first_name,
            last_name=last_name,
            **kwargs
        )

        account.set_password(password)
        account.save()

        return account

    def create_superuser(self, email, first_name, last_name, password, **kwargs):
        """ Create a superuser """

        account = self.create_user(
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
        )

        account.is_staff = True
        account.is_superuser = True
        account.save()

        return account

