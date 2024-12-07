from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager

#custom user manager
class UserManager(BaseUserManager):
	def create_user(self, email, name, tc, password=None, password2=None):
		#creates and saves a user with the given name, email, tc and password

		if not email:
			raise ValueError("You must have an email.")
		#refers to the model user is associated with
		user = self.model(
				email = self.normalize_email(email),
				name=name,
				tc=tc,
			)
		user.set_password(password)
		user.save(using=self._db)#saves the user instance to the database
		return user

	def create_superuser(self, email, name, tc, password=None, password2=None):
		#creates and saves a user with the given name, email, tc and password
		if not email:
			raise ValueError("You must have an email")
		user = create_user(
				email,
				password=password,
				name=name,
				tc=tc,
			)
		user.is_admin = True
		user.save(using=self._db)
		return user 


class User(AbstractUser):
	#verbose_name is human readable name for the field
	email = models.EmailField(verbose_name="Email", max_length=100, unique=True)
	name = models.CharField(max_length=200)
	tc = models.BooleanField()
	is_active = models.BooleanField(default=True) #indicates whether the user is active
	is_admin = models.BooleanField(default=False) #indicates whether the user is an admin
	created_at = models.DateTimeField(auto_now_add=True) #time at which the user is created
	updated_at = models.DateTimeField(auto_now_add=True) #time at which the user is updated

	#custom user manager for this model
	objects = UserManager()

	USERNAME_FIELD = "email"
	REQUIRED_FIELDS = ["name", "tc"] 

	def __str__(self):
		return self.email

	def has_perm(self, perm, obj=None):
		#Does the user have specific permission? --> Simply yes, always
		return self.is_admin

	def has_module_perms(self, app_label):
		# Does the user have the permission to view the app 'app_label' --> Yes always
		return True

	@property 
	def is_staff(self):
		#is the user a member of the staff? --> Simply all admins are staff members
		return self.is_admin

























