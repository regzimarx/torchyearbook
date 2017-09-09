from django.db import models


class Department(models.Model):
    """ Model for Department """

    short_name = models.CharField(max_length=10)
    name = models.CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.name)


class Course(models.Model):
    """ Model for Course """

    short_name = models.CharField(max_length=10)
    name = models.CharField(max_length=250)
    department = models.ForeignKey('Department')

    def __str__(self):
        return '{}'.format(self.name)