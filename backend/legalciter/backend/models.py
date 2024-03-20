from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.db import models
from django.utils import timezone
from django.utils.translation import gettext_lazy as _

from .managers import CustomUserManager
    

class Case(models.Model):
    case_id = models.PositiveIntegerField(unique=True)
    title = models.CharField(max_length=100, default='')
    pub_date = models.DateTimeField()
    case_text = models.TextField()

    highlighted = models.TextField()

    def __str__(self) -> str:
        return self.title
    
    def save(self, *args, **kwargs):
        options = {'title': self.title} if self.title else {}
        super().save(*args, **kwargs)
    

class Cite(models.Model):
    cite_id = models.PositiveIntegerField(unique=True)
    name = models.CharField(max_length=100, default='')
    date_created = models.DateTimeField(auto_now_add=True)
    cite_text = models.TextField()

    owner = models.ForeignKey('backend.CustomUser', related_name='cites', on_delete=models.CASCADE)
    highlighted = models.TextField()

    def __str__(self) -> str:
        return self.name
    
    def save(self, *args, **kwargs):
        options = {'name': self.name} if self.name else {}
        super().save(*args, **kwargs)


class CustomUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(_("email address"), unique=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    date_joined = models.DateTimeField(default=timezone.now)
    # cite = models.ForeignKey(Cite, on_delete=models.CASCADE, verbose_name="the related cite", null=False, default=None)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email