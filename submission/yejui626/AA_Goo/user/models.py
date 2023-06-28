from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from jsonfield import JSONField

###MySQL
class UserManager(BaseUserManager):
    def _create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError("The Email field must be set")
        
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
    
    def create_user(self, email, password, **extra_fields):
        """Create and save a regular User with the given email and password."""
        extra_fields.setdefault("is_staff", False)
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)
    
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        return self._create_user(email, password, **extra_fields)

class User(AbstractBaseUser,PermissionsMixin):
    USER_TYPE_CHOICES = (
        ('customer', 'Customer'),
        ('technical_worker', 'Technical Worker'),
        ('senior_management', 'Senior Management'),
    )

    email = models.EmailField(unique=True)
    name = models.CharField(max_length=255)  # Name field
    user_type = models.CharField(max_length=20, choices=USER_TYPE_CHOICES)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name','user_type']

    objects = UserManager()

    class Meta:
        verbose_name = 'User'
        app_label = 'user'
    
    def __str__(self):
        return self.email

class Story(models.Model):
    href = models.URLField()
    title = models.CharField(max_length=255)
    comments = models.IntegerField()
    container = JSONField()
    submit_date = models.DateTimeField()
    topic = JSONField()
    promote_date = models.DateTimeField()
    idJSON = models.CharField(max_length=255)
    media = models.CharField(max_length=255)
    diggs = models.IntegerField()
    description = models.TextField()
    link = models.URLField()
    user = JSONField()
    status = models.CharField(max_length=255)
    shorturl = JSONField()

    class Meta:
        verbose_name = 'Story'
        app_label = 'user'
