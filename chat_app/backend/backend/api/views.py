import json
import requests
import threading
import calendar
import datetime
from collections import Counter
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from django.contrib.auth.models import User
from .models import Profile, Community
from .serializers import (
    ProfileSerializer
    )
#from heyoo import WhatsApp

# Create your views here.

# api for serverstatus begins here---------------------------
@method_decorator(csrf_exempt, name="dispatch")
class serverStatus(APIView):
    def get(self, request):
        return Response(
            {"info": f"Welcome to {settings.APPNAME} 1.0"},
            status=status.HTTP_200_OK,
        )

class Profiles(APIView):
    def post(self, request):
        data = request.data
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            email = data.get("email")
            country = data.get("country")
            phone = data.get("phone")
            username = email.split('@')[0]
            first_name = data.get("first_name")
            last_name = data.get("last_name")
            password = data.get("password")
            user = User.objects.create_user(username=username,email=email,password=password,first_name=first_name,last_name=last_name)
            profile = Profile.objects.create(user=user, username=username,email=email,password=password,country=country,
                                             phone=phone,first_name=first_name,last_name=last_name)
            print(profile)
            return Response(
                            {
                                "message": f"User {email} has been created",
                                "response": email,
                            },
                            status=status.HTTP_201_CREATED,
                        )
        else:
            default_errors = serializer.errors
            new_error = {}
            for field_name, field_errors in default_errors.items():
                new_error[field_name] = field_errors[0]
            return Response(new_error, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request, email):
        user = Profile.objects.get(email=email)
        return Response(
                {
                    "message": f"User with username-{user.username} was found",
                    "response": user,
                },
                status=status.HTTP_200_OK,
            )
    def patch(self,request,email):
        data = request.data
        user = Profile.objects.get(email=email)
        if data.get("email"):
            email = data.get("email")
        
        if data.get("country"):
            user.country = data.get("country")

        if data.get("phone"):
            user.phone = data.get("phone")
        
        if data.get("username"):
            user.username = data.get("username")
        
        if data.get("first_name"):
            user.first_name = data.get("first_name")
        
        if data.get("last_name"):
            user.last_name = data.get("last_name")

        user.save()
        return Response(
                {
                    "message": f"User has been successully updated",
                    "response": user,
                },
                status=status.HTTP_200_OK,
            )

class Communities(APIView):
    pass

@method_decorator(csrf_exempt, name="dispatch")
class Message(APIView):
    def post(self, request):
        data = request.data
        payload={
            "message":data["message"],
            "phone":data["phone"],
            "email":data["email"],
            "username":data["username"],
            "room_type":data["room_type"]
        }
        room_type
@method_decorator(csrf_exempt, name="dispatch")
class Member(APIView):
    def post(self, request):
        return Response(data={"isSuccess":True,"response":"In progress"},status=200)
    def get(self, request, member_id):
        return Response(data={"isSuccess":True,"response":"In progress"},status=200)
    def patch(self, request, member_id):
        return Response(data={"isSuccess":True,"response":"In progress"},status=200)
