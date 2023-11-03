from django.urls import path
from .views import *

urlpatterns = [
    # serverstatus-------------------------------------------
    path("", serverStatus.as_view()),
    # accounts management-------------------------------------------
    #path("send_message/", send_message.as_view()),
    ]