"""blogsystem URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.contrib.sitemaps import views as sitemap_views

from .autocomplete import CategoryAutocomplete, TagAutocomplete

from blog.views import (IndexView, CategoryView, TagView, PostDetailView, SearchView, AuthView, LinklistView,
                        demo, staticthml)
from blog.sitemap import PostSitemap
from blog.rss import LatestPostFeed

from comment.views import CommentView
from config.views import links
from .custom_site import custom_site

urlpatterns = [
    url(r'^category-autocomplete/$', CategoryAutocomplete.as_view(), name='category-autocomplete'),
    url(r'^tag-autocomplete/$', TagAutocomplete.as_view(), name='tag-autocomplete'),
    url(r'^rss|feed/', LatestPostFeed(), name='rss'),
    url(r'^sitemap\.xml$', sitemap_views.sitemap, {'sitemaps': {'posts': PostSitemap}}),
    url(r'^comment/$', CommentView.as_view(), name='comment'),
    url(r'^links/$', LinklistView.as_view(), name='links'),
    url(r'^author/(?P<owner_id>\d+)/$', AuthView.as_view(), name='author'),
    url(r'^search/$', SearchView.as_view(), name='search'),
    url(r'^blog/static.html$', staticthml),
    url(r'^blog/demo.html$', demo),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^category/(?P<category_id>\d+)/$', CategoryView.as_view(), name='category-list'),
    url(r'^tag/(?P<tag_id>\d+)/$', TagView.as_view(), name='tag-list'),
    url(r'^post/(?P<post_id>\d+).html$', PostDetailView.as_view(), name='post-detail'),
    url(r'^links/$', links, name='links'),
    url(r'^super_admin/', admin.site.urls, name='super-admin'),
    url(r'^admin/', custom_site.urls, name='admin')
    # path('super_admin/', admin.site.urls),
    # path('admin/', custom_site.urls),
]
