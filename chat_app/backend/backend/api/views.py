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
from heyoo import WhatsApp

# Create your views here.

# api for serverstatus begins here---------------------------
@method_decorator(csrf_exempt, name="dispatch")
class serverStatus(APIView):
    def get(self, request):
        return Response(
            {"info": "Welcome to Scar 1.0"},
            status=status.HTTP_200_OK,
        )


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
            )



