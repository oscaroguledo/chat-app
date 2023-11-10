from django.urls import path
from .views import *

urlpatterns = [
    # serverstatus-------------------------------------------
    path("", serverStatus.as_view()),
    
    # user profile--------------------------------------------
    path("create_user/",ProfilesClass.as_view()),
    path("create_superuser/",SuperAdminProfilesClass.as_view(), name='create_superuser'),
    path("create_adminuser/",AdminProfilesClass.as_view(), name='create_adminuser'),
    path("get_user/<str:email>/<str:username>/<str:phone>/",ProfilesClass.as_view()),
    path("update_user/<str:email>/",ProfilesClass.as_view()),
    path("delete_user/<str:email>/<str:username>/<str:phone>/<str:deleter_id>/",ProfilesClass.as_view()),

    # community----------------------------------------------------------------
    path("create_community/",CommunityClass.as_view()),
    path("set_community_admin/",CommunityClass.as_view()),
    path("remove_community_admin/",CommunityClass.as_view()),
    path("add_member_community/",CommunityClass.as_view()),
    path("remove_member_community/",CommunityClass.as_view()),
    path("send_message_community/",CommunityClass.as_view()),
    path("edit_message_community/",CommunityClass.as_view()),
    path("delete_message_community/",CommunityClass.as_view()),
    path("get_community/<str:group_id>/",CommunityClass.as_view()),
    path("update_community/<str:group_id>/",CommunityClass.as_view()),

    # private chat----------------------------------------------------------------
    path("send_message_private/",PrivateMessageClass.as_view()),
    path("get_message_private/<str:sender_id>/<str:receiver_id>/<str:created_date>/",PrivateMessageClass.as_view()),    
    path("update_message_private/<str:sender_id>/<str:receiver_id>/<str:created_date>/",PrivateMessageClass.as_view()),
    path("delete_message_private/<str:sender_id>/<str:receiver_id>/<str:created_date>/",PrivateMessageClass.as_view()),#-------------------------------
    path("get_chats_private/<str:sender_id>/",PrivateChatClass.as_view()),
    #path("delete_chat_private/<str:sender_id>/<str:receiver_id>/",PrivateChatClass.as_view()),
    ]