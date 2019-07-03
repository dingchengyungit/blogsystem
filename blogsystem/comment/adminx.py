# coding=UTF-8
import xadmin
from django.contrib import admin

from .models import Comment

from blogsystem.base_admin import BaseOwnerAdmin
from blogsystem.custom_site import custom_site


# Register your models here.
@xadmin.sites.register(Comment)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
