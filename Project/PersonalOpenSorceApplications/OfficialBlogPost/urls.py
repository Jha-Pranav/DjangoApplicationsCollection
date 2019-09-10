from django.urls import path,re_path
from .views import (AboutView,PostListView, PostDetailsView,
 PostCreateView, PostDeleteView,PostUpdateView, PostDraftView,
 add_comment_to_post, approve_comment, remove_comment, post_publish)



urlpatterns = [
    re_path(r'^$', PostListView.as_view(), name='post_list'),
    re_path(r'^about/$', AboutView.as_view(), name='about'),
    re_path(r'^post/(?P<pk>\d+)$', PostDetailsView.as_view(), name='post_detail'),
    re_path(r'^post/new/$', PostCreateView.as_view(), name='post_new'),
    re_path(r'^post/(?P<pk>\d+)/edit/$',PostUpdateView.as_view(), name='post_edit'),
    re_path(r'^post/(?P<pk>\d+)/remove/$',PostDeleteView.as_view(), name='post_remove'),
    re_path(r'^drafts/$',PostDraftView.as_view(), name='post_draft'),

    re_path(r'^post/(?P<pk>\d+)/comment/$',add_comment_to_post, name='add_comment_to_post'),
    re_path(r'^comment/(?P<pk>\d+)/approve/$',approve_comment, name='approve_comment'),
    re_path(r'^comment/(?P<pk>\d+)/remove/$',remove_comment, name='remove_comment'),
    re_path(r'^post/(?P<pk>\d+)/publish/$',post_publish, name='post_publish'),

]
