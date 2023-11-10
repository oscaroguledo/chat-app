import json
import requests
import threading
import calendar
import datetime
from collections import Counter
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from rest_framework import status, generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from django.contrib.auth.models import User
from .models import Profile, Community,PrivateMessage, CommunityAdmin,CommunityMember,CommunityMessage, models
from .serializers import *
from django.core.serializers import serialize
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
    
class SuperAdminProfilesClass(APIView):
    def post(self, request):
        data = request.data
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            email = data.get("email")
            
            try:
                serializer.createsuperuser(data)
            except Exception as error:
                print(error)
                return Response({"isSuccess":False,"errors":error}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(
                            {"message": f"SuperAdmin User {email} has been created",
                                "response": email},
                            status=status.HTTP_201_CREATED,
                        )
        
        new_error = {field_name:field_errors[0] for field_name, field_errors in serializer.errors.items()}
        return Response({"isSuccess":False,"errors":new_error}, status=status.HTTP_400_BAD_REQUEST)

class AdminProfilesClass(APIView):
    def post(self, request):
        data = request.data
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            email = data.get("email")
            
            try:
                serializer.createadminuser(data)
            except Exception as error:
                new_error = {field_name:field_errors for field_name, field_errors in error.detail.items()}
                return Response({"isSuccess":False,"errors":new_error}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(
                            {"message": f"Admin User {email} has been created",
                                "response": email},
                            status=status.HTTP_201_CREATED,
                        )
        
        new_error = {field_name:field_errors[0] for field_name, field_errors in serializer.errors.items()}
        return Response({"isSuccess":False,"errors":new_error}, status=status.HTTP_400_BAD_REQUEST)

class ProfilesClass(APIView):
    def post(self, request):
        data = request.data
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            email = data.get("email")
            
            try:
                serializer.create(data)
            except Exception as error:
                new_error = {field_name:field_errors for field_name, field_errors in error.detail.items()}
                return Response({"isSuccess":False,"errors":new_error}, status=status.HTTP_400_BAD_REQUEST)
            
            return Response(
                            {"message": f"User {email} has been created",
                                "response": email},
                            status=status.HTTP_201_CREATED,
                        )
        
        new_error = {field_name:field_errors[0] for field_name, field_errors in serializer.errors.items()}
        return Response({"isSuccess":False,"errors":new_error}, status=status.HTTP_400_BAD_REQUEST)
    def get(self,request, email,username,phone):
        user = None
        searchparam = None

        if Profile.objects.filter(email=email).exists():
            user = Profile.objects.get(email=email)
            searchparam = {"email":email}
        elif Profile.objects.filter(username=username).exists():
            user = Profile.objects.get(username=username)
            searchparam = {"username":username}
        elif Profile.objects.filter(phone=phone).exists():
            user = Profile.objects.get(phone=phone)
            searchparam = {"phone":phone}

        if user:
            user_details = {field.name: getattr(user, field.name) for field in user._meta.fields}

            return Response(
                    {
                        "message": f"User with {list(searchparam.keys())[0]} -{list(searchparam.values())[0]} was found",
                        "response": user_details,
                    },
                    status=status.HTTP_200_OK,
                )
        return Response(
                {
                    "message": f"User not found"
                },
                status=status.HTTP_404_NOT_FOUND,
            )
    def patch(self,request,email,username,phone):
        data = request.data
        user = None
        searchparam = None

        if Profile.objects.filter(email=email).exists():
            user = Profile.objects.get(email=email)
            searchparam = {"email":email}
        elif Profile.objects.filter(username=username).exists():
            user = Profile.objects.get(username=username)
            searchparam = {"username":username}
        elif Profile.objects.filter(phone=phone).exists():
            user = Profile.objects.get(phone=phone)
            searchparam = {"phone":phone}
        if user:
            if data.get("email"):
                email = data.get("email")
                user.email=email
            
            if data.get("country"):
                user.country = data.get("country")

            if data.get("phone"):
                user.phone = data.get("phone")
            
            if data.get("username"):
                user.username=data.get("username")
            
            if data.get("first_name"):
                user.first_name=data.get("first_name")
            
            if data.get("last_name"):
                user.last_name=data.get("last_name")

            user.save()
            return Response(
                    {
                        "message": f"User with {list(searchparam.keys())[0]} -{list(searchparam.values())[0]}has been successully updated",
                        "response": user,
                    },
                    status=status.HTTP_200_OK,
                )
        return Response(
                {
                    "message": f"User not found"
                },
                status=status.HTTP_404_NOT_FOUND,
            )
    def delete(self,request, email,username,phone,deleter_id):
        user = None
        searchparam = None

        if Profile.objects.filter(email=email).exists():
            user = Profile.objects.get(email=email)
            searchparam = {"email":email}
        elif Profile.objects.filter(username=username).exists():
            user = Profile.objects.get(username=username)
            searchparam = {"username":username}
        elif Profile.objects.filter(phone=phone).exists():
            user = Profile.objects.get(phone=phone)
            searchparam = {"phone":phone}

        if user:
            if Profile.objects.filter(id=deleter_id).exists():
                deleter=Profile.objects.get(id=deleter_id)
                if (deleter.is_superuser == True or deleter.id == user.id):
                    user.delete()
                
                    return Response(
                            {
                                "message": f"User {list(searchparam.keys())[0]} -{list(searchparam.values())[0]} was deleted by {deleter.email}",
                                
                            },
                            status=status.HTTP_200_OK,
                        )
            return Response(
                {
                    "message": f"You do not have the right to delete this user profile"
                },
                status=status.HTTP_404_NOT_FOUND,
            )
            
        return Response(
                {
                    "message": f"User not found"
                },
                status=status.HTTP_404_NOT_FOUND,
            )

class CommunityClass(APIView):
    def create_group(self, creator_id, name, created_on):
        
        if Profile.objects.filter(id=creator_id).exists():
            profile = Profile.objects.get(id=creator_id)
            community = Community.objects.create(name =name,created_by =f"{profile}"+f"-{profile.id}", created_on=created_on)
            
            community_admin = CommunityAdmin.objects.create(user=profile, community=community)
            community_member = CommunityMember.objects.create(user=profile, community=community)
                
            return Response(data={"isSuccess":True,"response":f"Successfully created community -id {community.id}"},status=200)
            
        else:
            return Response(
                {
                    "message": f"User with id - {creator_id}  not found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
            
    def add_member_to_group(self,member_id, group_id,admin_id):
        if Community.objects.filter(id=group_id).exists():
            community = Community.objects.get(id=group_id)
            if CommunityAdmin.objects.filter(user=Profile.objects.get(id=admin_id),community=community).exists():
                profile =Profile.objects.get(id=member_id)
                community_member = CommunityMember.objects.create(user=profile, community=community)
                return Response(data={"isSuccess":True,"response":f"Added {member_id} to community"},status=200)
            
            return Response(data={"isSuccess":False,"response":"You dont have permission to add a member to the community"},status=403)
    
        return Response(data={"isSuccess":False,"response":f"This group-{group_id} doesn't exist"},status=400)
    def remove_member_from_group(self,member_id,group_id,deleter_id):
        if Community.objects.filter(id=group_id).exists():
            community = Community.objects.get(id=group_id)
            deleter = Profile.objects.get(id=deleter_id)
            member = Profile.objects.get(id=member_id)
            is_admin=CommunityAdmin.objects.filter(user=deleter,community=community).exists()
            
            if is_admin or deleter == member:
                community_member = CommunityMember.objects.get(user=member, community=community)
                community_member.delete()
                if deleter == member:
                    return Response(data={"isSuccess":True,"response":f"You have left the community"},status=200)
                else:
                    return Response(data={"isSuccess":True,"response":f"Removed {member_id} from community"},status=200)
            
            return Response(data={"isSuccess":False,"response":"You dont have permission to remove this member to the community"},status=403)
    
        return Response(data={"isSuccess":False,"response":f"This group-{group_id} doesn't exist"},status=400)
    
    def send_message_to_group(self,message,group_id,sender_id,sent_on):
        if Community.objects.filter(id=group_id).exists():
            community = Community.objects.get(id=group_id)
            profile =Profile.objects.get(id=sender_id)
            if CommunityMember.objects.filter(user=profile,community=community).exists():
                
                community_message = CommunityMessage.objects.create(sent_by=profile,details=message, community=community)
                
                return Response(data={"isSuccess":True,"response":f"Sent message to the community"},status=200)
            
            return Response(data={"isSuccess":False,"response":"You dont have permission to send messages to the community"},status=403)
    
        return Response(data={"isSuccess":False,"response":f"This group-{group_id} doesn't exist"},status=400)
    def edit_message_in_group(self,message_id,new_message,group_id,editor_id):
        if Community.objects.filter(id=group_id).exists():
            community = Community.objects.get(id=group_id)
            profile =Profile.objects.get(id=editor_id)
            if CommunityMember.objects.filter(user=profile,community=community).exists():
                
                community_message = CommunityMessage.objects.get(id=message_id)
                if profile == community_message.sent_by:
                    community_message.details=new_message
                    community_message.save()
                    return Response(data={"isSuccess":True,"response":f"Successfully updated message to the community"},status=200)
            
            return Response(data={"isSuccess":False,"response":"You dont have permission to edit messages in the community"},status=403)
    
        return Response(data={"isSuccess":False,"response":f"This group-{group_id} doesn't exist"},status=400)
    def delete_message_from_group(self,message_id,group_id,deleter_id):
        if Community.objects.filter(id=group_id).exists():
            community = Community.objects.get(id=group_id)
            profile =Profile.objects.get(id=deleter_id)
            if CommunityMember.objects.filter(user=profile,community=community).exists():
                
                community_message = CommunityMessage.objects.get(id=message_id)
                community_message.delete()
                
                return Response(data={"isSuccess":True,"response":f"Deleted message from the community"},status=200)
            
            return Response(data={"isSuccess":False,"response":"You dont have permission to delete messages from the community"},status=403)
    
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
        if Community.objects.filter(id=group_id).exists():
            community = Community.objects.get(id=group_id)
            if CommunityAdmin.objects.filter(user=Profile.objects.get(id=setter_id),community=community).exists():
                profile =Profile.objects.get(id=member_id)
                if  CommunityMember.objects.filter(user=profile,community=community).exists():  

                    community_admin = CommunityAdmin.objects.create(user=profile, community=community)
                    return Response(data={"isSuccess":True,"response":f"Added {member_id} as admin"},status=200)
                    
                return Response(data={"isSuccess":False,"response":"This member doesnt belong to this community"},status=403)
                
            return Response(data={"isSuccess":False,"response":"You dont have permission to add admin to the community"},status=403)
    
        return Response(data={"isSuccess":False,"response":f"This group-{group_id} doesn't exist"},status=400)
    def remove_admin(self,member_id,group_id, remover_id):
        if Community.objects.filter(id=group_id).exists():
            community = Community.objects.get(id=group_id)
            if CommunityAdmin.objects.filter(user=Profile.objects.get(id=remover_id),community=community).exists():
                profile =Profile.objects.get(id=member_id)
                if  CommunityMember.objects.filter(user=profile,community=community).exists():  

                    community_admin = CommunityAdmin.objects.get(user=profile, community=community)
                    community_admin.delete()

                    return Response(data={"isSuccess":True,"response":f"Added {member_id} as admin"},status=200)
                    
                return Response(data={"isSuccess":False,"response":"This member doesnt belong to this community"},status=403)
                
            return Response(data={"isSuccess":False,"response":"You dont have permission to remove admin from the community"},status=403)
    
        return Response(data={"isSuccess":False,"response":f"This group-{group_id} doesn't exist"},status=400)
        
    def post(self, request):
        data = request.data
        if data["type"] == "create":
            payload={
                "creator_id":data["creator_id"],
                "name":data["name"],
                "created_on":data["created_on"]
            }
            serializer = CreateCommunitySerializer(data=payload)
            if serializer.is_valid():
                response = self.create_group(payload["creator_id"], payload["name"], payload["created_on"])
                return response
            new_error = {field_name:field_errors[0] for field_name, field_errors in serializer.errors.items()}
            return Response({"errors":new_error}, status=status.HTTP_400_BAD_REQUEST)
        
        elif data["type"] == "set_admin":
            payload={
                "community_id":data["community_id"],
                "member_id":data["member_id"],
                "setter_id":data["setter_id"]
            }
            serializer = CommunitySetAdminSerializer(data=payload)
            if serializer.is_valid():
                response = self.set_admin(payload["member_id"],payload["community_id"], payload["setter_id"])
                return response
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        elif data["type"] == "remove_admin":
            payload={
                "community_id":data["community_id"],
                "member_id":data["member_id"],
                "remover_id":data["remover_id"]
            }
            serializer = CommunityRemoveAdminSerializer(data=payload)
            if serializer.is_valid():
                response = self.remove_admin(payload["member_id"],payload["community_id"],data["remover_id"])
                return response
            return Response(serializer.errors, status=400)
        elif data["type"] == "add_member":
            payload={
                "community_id":data["community_id"],
                "member_id":data["member_id"],
                "admin_id":data["admin_id"]
            }
            serializer = CommunityAddMemberSerializer(data=payload)
            if serializer.is_valid():
                response = self.add_member_to_group(payload["member_id"],payload["community_id"], payload["admin_id"])
                return response
            return Response(serializer.errors, status=400)
        elif data["type"] == "delete_member":
            payload={
                "community_id":data["community_id"],
                "member_id":data["member_id"],
                "deleter_id":data["deleter_id"]
            }
            serializer = CommunityRemoveMemberSerializer(data=payload)
            if serializer.is_valid():
                response = self.remove_member_from_group(payload["member_id"],payload["community_id"],data["deleter_id"])
                return response
            return Response(serializer.errors, status=400)

        elif data["type"] == "send_message":
            payload={
                "community_id":data["community_id"],
                "message":data["message"],
                "sender_id":data["sender_id"],
                "sent_on":data["sent_on"]
            }
            serializer = CommunitySendMessageSerializer(data=payload)
            if serializer.is_valid():
                response = self.send_message_to_group(message=payload["message"],group_id=payload["community_id"],sender_id=data["sender_id"],sent_on=payload["sent_on"])
                return response
            return Response(serializer.errors, status=400)
        elif data["type"] == "edit_message":
            payload={
                "community_id":data["community_id"],
                "message_id":data["message_id"],
                "editor_id":data["editor_id"],
                "new_message":data["new_message"]
            }
            serializer = CommunityEditMessageSerializer(data=payload)
            if serializer.is_valid():
                response  =self.edit_message_in_group(payload["message_id"], payload["new_message"],payload["community_id"],data["editor_id"])
                return response
            return Response(serializer.errors, status=400)
        elif data["type"] == "delete_message":
            payload={
                "community_id":data["community_id"],
                "message_id":data["message_id"],
                "deleter_id":data["deleter_id"]
            }
            serializer = CommunityDeleteMessageSerializer(data=payload)
            if serializer.is_valid():
                response = self.delete_message_from_group(payload["message_id"],payload["community_id"],data["deleter_id"])
                return response
            return Response(serializer.errors, status=400)
        elif data["type"] == "view_group":
            payload={
                "community_id":data["community_id"],
                "member_id":data["member_id"]
            }
            serializer = CommunityViewedGroupSerializer(data=payload)
            if serializer.is_valid():
                response = self.view_group(data["member_id"],payload["community_id"])
                return response
            return Response(serializer.errors, status=400)
        else:
            return Response({"error":"select a valid type"},status=400)
    def get(self, request,group_id):
        if Community.objects.filter(id=group_id).exists():
            try:
                community = Community.objects.get(id=group_id)
                data={field.name: str(getattr(community, field.name)) for field in community._meta.fields}

                members=CommunityMember.objects.filter(community=community).all()
                members_dict = {f"{field.user.id}": f"{field.user}" for field in members}
                data.update({'num_of_members': f"{members.count()}", 'members': members_dict})
                return Response(data, status=200)
            except Exception as error:
                return Response(data={"isSuccess":False,"response":f"{error}"},status=400)
        return Response(data={"isSuccess":False,"response":f"Sorry the group-{group_id} doesn't exist"},status=400)

    def patch(self,request, group_id):
        data = request.data
        if Community.objects.filter(id=group_id).exists():
            community = Community.objects.get(id=group_id)
            profile=Profile.objects.get(id=data["member_id"])
            if CommunityAdmin.objects.filter(user=profile).exists():
                try:
                    community.name=data["name"]
                    community.max_members=data["max_members"]
                    community.save()
                    return Response(data={"isSuccess":True,"response":f"successfully update the community -{group_id}"}, status=200)
                except Exception as error:
                    return Response(data={"isSuccess":False,"response":f"{error}"},status=301)
            return Response(data={"isSuccess":False,"response":f"Sorry the you dont have the permission to perform this action"},status=301)
        return Response(data={"isSuccess":False,"response":f"Sorry the group-{group_id} doesn't exist"},status=400)

class PrivateMessageClass(APIView):
    def post(self, request):
        data = request.data
        payload={
            "sender_id":data["sender_id"],
            "receiver_id":data["receiver_id"],
            "details":data["details"],
            "created_date":data["created_date"]
        }
        serializer = PrivateMessageSerializer(data=payload)
        if serializer.is_valid():
            if not data["platform"]:
                payload["platform"] = settings.APPNAME
            else:
               payload["platform"] =data["platform"]
            sender = Profile.objects.get(id=payload["sender_id"])
            receiver = Profile.objects.get(id=payload["receiver_id"])
            if sender and receiver:
                try:
                    message = PrivateMessage.objects.create(details=payload["details"],sender=sender,receiver=receiver, platform=payload["platform"],created_date=payload["created_date"])
                    return Response(data={"isSuccess":True,"response":f"{sender.id} Sent Message to -{receiver.id}"}, status=200)
                except Exception as error:
                        return Response(data={"isSuccess":False,"response":f"{error}"},status=301)
            return Response(data={"isSuccess":False,"response":f"Sorry, pls check wether the users exists"},status=404)
        return Response(serializer.errors, status=400)
    
    def get(self,request,sender_id, receiver_id, created_date):
        if Profile.objects.filter(id=receiver_id).exists():
            receiver = Profile.objects.get(id=receiver_id)
            if Profile.objects.filter(id=sender_id).exists():
                sender = Profile.objects.get(id=sender_id)
                if created_date:
                    try:
                        message = PrivateMessage.objects.get(sender=sender,receiver=receiver,created_date=created_date)
                        data={field.name: str(getattr(message, field.name)) for field in message._meta.fields}
                        return Response({"isSuccess":True,"response":data}, status=200)
                    except Exception as error:
                            return Response(data={"isSuccess":False,"response":f"{error}"},status=301)
                return Response(data={"isSuccess":False,"response":f"Sorry this date doesn't exist"},status=404)
            return Response(data={"isSuccess":False,"response":f"Sorry this sender doesn't exist"},status=404)
        return Response(data={"isSuccess":False,"response":f"Sorry this receiver doesn't exist"},status=404)
        
    def patch(self,request,sender_id, receiver_id, created_date):
        data = request.data
        if Profile.objects.filter(id=receiver_id).exists():
            receiver = Profile.objects.get(id=receiver_id)
            if Profile.objects.filter(id=sender_id).exists():
                sender = Profile.objects.get(id=sender_id)
                if created_date:
                    try:
                        message = PrivateMessage.objects.get(sender=sender,receiver=receiver,created_date=created_date)
                        message.details=data["new_message"]
                        message.save()
                        
                        return Response({"isSuccess":True,"response":"Successfully updated message"}, status=200)
                    except Exception as error:
                        return Response(data={"isSuccess":False,"response":f"{error}"},status=301)
                return Response(data={"isSuccess":False,"response":f"Sorry this date doesn't exist"},status=404)
            return Response(data={"isSuccess":False,"response":f"Sorry this sender doesn't exist"},status=404)
        return Response(data={"isSuccess":False,"response":f"Sorry this receiver doesn't exist"},status=404)
    def delete(self,request,sender_id, receiver_id, created_date):
        if Profile.objects.filter(id=receiver_id).exists():
            receiver = Profile.objects.get(id=receiver_id)
            if Profile.objects.filter(id=sender_id).exists():
                sender = Profile.objects.get(id=sender_id)
                if created_date:
                    try:
                        message = PrivateMessage.objects.get(sender=sender,receiver=receiver,created_date=created_date)
                        message.delete()
                        return Response({"isSuccess":True,"response":"Successfully deleted message"}, status=200)
                    except Exception as error:
                        return Response(data={"isSuccess":False,"response":f"{error}"},status=301)
                return Response(data={"isSuccess":False,"response":f"Sorry this date doesn't exist"},status=404)
            return Response(data={"isSuccess":False,"response":f"Sorry this sender doesn't exist"},status=404)
        return Response(data={"isSuccess":False,"response":f"Sorry this receiver doesn't exist"},status=404)

class PrivateChatClass(APIView):
    def get(self,request,sender_id):
        if Profile.objects.filter(id=sender_id).exists():
            sender = Profile.objects.get(id=sender_id)
            chats = PrivateMessage.objects.filter(sender=sender)
            #print(chats)
            data= [{f"id":f"{chat.receiver.id}",f"name":f"{chat.receiver.username}",f"message":f"{chat.details}",
                    f"dtime":f"{chat.created_date}"} 
                    for chat in chats 
                    if chat.id == PrivateMessage.objects.filter(sender=sender, receiver = chat.receiver).aggregate(max_id=models.Max('id'))['max_id']]
            return Response({"isSuccess":True,"num_chats":chats.count(),"chats":data}, status=200)
        return Response(data={"isSuccess":False,"response":f"Sorry this sender doesn't exist"},status=404)
class PlatformPrivateMessageClass(APIView):
    def post(self, request):
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



