# coding=UTF-8

from django.contrib import admin
from django.contrib.admin.models import LogEntry

from django.urls import reverse
from django.utils.html import format_html

from .models import Category, Tag, Post
from blog.adminforms import PostAdminForm

from blogsystem.base_admin import BaseOwnerAdmin
from blogsystem.custom_site import custom_site


# Register your models here.


class PostInline(admin.TabularInline):
    fields = ('title', 'desc')
    extra = 1
    model = Post


@admin.register(Category, site=custom_site)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline]

    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@admin.register(Tag, site=custom_site)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time', 'post_count')
    fields = ('name', 'status')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


class CategoryOwnerFilter(admin.SimpleListFilter):
    title = '分类过滤器'
    parameter_name = 'owner_category'

    def lookups(self, request, model_admin):
        return Category.objects.filter(owner=request.user).values_list('id', 'name')

    def queryset(self, request, queryset):
        category_id = self.value()
        if category_id:
            return queryset.filter(category_id=category_id)
        return queryset


@admin.register(Post, site=custom_site)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'id', 'title', 'category', 'status',
        'created_time', 'owner', 'operator'
    ]
    list_display_links = []

    # list_filter = ['category', ]
    list_filter = [CategoryOwnerFilter]
    search_fields = ['title', 'category__name']  # 搜索关联model的数据
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True

    exclude = ['owner']
    fieldsets = (
        ('基础配置', {
            'description': '基础配置描述',
            'fields': (
                ('title', 'category'),
                ('status',),
                'tag',
            ),
        }),
        ('内容', {
            'fields': (
                'desc',
                'content'
                # 'is_md', # 当markdown和富文本共存的时候把注释去掉
                # 'content_ck',
                # 'content_md',  # 当markdown和富文本共存的时候把注释去掉
                # 'content',    # 当markdown和富文本共存的时候把注释去掉
            ),
        }),
        # ('额外信息', {
        #     'classes': ('collapse', ),
        #     'fields': ('tag', ),
        # })
    )

    # filter_horizontal = ('tag',)
    filter_vertical = ('tag',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('cus_admin:blog_post_change', args=(obj.id,))
        )

    operator.short_description = '操作'

    class Media:
        css = {
            'all': ("https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",),
        }
        js = ('https://cdn.bootcss.com/bootstrap/4.0.0-beta.2/js/bootstrap.bundle.js',)


@admin.register(LogEntry, site=custom_site)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ['object_repr', 'object_id', 'action_flag', 'user', 'change_message']
