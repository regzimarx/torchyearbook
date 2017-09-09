from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin

from .managers import CustomUserManager


class User(AbstractBaseUser, PermissionsMixin):
    """ Create a custom class for the users or accounts to enable adding of
    custom fields """

    REGULAR = 'regular'
    STAFF = 'staff'

    LIST_OF_ROLES = (
        (REGULAR, 'Regular'),
        (STAFF, 'Staff'),
    )

    MALE = 'male'
    FEMALE = 'female'

    LIST_OF_GENDER = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
    )

    email = models.EmailField(unique=True)
    username = models.CharField(max_length=50, null=True, blank=True)
    first_name = models.CharField(max_length=100, null=True)
    middle_name = models.CharField(max_length=100, null=True)
    last_name = models.CharField(max_length=100, null=True)

    department = models.ForeignKey('management.Department', null=True)
    course = models.ForeignKey('management.Course', null=True)

    nick_name = models.CharField(max_length=20, null=True)
    birthdate = models.DateField(null=True)
    mobile_number = models.CharField(max_length=13, null=True)
    age = models.IntegerField(null=True)
    father_name = models.CharField(max_length=250, null=True)
    mother_maiden_name = models.CharField(max_length=250, null=True)
    address = models.CharField(max_length=250, null=True)

    affiliations = models.TextField(null=True)
    awards = models.TextField(null=True)

    role = models.CharField(max_length=7, choices=LIST_OF_ROLES, default=REGULAR)
    gender = models.CharField(max_length=6, choices=LIST_OF_GENDER, default=MALE)

    date_joined = models.DateTimeField()

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name')

    objects = CustomUserManager()

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return '{}'.format(self.first_name)

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

# Steps
# 1. Import `AbstractBaseUser` which has the core implementation for a user model
# 2. Define your model fields. Add `get_short_name()` method.
# 3. Use `USERNAME_FIELD` to identify your unique field which will replace `username`
#    as the default unique field
# 4. Create a custom manager for a custom user model
# 5. Inherit `PermissionsMixin` for the permissions