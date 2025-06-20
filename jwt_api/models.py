from django.db import models
from django.contrib import admin
from django.contrib.auth.models import AbstractUser, PermissionsMixin, BaseUserManager
from datetime import datetime
from django.utils.timezone import now

class CustomUserManager(BaseUserManager):
	def create_user(self, username, email, password=None, **extra_fields):
		if not email:
			raise ValueError('The email field is required')
		email = self.normalize_email(email)
		user = self.model(username=username, email=email, **extra_fields)
		user.set_password(password)
		user.save(using=self._db)
		return user 

	def create_superuser(self, username, email, password=None, **extra_fields):
		extra_fields.setdefault('is_staff', True)
		extra_fields.setdefault('is_superuser', True)

		return self.create_user(username, email, password, **extra_fields)

class CustomUser(AbstractUser, PermissionsMixin):
	ROLE_CHOICES = [('admin', 'Admin'), ('user', 'User'),]
	role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='user')
	last_active = models.DateTimeField(null=True, blank=True, default=now) 
	latest_token = models.CharField(max_length=255, null=True, blank=True)
	is_2fa_enabled = models.BooleanField(default=False)
	remember_me = models.BooleanField(default=False)
	objects = CustomUserManager()

	def update_last_active(self):
		self.last_active = datetime.now()
		self.save()

	def __str__(self):
		return self.username

class ActiveToken(models.Model):
    user = models.ForeignKey('jwt_api.CustomUser', on_delete=models.CASCADE)
    refresh_token = models.CharField(max_length=255)

    def __str__(self):
        return f"Active Token : {self.user.username}"