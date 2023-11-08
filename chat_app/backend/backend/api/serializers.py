from rest_framework import serializers
from .models import Profile
import json, re
from datetime import datetime

# profile serializers__________________________________________________________________________
class ProfileSerializer(serializers.Serializer):
    class Meta:
        model = Profile
        fields = "__all__" 
    def create(self, validated_data):
        # Perform object-level validation
        if Profile.objects.filter(phone=validated_data['phone']).exists():
            raise serializers.ValidationError({"Phone":"Phone number already exists."})
        if Profile.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({"Email":"Email already exists."})
        if Profile.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError({"Username":"Username already exists."})
        if len(validated_data['password']) < 8:
            raise serializers.ValidationError({"Password":"The password length must be over 8 characters"})
        if validated_data['password'].isnumeric():
            raise serializers.ValidationError({"Password":"The password cannot be only numbers"})
        if validated_data['password'].isalpha():
            raise serializers.ValidationError({"Password":"The password cannot be only letters"})


        # Save the object
        return Profile.objects.create_user(**validated_data)
    def createadminuser(self, validated_data):
        # Perform object-level validation
        if Profile.objects.filter(phone=validated_data['phone']).exists():
            raise serializers.ValidationError({"Phone":"Phone number already exists."})
        if Profile.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({"Email":"Email already exists."})
        if Profile.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError({"Username":"Username already exists."})
        if len(validated_data['password']) < 8:
            raise serializers.ValidationError({"Password":"The password length must be over 8 characters"})
        if validated_data['password'].isnumeric():
            raise serializers.ValidationError({"Password":"The password cannot be only numbers"})
        if validated_data['password'].isalpha():
            raise serializers.ValidationError({"Password":"The password cannot be only letters"})

        # Save the object
        return Profile.objects.create_adminuser(**validated_data)
    def createsuperuser(self, validated_data):
        # Perform object-level validation
        if Profile.objects.filter(phone=validated_data['phone']).exists():
            raise serializers.ValidationError({"Phone":"Phone number already exists."})
        if Profile.objects.filter(email=validated_data['email']).exists():
            raise serializers.ValidationError({"Email":"Email already exists."})
        if Profile.objects.filter(username=validated_data['username']).exists():
            raise serializers.ValidationError({"Username":"Username already exists."})
        if len(validated_data['password']) < 8:
            raise serializers.ValidationError({"Password":"The password length must be over 8 characters"})
        if validated_data['password'].isnumeric():
            raise serializers.ValidationError({"Password":"The password cannot be only numbers"})
        if validated_data['password'].isalpha():
            raise serializers.ValidationError({"Password":"The password cannot be only letters"})

        # Save the object
        return Profile.objects.create_superuser(**validated_data)
# community serializer____________________________________________________________________________
class CreateCommunitySerializer(serializers.Serializer):
    creator_id = serializers.CharField(allow_null=False, allow_blank=False)
    name = serializers.CharField(allow_null=False, allow_blank=False)
    #created_on = serializers.CharField(allow_null=False, allow_blank=False)
    
    
# set admin serializers__________________________________________________________________________
class CommunitySetAdminSerializer(serializers.Serializer):
    community_id = serializers.CharField(allow_null=False, allow_blank=False)
    member_id = serializers.CharField(allow_null=False, allow_blank=False)
    setter_id = serializers.CharField(allow_null=False, allow_blank=False)
# remove admin serializers__________________________________________________________________________
class CommunityRemoveAdminSerializer(serializers.Serializer):
    community_id = serializers.CharField(allow_null=False, allow_blank=False)
    member_id = serializers.CharField(allow_null=False, allow_blank=False)
    remover_id = serializers.CharField(allow_null=False, allow_blank=False)
# add member serializers__________________________________________________________________________
class CommunityAddMemberSerializer(serializers.Serializer):
    community_id = serializers.CharField(allow_null=False, allow_blank=False)
    member_id = serializers.CharField(allow_null=False, allow_blank=False)
# remove member serializers__________________________________________________________________________
class CommunityRemoveMemberSerializer(serializers.Serializer):
    community_id = serializers.CharField(allow_null=False, allow_blank=False)
    member_id = serializers.CharField(allow_null=False, allow_blank=False)
    deleter_id = serializers.CharField(allow_null=False, allow_blank=False)
# send message serializers__________________________________________________________________________
class CommunitySendMessageSerializer(serializers.Serializer):
    community_id = serializers.CharField(allow_null=False, allow_blank=False)
    message = serializers.CharField(allow_null=False, allow_blank=False)
    sender_id = serializers.CharField(allow_null=False, allow_blank=False)
# edit message serializers__________________________________________________________________________
class CommunityEditMessageSerializer(serializers.Serializer):
    community_id = serializers.CharField(allow_null=False, allow_blank=False)
    message_id = serializers.CharField(allow_null=False, allow_blank=False)
    editor_id = serializers.CharField(allow_null=False, allow_blank=False)
    new_message = serializers.CharField(allow_null=False, allow_blank=False)
# delete message serializers__________________________________________________________________________
class CommunityDeleteMessageSerializer(serializers.Serializer):
    community_id = serializers.CharField(allow_null=False, allow_blank=False)
    message_id = serializers.CharField(allow_null=False, allow_blank=False)
    deleter_id = serializers.CharField(allow_null=False, allow_blank=False)
# viewed group serializers__________________________________________________________________________
class CommunityViewedGroupSerializer(serializers.Serializer):
    community_id = serializers.CharField(allow_null=False, allow_blank=False)
    member_id = serializers.CharField(allow_null=False, allow_blank=False)

#---private message--------------------
class PrivateMessageSerializer(serializers.Serializer):
    details = serializers.CharField(allow_null=False, allow_blank=False)
    sender_id = serializers.CharField(allow_null=False, allow_blank=False)
    created_date = serializers.CharField(allow_null=False, allow_blank=False)
    receiver_id = serializers.CharField(allow_null=False, allow_blank=False)

