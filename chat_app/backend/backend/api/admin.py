from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin

from .models import Profile , PrivateMessage,Platform, Community, CommunityAdmin, CommunityMember, CommunityMessage, CommunityMessageRecipient, CommunityMessageViewer

# Register your models here.
class ProfileAdmin(admin.ModelAdmin):
    readonly_fields = ('id','password','date_joined',)  # Make the 'username' field uneditable
    fieldsets = [
        ('Details', {'fields': readonly_fields}),
        ('', {'fields': [field.name for field in Profile._meta.fields if field.name not in ('id','password','date_joined',)]})
    ]

class CommunityMessageAdmin(admin.ModelAdmin):
    readonly_fields = ('id',)  # Make the 'username' field uneditable
    fieldsets = [
        ('Details', {'fields': readonly_fields}),
        ('', {'fields': [field.name for field in CommunityMessage._meta.fields if field.name not in ('id')]})
    ]

admin.site.register(Profile, ProfileAdmin)
admin.site.register(PrivateMessage)
admin.site.register(Community)
admin.site.register(CommunityAdmin)
admin.site.register(CommunityMember)
admin.site.register(CommunityMessage,CommunityMessageAdmin)
admin.site.register(CommunityMessageRecipient)
admin.site.register(CommunityMessageViewer)
admin.site.register(Platform)


admin.site.unregister(Group)