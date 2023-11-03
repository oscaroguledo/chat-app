from __future__ import unicode_literals
from django.db import models 
from django.contrib.auth.models import User, BaseUserManager,AbstractBaseUser, PermissionsMixin, Group,GroupManager
from django.contrib.auth.hashers import make_password
from django.db import transaction
from django.utils import timezone


# Create your models here.

## Custom User model----------------------------------------------------------------------------
class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone = models.CharField(verbose_name="Phone number",max_length=11, unique=True)
    country = models.CharField(max_length=30, blank=False)
    email = models.EmailField(verbose_name="email address",max_length=40, unique=True)
    username = models.CharField(max_length=30, blank=True,unique=True)
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    profile_img = models.URLField(max_length=3000, blank=True)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_admin=models.BooleanField(default=False)
    is_superuser =models.BooleanField(default=False)
    date_joined = models.DateTimeField(auto_now_add=True)


class Platform(models.Model):
    name  = models.CharField(max_length=100, blank=True)


class Message(models.Model):
    details = models.CharField(max_length=255)
    sent_by = models.ForeignKey(Profile, on_delete=models.DO_NOTHING)
    received_by = models.ManyToManyField(Profile)
    viewed_by = models.ManyToManyField(Profile)
    types= (("Community","Community"),("PrivateChat","PrivateChat"))
    room_type = models.CharField(max_length=50, choices=types)
    room_id = models.PositiveIntegerField()
    platform = models.CharField(max_length=50)
    
    @property
    def recieved_message(self,profile):
        self.received_by.add(profile)
    @property
    def viewed_message(self,profile):
        self.viewed_by.add(profile)

    def save(self, *args, **kwargs):
        details = kwargs.pop('message', None)
        sent_by = kwargs.pop('sent_by', None)
        room_type = kwargs.pop('room_type', None)
        room_id = kwargs.pop('room_id', None)
        platform = kwargs.pop('platform', None)

        if details is not None:
            self.details = details
        if sent_by is not None:
            self.sent_by = sent_by
        if room_type is not None:
            self.room_type = room_type
        if room_id is not None:
            self.room_id = room_id
        if platform is not None:
            self.platform = platform

        super(Message, self).save(*args, **kwargs)

                

class Room(models.Model):
    _id = models.CharField(max_length=1000, blank=True)
    image = models.CharField(max_length=2000, null=True, blank=True)
    date_created = models.DateTimeField(auto_now_add=True)

    @property
    def set_max_members(self,num):
        self.max_members=num


class Community(Room):
    name = models.CharField(max_length=100, blank=True)
    members = models.ManyToManyField(Profile)
    added_members = models.ManyToManyField(Profile, related_name='added_to', through='Communitymember')
    max_members= models.IntegerField(blank=True, null=True)

    messages = models.ManyToManyField(Message)
    added_messages = models.ManyToManyField(Message, related_name='added_to', through='Communitymessage')

    admins = models.ManyToManyField(Profile)
    created_by = models.CharField(max_length=100, blank=True)
    @property
    def add_admin(self, member_id):
        pass
    @property
    def remove_admin(self,member_id):
        pass
    @property
    def add_member(self,member_id,added_on):
        if member_id is not None:
            try:
                member = Profile.objects.get(id=member_id)
            except member.DoesNotExist:
                member = None

            # Add the item to the many-to-many field if it exists
            if member:
                self.members.add(member)
                mem = self.members.get(id=member_id)
                mem.joined_date=added_on
                mem.save()
                self.save()
    @property
    def remove_member(self,member_id):
        if member_id is not None:
            try:
                member = Profile.objects.get(id=member_id)
            except member.DoesNotExist:
                member = None

            # Add the item to the many-to-many field if it exists
            if member:
                self.members.remove(member)
                self.save()
    @property
    def add_message(self,message,sender_id,platform,sent_on):  
        sender = Profile.objects.get(id=sender_id)
        if sender:
            messageinstance, messagecreated = Message.objects.get_or_create(details=message,sent_by=sender,room_type="Community",room_id=self.id,platform=platform)
            if messagecreated:
                self.messages.add(messageinstance)
                mem = self.messages.get(id=messageinstance.id)
                mem.created_date=sent_on
                mem.save()
                self.save()
    @property
    def edit_message(self,message_id, new_message):  
        messageinstance= Message.objects.get(message=message_id)
        if messageinstance:
            messageinstance.details=new_message
            self.save()
    @property
    def remove_message(self,message_id):  
        messageinstance= Message.objects.get(message=message_id)
        if messageinstance:
            self.messages.remove(messageinstance)
            self.save()
    

class Communitymember(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    member = models.ForeignKey(Profile, on_delete=models.CASCADE)
    joined_date = models.CharField(max_length=100, blank=True)

    @property
    def add_date(self,date):
        self.joined_date = date
class Communitymessage(models.Model):
    community = models.ForeignKey(Community, on_delete=models.CASCADE)
    message = models.ForeignKey(Message, on_delete=models.CASCADE)
    created_date = models.CharField(max_length=100, blank=True)
    @property
    def add_date(self,date):
        self.created_date = date




class PrivateChat(Room):
    name = models.CharField(max_length=100, blank=True)
    max_members =models.IntegerField(blank=True, null=True, default=2)
    created_by = models.CharField(max_length=100, blank=True)

       