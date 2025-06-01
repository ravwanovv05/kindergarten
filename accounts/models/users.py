from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    ROLE_CHOICES = (
        ('user', 'User'),
        ('admin', 'Admin'),
        ('manager', 'Manager'),
        ('director', 'Director'),
        ('nursery', 'Nursery'),
        ('nurse', 'Nurse'),
        ('chef', 'Chef'),
        ('parent', 'Parent'),
        ('civil_servant', 'Civil Servant'),
    )
    first_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='First name')
    last_name = models.CharField(max_length=50, blank=True, null=True, verbose_name='Last name')
    phone_number = models.CharField(max_length=13, blank=True, null=True, verbose_name='Phone number')
    username = models.CharField(max_length=30, unique=True, verbose_name='Username')
    password = models.CharField(max_length=128, verbose_name='Password')
    date_of_birth = models.DateField(blank=True, null=True, verbose_name='Date of birth')
    role = models.CharField(max_length=20, default='user', choices=ROLE_CHOICES, blank=True, null=True, verbose_name='Role')
    salary_status = models.BooleanField(default=False, blank=True, null=True, verbose_name='Salary status')
    kindergarten_id = models.ForeignKey('main.Kindergarten', on_delete=models.CASCADE, verbose_name='Kindergarten ID')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Created at')

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'

    def __str__(self):
        return self.username




