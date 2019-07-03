# coding=UTF-8
import xadmin
from django.contrib import admin
from django.contrib.admin.models import LogEntry

from django.urls import reverse
from django.utils.html import format_html

from xadmin.layout import Row, Fieldset
from xadmin.filters import manager, RelatedFieldListFilter

from .models import Category, Tag, Post
from blog.adminforms import PostAdminForm

from blogsystem.base_admin import BaseOwnerAdmin
from blogsystem.custom_site import custom_site


# Register your models here.


class PostInline(admin.TabularInline):
    fields = ('title', 'desc')
    extra = 1
    model = Post


@xadmin.sites.register(Category)
class CategoryAdmin(BaseOwnerAdmin):
    inlines = [PostInline]

    list_display = ('name', 'status', 'is_nav', 'created_time', 'post_count')
    fields = ('name', 'status', 'is_nav')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


@xadmin.sites.register(Tag)
class TagAdmin(BaseOwnerAdmin):
    list_display = ('name', 'status', 'created_time', 'post_count')
    fields = ('name', 'status')

    def post_count(self, obj):
        return obj.post_set.count()

    post_count.short_description = '文章数量'


# class CategoryOwnerFilter(admin.SimpleListFilter):
    # title = '分类过滤器'
    # parameter_name = 'owner_category'
    #
    # def lookups(self, request, model_admin):
    #     return Category.objects.filter(owner=request.user).values_list('id', 'name')
    #
    # def queryset(self, request, queryset):
    #     category_id = self.value()
    #     if category_id:
    #         return queryset.filter(category_id=category_id)
    #     return queryset


class CategoryOwnerFilter(RelatedFieldListFilter):
    @classmethod
    def test(cls, field, request, params, model, admin_view, field_path):
        return field.name == 'category'

    def __init__(self, field, request, params, model, model_admin, field_path):
        super().__init__(field, request, params, model, model_admin, field_path)
        self.lookup_choices = Category.objects.filter(owner=request.uesr).values_list('id', 'name')


manager.register(CategoryOwnerFilter, take_priority=True)


@xadmin.sites.register(Post)
class PostAdmin(BaseOwnerAdmin):
    form = PostAdminForm
    list_display = [
        'id', 'title', 'category', 'status',
        'created_time', 'owner', 'operator'
    ]
    list_display_links = []

    # list_filter = ['category', ]
    list_filter = ['category']
    search_fields = ['title', 'category__name']  # 搜索关联model的数据
    save_on_top = True

    actions_on_top = True
    actions_on_bottom = True

    exclude = ['owner']

    form_layout = (
        Fieldset(
            '基础信息',
            Row('title', 'category'),
            'status',
            'tag'
        ),
        Fieldset(
            '内容信息',
            'desc',
            'content'
        )
    )
    # filter_horizontal = ('tag',)
    filter_vertical = ('tag',)

    def operator(self, obj):
        return format_html(
            '<a href="{}">编辑</a>',
            reverse('xadmin:blog_post_change', args=(obj.id,))
            # reverse(self.model_admin_url('change', obj.id))
        )

    operator.short_description = '操作'
