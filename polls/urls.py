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

    #API for android testing
    url(r'^temp/api/(?P<language_name>[a-zA-Z0-9]+)/(?P<level>[a-zA-Z0-9]+)/(?P<topic_name>[\w\s]+)/situationalVideo/$', views.situational_video_list_temp),
    url(r'^temp/api/(?P<language_name>[a-zA-Z0-9]+)/(?P<level>[a-zA-Z0-9]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/grammarVideo/$', views.grammar_video_list_temp),
    url(r'^temp/api/(?P<language_name>[a-zA-Z0-9]+)/(?P<level>[a-zA-Z0-9]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/exerciseQuestion/$', views.exercise_question_list_temp),
    url(r'^temp/api/(?P<language_name>[a-zA-Z0-9]+)/(?P<level>[a-zA-Z0-9]+)/(?P<topic_name>[\w\s]+)/subtopicList/$', views.subtopic_list_temp),
    url(r'^temp/api/(?P<language_name>[a-zA-Z0-9]+)/(?P<level>[a-zA-Z0-9]+)/(?P<topic_name>[\w\s]+)/listeningComprehension/$', views.listening_comprehension_temp),


    #For API
    url(r'^api/(?P<language>[a-zA-Z0-9]+)/(?P<level>[a-zA-Z0-9]+)/(?P<topic_name>[\w\s]+)/situationalVideo/$', views.situational_video_list),
    url(r'^api/(?P<language>[a-zA-Z0-9]+)/(?P<level>[a-zA-Z0-9]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/grammarVideo/$', views.grammar_video_list),
    url(r'^api/(?P<language>[a-zA-Z0-9]+)/(?P<level>[a-zA-Z0-9]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/exerciseQuestion/$', views.exercise_question_list),
    url(r'^api/(?P<language>[a-zA-Z0-9]+)/(?P<level>[a-zA-Z0-9]+)/(?P<topic_name>[\w\s]+)/subtopicList/$', views.subtopic_list),
    url(r'^api/languageList/$', views.language_list),
    url(r'^api/(?P<language_name>[a-zA-Z]+)/levelList/$', views.level_api),
    url(r'^api/(?P<language_name>[a-zA-Z0-9]+)/(?P<dialect>[a-zA-Z0-9]+)/(?P<resource_name>[a-zA-Z0-9]+)/$', views.resource_api),

    url(r'^language/list/$', views.language_list, name='language_list'),
    url(r'^language/add/$', views.language_create, name='language_create'),
    url(r'^language/(?P<language_id>[\w]+)/edit/$', views.language_update, name='language_update'),
    url(r'^language/(?P<language_id>[\w]+)/delete', views.language_delete, name='language_delete'),
    url(r'^language/(?P<language_name>[\w]+)/$', views.language_detail, name='language_detail'),



    url(r'^$', views.dashboard, name="dashboard"),

    url(r'^(?P<level>[\w]+)/$', views.level_detail, name="level_detail"),
    url(r'^(?P<level>[\w]+)/newtopic/$', views.topic_create, name="topic_create"),
    url(r'^(?P<level>[\w]+)/(?P<topic_id>[\w]+)/edit/$', views.topic_update, name="topic_update"),



    #Resources
    url(r'^(?P<language_name>[\w]+)/resources/$', views.choose_dialect, name="choose_dialect"),
    url(r'^(?P<language_name>[\w]+)/resources/newdialect/$', views.dialect_create, name="dialect_create"),
    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect_id>[0-9]+)/$', views.dialect_update, name="dialect_update"),


    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/$', views.language_resources, name="language_resources"),
    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/(?P<resource_name>[\w]+)/edit/$', views.resources_edit, name="resources_edit"),

    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/alphabet/$', views.language_resources_alphabet, name="resources_alphabet"),
    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/alphabet/(?P<resource_id>[0-9]+)/edit$', views.letter_resource_update, name="letter_resource_update"),
    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/alphabet/add/$', views.letter_resource_create, name="letter_resource_create"),

    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/numbers/$', views.language_resources_numbers, name="resources_numbers"),
    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/numbers/(?P<resource_id>[0-9]+)/edit$', views.number_resource_update, name="number_resource_update"),
    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/numbers/add/$', views.number_resource_create, name="number_resource_create"),

    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/days/$', views.resources_days, name="resources_days"),
    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/days/(?P<resource_id>[0-9]+)/edit$', views.days_resource_update, name="days_resource_update"),
    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/days/add/$', views.days_resource_create, name="days_resource_create"),

    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/holidays/$', views.resources_holidays, name="resources_holidays"),
    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/holidays/(?P<resource_id>[0-9]+)/edit$', views.holidays_resource_update, name="holidays_resource_update"),
    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/holidays/add/$', views.holidays_resource_create, name="holidays_resource_create"),

    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/seasons_and_months/$', views.resources_months, name="resources_months"),
    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/seasons_and_months/(?P<season_or_month_name>[\w]+)/edit$', views.months_resource_update, name="months_resource_update"),
    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/seasons_and_months/add/$', views.months_resource_create, name="months_resource_create"),

    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/time/$', views.resources_time, name="resources_time"),
    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/time/(?P<resource_id>[0-9]+)/edit$', views.time_resource_update, name="time_resource_update"),
    url(r'^(?P<language_name>[\w]+)/resources/(?P<dialect>[\w\s]+)/time/add/$', views.time_resource_create, name="time_resource_create"),


    url(r'^(?P<language_name>[\w]+)/(?P<level>[a-zA-Z0-9]+)/$', views.language_topic_list, name='topic_list'),
    url(r'^(?P<language_name>[\w]+)/(?P<level>[a-z]+)/newtopic/', views.language_topic_create, name="topic_create"),



    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/newsubtopic/', views.subtopic_create, name="subtopic_create"),
    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/$', views.subtopic_detail, name='subtopic_detail'),
    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/edit/$', views.subtopic_update, name='subtopic_update'),

    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/edit', views.language_topic_update, name='topic_update'),
    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/$', views.language_topic_detail, name='topic_detail'),

    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/newsituationalvideo/$', views.situational_video_create, name='situational_video_create'),
    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/situationalvideo/edit$', views.situational_video_update, name='situational_video_update'),
    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/situationalvideo/$', views.situational_video_detail, name='situational_video_detail'),

    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/(?P<sv_id>[0-9]+)/listeningComprehension', views.listening_comprehension_update, name='listening_comprehension_update'),



    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/$', views.exercise_detail, name='exercise_detail'),
    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/edit/$', views.exercise_update, name='exercise_update'),

    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/(?P<question_id>[0-9]+)/$', views.exercise_question_detail, name='exercise_question_detail'),
    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/(?P<question_id>[0-9]+)/edit/$', views.exercise_question_update, name='exercise_question_update'),

    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/newexercise/', views.exercise_create, name="exercise_create"),
    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/newquestion/', views.exercise_question_create, name="exercise_question_create"),
    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<question_id>[0-9]+)/$', views.exercise_question_detail, name='exercise_question_detail'),


    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<vocab_question_id>[0-9]+)/vocab/$', views.exercise_vocab_question_detail, name='exercise_vocab_question_detail'),
    url(r'^(?P<language_name>[\w]+)/(?P<level>[\w]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<vocab_question_id>[0-9]+)/vocab/edit/$', views.exercise_vocab_question_update, name='exercise_vocab_question_update'),



]


if not settings.DEBUG:
    urlpatterns += patterns(
'',
    (r'^static/(?P.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )  

