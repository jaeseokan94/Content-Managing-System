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
    url(r'^temp/api/(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/situationalVideo/$', views.situational_video_list_temp),
    url(r'^temp/api/(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/grammarVideo/$', views.grammar_video_list_temp),
    url(r'^temp/api/(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/exerciseQuestion/$', views.exercise_question_list_temp),
    url(r'^temp/api/(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/subtopicList/$', views.subtopic_list_temp),
    url(r'^temp/api/(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/listeningComprehension/$', views.listening_comprehension),


    #For API
    url(r'^api/(?P<language>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/situationalVideo/$', views.situational_video_list, name="api_get_situational_video"),
    url(r'^api/(?P<language>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/grammarVideo/$', views.grammar_video_list, name="api_get_grammar_video"),
    url(r'^api/(?P<language>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/exercisesList/$', views.exercise_list, name="api_get_exercises_list"),
    url(r'^api/(?P<language>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/exerciseQuestions/$', views.exercise_question_list, name="api_get_questions"),
    url(r'^api/(?P<language>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/vocabExercisesQuestions/$', views.exercise_vocab_question_list, name="api_get_vocab_questions"),
    url(r'^api/(?P<language>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/subtopicList/$', views.subtopic_list, name="api_get_subtopic_list"),
    url(r'^api/languageList/$', views.language_list_show, name="api_get_language_list"),
    url(r'^api/(?P<language_name>[a-zA-Z]+)/levelList/$', views.level_api, name="api_get_level_list"),
    url(r'^api/(?P<level>[a-zA-Z]+)/topicList/$', views.topic_list, name="api_get_topic_list"),
    url(r'^api/(?P<language>[\w\s]+)/dialectList/$', views.dialect_list, name="api_get_dialect_list"),
    url(r'^api/(?P<language_name>[\w\s]+)/(?P<dialect>[\w\s]+)/(?P<resource_name>[\w\s]+)/$', views.resource_api, name="api_get_resource"),
    url(r'^api/(?P<language>[\w\s]+)/glossaryList/$', views.glossary_api, name="api_get_glossary"),
    url(r'^api/(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/listeningComprehension/$', views.listening_comprehension, name="api_get_listening_comp"),




    url(r'^language/list/$', views.language_list, name='language_list'),
    url(r'^language/new/$', views.language_create, name='language_create'),
    url(r'^language/(?P<language_id>[\w\s]+)/edit/$', views.language_update, name='language_update'),
    url(r'^language/(?P<language_id>[\w\s]+)/delete', views.language_delete, name='language_delete'),
    url(r'^language/(?P<language_name>[\w\s]+)/$', views.language_detail, name='language_detail'),



    url(r'^$', views.dashboard, name="dashboard"),

    url(r'^(?P<language_name>[\w\s]+)/newLevel/$', views.level_language_create, name="level_language_create"),
    url(r'^(?P<level_id>[0-9]+)/edit/$', views.level_update, name="level_update"),
    url(r'^(?P<level_id>[0-9]+)/delete/$', views.level_delete, name="level_delete"),
    url(r'^level/new/$', views.level_create, name="level_create"),
    url(r'^(?P<level>[\w\s]+)/$', views.level_detail, name="level_detail"),
    url(r'^(?P<level>[\w\s]+)/newtopic/$', views.topic_create, name="topic_create"),
    url(r'^(?P<level>[\w\s]+)/(?P<topic_id>[\w\s]+)/edit/$', views.topic_update, name="topic_update"),



    #Resources
    url(r'^(?P<language_name>[\w\s]+)/resources/$', views.choose_dialect, name="choose_dialect"),
    url(r'^(?P<language_name>[\w\s]+)/resources/newdialect/$', views.dialect_create, name="dialect_create"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect_id>[0-9]+)/edit/$', views.dialect_update, name="dialect_update"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect_id>[0-9]+)/delete/$', views.dialect_delete, name="dialect_delete"),


    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/$', views.language_resources, name="language_resources"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/(?P<resource_name>[\w\s]+)/edit/$', views.resources_edit, name="resources_edit"),

    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/alphabet/$', views.language_resources_alphabet, name="resources_alphabet"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/alphabet/(?P<resource_id>[0-9]+)/edit$', views.letter_resource_update, name="letter_resource_update"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/alphabet/add/$', views.letter_resource_create, name="letter_resource_create"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/alphabet/(?P<resource_id>[0-9]+)/delete$', views.letter_resource_delete, name="letter_resource_delete"),

    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/numbers/$', views.language_resources_numbers, name="resources_numbers"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/numbers/1-31/(?P<number_name>[\w\s]+)/edit$', views.number_resource_update_1_to_31, name="number_resource_update_1_to_31"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/numbers/(?P<resource_id>[0-9]+)/edit$', views.number_resource_update, name="number_resource_update"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/numbers/add/$', views.number_resource_create, name="number_resource_create"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/numbers/(?P<resource_id>[0-9]+)/delete$', views.number_resource_delete, name="number_resource_delete"),

    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/days/$', views.resources_days, name="resources_days"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/days/(?P<day_name>[\w\s]+)/edit$', views.days_resource_update, name="days_resource_update"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/days/add/$', views.days_resource_create, name="days_resource_create"),

    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/holidays/$', views.resources_holidays, name="resources_holidays"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/holidays/(?P<resource_id>[0-9]+)/edit$', views.holidays_resource_update, name="holidays_resource_update"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/holidays/add/$', views.holidays_resource_create, name="holidays_resource_create"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/holidays/(?P<resource_id>[0-9]+)/delete$', views.holidays_resource_delete, name="holidays_resource_delete"),

    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/seasons_and_months/$', views.resources_months, name="resources_months"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/seasons_and_months/(?P<season_or_month_name>[\w\s]+)/edit$', views.months_resource_update, name="months_resource_update"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/seasons_and_months/add/$', views.months_resource_create, name="months_resource_create"),

    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/time/$', views.resources_time, name="resources_time"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/time/(?P<resource_id>[0-9]+)/edit$', views.time_resource_update, name="time_resource_update"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/time/add/$', views.time_resource_create, name="time_resource_create"),
    url(r'^(?P<language_name>[\w\s]+)/resources/(?P<dialect>[\w\s]+)/time/(?P<resource_id>[0-9]+)/delete$', views.time_resource_delete, name="time_resource_delete"),

    url(r'^(?P<language_name>[\w\s]+)/glossary/$', views.glossary_detail, name="glossary_detail"),
    url(r'^(?P<language_name>[\w\s]+)/glossary/(?P<glossary_id>[0-9]+)/delete/$', views.glossary_delete, name="glossary_delete"),
    url(r'^(?P<language_name>[\w\s]+)/glossary/(?P<glossary_id>[0-9]+)/edit/$', views.glossary_update, name="glossary_update"),
    url(r'^(?P<language_name>[\w\s]+)/glossary/add/$', views.glossary_create, name="glossary_create"),


    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/$', views.language_topic_list, name='topic_list'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[a-z]+)/newtopic/', views.language_topic_create, name="topic_create"),

    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/newsituationalvideo/$', views.situational_video_create, name='situational_video_create'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/situationalvideo/edit$', views.situational_video_update, name='situational_video_update'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/situationalvideo/$', views.situational_video_detail, name='situational_video_detail'),

    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/newVocabulary/', views.vocabulary_subtopic_create, name="vocabulary_subtopic_create"),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/newsubtopic/', views.subtopic_create, name="subtopic_create"),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_id>[0-9]+)/delete/', views.language_subtopic_delete, name="language_subtopic_delete"),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/$', views.subtopic_detail, name='subtopic_detail'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/edit/$', views.subtopic_update, name='subtopic_update'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/editVocab/$', views.subtopic_vocabulary_update, name='subtopic_vocabulary_update'),

    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/edit', views.language_topic_update, name='topic_update'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/$', views.language_topic_detail, name='topic_detail'),

    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<sv_id>[0-9]+)/listeningComprehension', views.listening_comprehension_update, name='listening_comprehension_update'),


    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/vocab/$', views.vocab_exercise_detail, name='vocab_exercise_detail'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/$', views.exercise_detail, name='exercise_detail'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/edit/$', views.exercise_update, name='exercise_update'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/delete/$', views.exercise_delete, name='exercise_delete'),


    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/(?P<question_id>[0-9]+)/$', views.exercise_question_detail, name='exercise_question_detail'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/(?P<question_id>[0-9]+)/edit/$', views.exercise_question_update, name='exercise_question_update'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/(?P<question_id>[0-9]+)/mc/delete/$', views.exercise_question_delete, name='exercise_question_delete'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/(?P<question_id>[0-9]+)/type/delete/$', views.exercise_question_type_update, name='exercise_question_type_update'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/(?P<question_id>[0-9]+)/truefalse/delete/$', views.exercise_question_truefalse_update, name='exercise_question_truefalse_update'),


    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/newexercise/', views.exercise_create, name="exercise_create"),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/newquestion/', views.exercise_question_create, name="exercise_question_create"),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/newquestiontype/', views.exercise_question_type_create, name="exercise_question_type_create"),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<exercise_id>[0-9]+)/newquestiontruefalse/', views.exercise_question_truefalse_create, name="exercise_question_truefalse_create"),

    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<question_id>[0-9]+)/$', views.exercise_question_detail, name='exercise_question_detail'),


    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<vocab_question_id>[0-9]+)/vocab/$', views.exercise_vocab_question_detail, name='exercise_vocab_question_detail'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/vocab/new/$', views.exercise_vocab_question_create, name='exercise_vocab_question_create'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<vocab_question_id>[0-9]+)/vocab/edit/$', views.exercise_vocab_question_update, name='exercise_vocab_question_update'),
    url(r'^(?P<language_name>[\w\s]+)/(?P<level>[\w\s]+)/(?P<topic_name>[\w\s]+)/(?P<subtopic_name>[\w\s]+)/(?P<vocab_question_id>[0-9]+)/vocab/delete/$', views.exercise_vocab_question_delete, name='exercise_vocab_question_delete'),



]


if not settings.DEBUG:
    urlpatterns += patterns(
'',
    (r'^static/', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
    )  

