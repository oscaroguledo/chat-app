from rest_framework import serializers
import json

# profile serializers__________________________________________________________________________
class ProfileSerializer(serializers.Serializer):

    email = serializers.EmailField(allow_null=False, allow_blank=False)
    country = serializers.CharField(allow_null=False, allow_blank=False)
    phone = serializers.CharField(allow_null=False, allow_blank=False)
    username = serializers.CharField(allow_null=False, allow_blank=False)
    first_name = serializers.CharField(allow_null=False, allow_blank=False)
    last_name = serializers.CharField(allow_null=False, allow_blank=False)
