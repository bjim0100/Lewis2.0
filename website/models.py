from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager


# class UserManager(BaseUserManager):
#
#     def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
#         if not email:
#             raise ValueError("User must have email")
#         if not password:
#             raise ValueError("User must have a password")
#         user_obj = self.model(
#             email=self.normalize_email(email)
#         )
#         user_obj.set_password(password)
#         user_obj.staff = is_staff
#         user_obj.admin = is_admin
#         user_obj.active = is_active
#         user_obj.save(using=self._db)
#         return user_obj
#
#     def create_staffuser(self, email, password=None,is_staff = True):
#         user = self.create_user(
#             email,
#             password=password,
#             is_staff=is_staff
#         )
#         return user
#
#     def create_superuser(self, email, password=None):
#         user = self.create_user(
#             email,
#             password=password,
#             is_staff=True,
#             is_admin=True,
#         )
#         return user
#
#
# class User(AbstractBaseUser):
#     email = models.EmailField(unique=True, max_length=255)
#     full_name = models.CharField(max_length=255, blank=True, null=True)
#     active = models.BooleanField(default=True)
#     staff = models.BooleanField(default=False)
#     admin = models.BooleanField(default=False)
#     timestamp = models.DateTimeField(auto_now_add=True)
#
#     USERNAME_FIELD = 'email'
#     REQUIRED_FIELDS = []
#
#     objects = UserManager()
#
#     def has_perm(self, perm, obj=None):
#         return self.is_admin
#
#     def has_module_perms(self, app_label):
#         return self.is_admin
#
#     def __str__(self):
#         return self.email
#
#     def get_full_name(self):
#         return self.email
#
#     def get_short_name(self):
#         return self.email
#
#     @property
#     def is_staff(self):
#         return self.staff
#
#     @property
#     def is_admin(self):
#         return self.admin
#
#     @property
#     def is_active(self):
#         return self.active

class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_admin=False, is_staff=False):
        if not email:
            raise ValueError("User must have an email")
        if not password:
            raise ValueError("User must have a password")
        user_obj = self.model(
            email=self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.staff = is_staff
        user_obj.admin = is_admin
        user_obj.active = is_active
        user_obj.save(using=self._db)
        return user_obj

    def create_business(self, email, password=None, is_individual=True, is_active=True, is_admin=False,
                        is_staff=False):
        user = self.create_user(
            email,
            password=password,
            is_staff=is_staff,
            is_active=is_active,
            is_individual=is_individual
        )
        return user

    def create_staffuser(self, email, password=None, is_active=True, is_staff=True):
        user = self.create_user(
            email,
            password=password,
            is_staff=is_staff,
            is_active=is_active
        )
        return user

    def create_superuser(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
            is_staff=True,
            is_active=True,
            is_admin=True
        )
        return user


class User(AbstractBaseUser):
    full_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=55, unique=True)
    active = models.BooleanField(default=True)

    individual = models.BooleanField(default=False,
                                     help_text="Click to create an individual account")
    admin = models.BooleanField(default=False)
    staff = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def has_perm(self, perm, obj=None):
        return self.is_admin

    def has_module_perms(self, app_label):
        return self.is_admin

    objects = UserManager()

    def __str__(self):
        return self.email

    @property
    def is_staff(self):
        return self.staff

    @property
    def is_admin(self):
        return self.admin

    @property
    def is_active(self):
        return self.active
