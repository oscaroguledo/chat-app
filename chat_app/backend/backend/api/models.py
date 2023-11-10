from __future__ import unicode_literals
from django.db import models 
from django.contrib.auth.models import User, BaseUserManager,AbstractBaseUser, PermissionsMixin, Group,GroupManager
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.utils import timezone
import uuid, datetime


# Create your models here.

## Custom User model----------------------------------------------------------------------------
class UserAccountManager(BaseUserManager):
    def create_user(self, username, email, phone, first_name, last_name,country,gender, date_joined, password=None, **kwargs):
        if not phone:
            raise ValueError('Accounts must have a  phone number')
        if not email:
            raise ValueError('Accounts must have a  email')
        if not username:
            raise ValueError('Accounts must have a  username')
        if not first_name:
            raise ValueError('Accounts must have a  first name')
        if not last_name:
            raise ValueError('Accounts must have a  last name')
        if not country:
            raise ValueError('Accounts must have a  country')
        if not gender:
            raise ValueError('Accounts must have a  gender')
        user = self.model(username=username, phone=phone, email=email, first_name=first_name, last_name=last_name, country=country, gender=gender, date_joined=date_joined)
        self.password = make_password(password)
        user.set_password(self.password)
        user.save(using=self._db)
        return user

    def create_adminuser(self, username, email, phone, first_name, last_name,country,gender, password, date_joined):
        user = self.model(username=username, phone=phone, email=email, first_name=first_name, last_name=last_name, country=country, gender=gender,
                          password=make_password(password), date_joined=date_joined)

        user.is_staff = True
        user.is_superuser = False
        user.save(using=self._db)
        return user

    def create_superuser(self, username, email, phone, first_name, last_name,country,gender, password, date_joined):
        user = self.model(username=username, phone=phone, email=email, first_name=first_name, last_name=last_name, country=country, gender=gender,
                          password=make_password(password), date_joined=date_joined)

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
    
class Profile(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    phone = models.CharField(verbose_name="Phone number",max_length=11, blank=True,unique=True)
    country = models.CharField(max_length=30, blank=True)
    email = models.EmailField(verbose_name="email address",max_length=40, blank=True,unique=True)
    username = models.CharField(max_length=30, blank=True,unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    profile_img = models.URLField(max_length=3000, blank=True)
    d = (('M', 'Male'),
         ('F', 'Female'),
         )
    gender = models.CharField(verbose_name='gender', choices=d, max_length=100, blank=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=False)

    objects = UserAccountManager()
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['phone', 'email', 'last_name','first_name','country','gender']

    def __str__(self):
        self.name = f"{self.first_name} {self.last_name} -({self.username})"
        return self.name

    def has_module_perms(self, app_label):
        return self.is_superuser

    def has_perm(self, perm, obj=None):
        return self.is_superuser
    class Meta:
        ordering = ['-date_joined']


class Platform(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name  = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return self.name


class PrivateMessage(models.Model):
    details = models.CharField(max_length=255)
    sender = models.ForeignKey(Profile, on_delete=models.SET_NULL,related_name="sent_by",null=True)
    receiver = models.ForeignKey(Profile, on_delete=models.SET_NULL,related_name="received_by",null=True)
    viewed = models.BooleanField(default=False)
    received =models.BooleanField(default=False)
    platform = models.CharField(max_length=50)
    created_date = models.DateTimeField(auto_now_add=False, editable=False)
    def __str__(self):
        self.name = f"id({self.id})  date({self.created_date})"
        return self.name
    class Meta:
        ordering = ['-created_date']


class Community(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, blank=True)
    profile_image = models.URLField(null=True, blank=True)
    max_members= models.PositiveIntegerField(blank=True,null=True,default=None)
    created_by = models.CharField(max_length=100000, blank=False,null=True, editable=False)
    created_on = models.DateTimeField(auto_now_add=False,null=True, editable=False)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Communities"
        ordering = ['-created_on']

class CommunityMember(models.Model):
    user= models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    community = models.ForeignKey(Community, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.user.id}-{self.user.username} ({self.community.id})"
    class Meta:
        ordering = ['user__first_name']
class CommunityAdmin(models.Model):
    user= models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    community = models.ForeignKey(Community, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f"{self.user.id}-{self.user.username} ({self.community.id})"
    class Meta:
        ordering = ['user__first_name']

class CommunityMessage(models.Model):
    sent_by= models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)
    community = models.ForeignKey(Community, on_delete=models.SET_NULL, null=True)
    media = models.URLField(null=True, blank=True)
    details= models.TextField(null=True, blank=True)
    date = models.DateTimeField(auto_now_add=False,null=True)
    def __str__(self):
        return f"{self.community.id}-({self.sent_by.id} {self.sent_by.id})"
    class Meta:
        ordering = ['-date']

class CommunityMessageRecipient(models.Model):
    message = models.ForeignKey(CommunityMessage, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.id}-{self.user.username} ({self.message.community.id})"
    class Meta:
        ordering = ['-date']

class CommunityMessageViewer(models.Model):
    message = models.ForeignKey(CommunityMessage, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"{self.user.id}-{self.user.username} ({self.message.community.id})"
    class Meta:
        ordering = ['-date']

       