class CommunityClass(APIView):
    def add_member_to_group(self,member_id, group_id,added_on):
        #check if a member with such id exists------------------
        try:
            member = Profile.objects.get(id=member_id)
        except member.DoesNotExist:
            member = None

        if member:
            if group_id is not None:
                try:
                    community = Community.objects.get(id=group_id)
                except community.DoesNotExist:
                    community = None

                if community:
                    community.add_member(member_id=member.id,added_on=added_on)
                    return Response(data={"isSuccess":True,"response":f"Successfully added user-{member} on{added_on} to group {community}"},status=200)
            
            return Response(data={"isSuccess":False,"response":f"Sorry the group-{group_id} doesn't exist"},status=400)
        
        return Response(data={"isSuccess":True,"response":f"Sorry this person-{member} doesn't exist"},status=200)
    def remove_member_from_group(self,member_id,group_id,deleter_id):
        try:
            community = Community.objects.get(id=group_id)
        except community.DoesNotExist:
            community = None

        if community:
            #check if the deleter is a member of the group----------
            if community.admins.get(id=deleter_id):
                community.remove_member(member_id)
                return Response(data={"isSuccess":True,"response":f"Deleted message from group {community}"},status=200)
                
            return Response(data={"isSuccess":False,"response":f"You dont have permission to remove a member of the group"},status=400)
    
        return Response(data={"isSuccess":False,"response":f"This group-{group_id} doesn't exist"},status=400)
    
    def send_message_to_group(self,message,group_id,sender_id,platform,sent_on):
        try:
            community = Community.objects.get(id=group_id)
        except community.DoesNotExist:
            community = None

        if community:
            community.add_message(message,sender_id,platform,sent_on)
            return Response(data={"isSuccess":True,"response":f"Sent message to group {community}"},status=200)

        return Response(data={"isSuccess":False,"response":f"This group-{group_id} doesn't exist"},status=400)
    def edit_message_in_group(self,message_id,new_message,group_id,editor_id):
        try:
            community = Community.objects.get(id=group_id)
        except community.DoesNotExist:
            community = None

        if community:
            #check if the deleter is a member of the group----------
            if community.members.get(id=editor_id):
                message = Message.objects.get(id=message_id)
                if message.sent_by.id ==editor_id:
                    community.edit_message(message.id, new_message)
                    return Response(data={"isSuccess":True,"response":f"Edited message from group {community}"},status=200)
                return Response(data={"isSuccess":False,"response":f"You dont have permission to edit this message"},status=400)
            return Response(data={"isSuccess":False,"response":f"You are a member of this group"},status=400)
    
        return Response(data={"isSuccess":False,"response":f"This group-{group_id} doesn't exist"},status=400)
    def delete_message_from_group(self,message_id,group_id,deleter_id):
        try:
            community = Community.objects.get(id=group_id)
        except community.DoesNotExist:
            community = None

        if community:
            #check if the deleter is a member of the group----------
            if community.members.get(id=deleter_id):
                message = Message.objects.get(id=message_id)
                if message.sent_by.id ==deleter_id:
                    community.remove_message(message.id)
                    return Response(data={"isSuccess":True,"response":f"Deleted message from group {community}"},status=200)
                return Response(data={"isSuccess":False,"response":f"You dont have permission to delete this message"},status=400)
            return Response(data={"isSuccess":False,"response":f"You are a member of this group"},status=400)
    
        return Response(data={"isSuccess":False,"response":f"This group-{group_id} doesn't exist"},status=400)
    
    def view_group(self,request, member_id,group_id):
        try:
            member = Profile.objects.get(id=member_id)
        except member.DoesNotExist:
            member = None

        if member:
            try:
                community = Community.objects.get(id=group_id)
            except community.DoesNotExist:
                community = None

            if community:
                for message in community.messages.all():
                    message.viewed_message(member)
    def set_admin(self,member_id,group_id, setter_id):
        pass
    def remove_admin(self,member_id,group_id, remover_id):
        pass
        
    def post(self, request):
        data = request.data
        if data["type"] == "set_admin":
            payload={
                "community_id":data["community_id"],
                "member_id":data["member_id"],
                "setter_id":data["setter_id"]
            }
            #use serializer
            self.set_admin(payload["member_id"],payload["community_id"], payload["setter_id"])
        elif data["type"] == "remove_admin":
            payload={
                "community_id":data["community_id"],
                "member_id":data["member_id"],
                "remover_id":data["remover_id"]
            }
            #use serializer
            self.remove_admin(payload["member_id"],payload["community_id"],data["remover_id"])
        elif data["type"] == "add_member":
            payload={
                "community_id":data["community_id"],
                "member_id":data["member_id"],
                "added_on":data["added_on"]
            }
            #use serializer
            self.add_member_to_group(payload["member_id"],payload["community_id"], payload["added_on"])
        elif data["type"] == "delete_member":
            payload={
                "community_id":data["community_id"],
                "member_id":data["member_id"],
                "deleter_id":data["deleter_id"]
            }
            #use serializer
            self.remove_member_from_group(payload["member_id"],payload["community_id"],data["deleter_id"])

        elif data["type"] == "send_message":
            payload={
                "community_id":data["community_id"],
                "message":data["message"],
                "sender_id":data["sender_id"],
                "platform":data["platform"],
                "sent_on":data["sent_on"]
            }
            #use serializer
            self.send_message_to_group(payload["message"],payload["community_id"],data["sender_id"],data["platform"], payload["sent_on"])
        elif data["type"] == "edit_message":
            payload={
                "community_id":data["community_id"],
                "message_id":data["message_id"],
                "editor_id":data["editor_id"],
                "new_message":data["new_message"]
            }
            #use serializer
            self.edit_message_in_group(payload["message_id"], payload["new_message"],payload["community_id"],data["editor_id"],data["platform"])
        elif data["type"] == "delete_message":
            payload={
                "community_id":data["community_id"],
                "message_id":data["message_id"],
                "deleter_id":data["deleter_id"]
            }
            #use serializer
            self.delete_message_from_group(payload["message_id"],payload["community_id"],data["deleter_id"])
        elif data["type"] == "view_group":
            payload={
                "community_id":data["community_id"],
                "member_id":data["member_id"]
            }
            #use serializer
            self.view_group(data["member_id"],payload["community_id"])
    def get(self, request,group_id,member_id):
        pass
    def patch(self,request, group_id,member_id):
        pass

            
        
"""
@method_decorator(csrf_exempt, name="dispatch")
class send_message(APIView):
    def post(self, request):
        
        messenger = WhatsApp('EABJj1xxxxxx',phone_number_id='+2348153452214')
        print(messenger)
        # For sending a Text messages
        messenger.send_message('Hello I am WhatsApp Cloud API', '+44747716596')
        # For sending an Image
        messenger.send_image(
                image="https://i.imgur.com/YSJayCb.jpeg",
                recipient_id="+44747716596",
            )
        return Response(
                {"message": "List of jobs.", "response": json.loads(messenger)},
                status=status.HTTP_200_OK,
            )"""



