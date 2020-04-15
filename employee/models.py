from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models


class EmployeeModel(AbstractBaseUser, PermissionsMixin):
    """Represents an employee in a system
    """
    email = models.EmailField(max_length=128, unique=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
