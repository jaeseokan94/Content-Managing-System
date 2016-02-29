from django.conf.urls import patterns, url, include
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from django.conf import settings
from django.contrib import admin





from . import views


admin.autodiscover()

app_name='polls'
urlpatterns = [
	url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/edit', views.topic_update, name='topic_update'),

    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/$', views.topic_detail, name='topic_detail'),

    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/situationalvideo/$', views.situational_video_detail, name='situational_video_detail'),


    url(r'^language/list$', views.language_list, name='language_list'),
    url(r'^language/add/$', views.language_create, name='language_create'),
    url(r'^(?P<language_name>[\w]+)/edit/$', views.language_update, name='language_update'),
    url(r'^(?P<language_name>[\w]+)/delete', views.language_delete, name='language_delete'),
    #url(r'^(?P<language_name>[\w]+)', views.language_detail, name='language_detail'),



    url(r'^topics/$', views.topic_list, name='topic_list'),
    #url(r'^list/$', 'list', name='list'),
    url(r'^(?P<language>[a-zA-Z0-9]+)/(?P<level>[a-zA-Z0-9]+)/(?P<topic_name>[\w\s]+)/situationalVideo/$', views.situational_video_list),
    url(r'^(?P<language>[a-zA-Z0-9]+)/(?P<level>[a-zA-Z0-9]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/grammarVideo/$', views.grammar_video_list),
    url(r'^(?P<language>[a-zA-Z0-9]+)/(?P<level>[a-zA-Z0-9]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/exerciseQuestion/$', views.exercise_question_list),


]


if not settings.DEBUG:
    urlpatterns += patterns(
'',
    (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )  

