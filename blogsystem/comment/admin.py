# coding=UTF-8
from django.contrib import admin

from .models import Comment

from blogsystem.base_admin import BaseOwnerAdmin
from blogsystem.custom_site import custom_site


# Register your models here.
@admin.register(Comment, site=custom_site)
class CommentAdmin(BaseOwnerAdmin):
    list_display = ('target', 'nickname', 'content', 'website', 'created_time')
