from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from polls.serializers import LanguageSerializer
from polls.serializers import SituationalVideoSerializer , GrammarVideoSerializer , ExerciseQuestionSerializer
from polls.serializers import SituationalVideo


from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

#from tutorial 3 for language_list()
from django.http import HttpResponse
from django.template import loader

from polls.models import Language, Topic, LanguageTopic, LanguageSubtopic, ExerciseQuestion, Exercise


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)


def language_list(request):
    language_list = Language.objects.all()
    context = {'language_list': language_list,}
    return render(request, 'polls/languagelist.html', context)


def language_detail(request, language_name):
    language = get_object_or_404(Language, name=language_name)
    return render(request, 'polls/languagedetail.html', {'language': language})



@csrf_exempt
def grammar_video_list(request, language, level, topic_name, subtopic_name):

    if request.method == 'GET':
        subtopic = LanguageSubtopic.objects.filter(subtopic_name=subtopic_name)
        serializer = GrammarVideoSerializer(subtopic, many=True)
        return JSONResponse(serializer.data)
'''http://127.0.0.1:8000/polls/German/beginner/Bathroom/subtopic-test/grammarVideo/'''

@csrf_exempt
def subtopic_list(request, language, level, topic_name):

      if request.method == 'GET':
        language = Language.objects.get(name=language)
        topic_list= Topic.objects.filter(topic_name=topic_name).get(level=level)
        language_topic= LanguageTopic.objects.filter(language=language.id).get(topic=topic_list.id)
        topic = LanguageSubtopic.objects.filter(language_topic=language_topic.id)
        serializer = GrammarVideoSerializer(topic, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def situational_video_list(request, language, level, topic_name):

    if request.method == 'GET':
        language = Language.objects.get(name=language)
        topic = Topic.objects.filter(topic_name=topic_name).get(level=level)
        language_topic = LanguageTopic.objects.filter(language=language.id).get(topic=topic.id)
        video = SituationalVideo.objects.filter(language_topic=language_topic.id)
        serializer = SituationalVideoSerializer(video, many=True)
        return JSONResponse(serializer.data)


@csrf_exempt
def exercise_question_list(request, language, level, topic_name, subtopic_name):

    if request.method == 'GET':
        language = Language.objects.get(name=language)
        topic = Topic.objects.filter(topic_name=topic_name).get(level=level)
        language_topic = LanguageTopic.objects.filter(topic=topic.id).get(language=language.id)

        language_subtopic = LanguageSubtopic.objects.get(subtopic_name=subtopic_name)

        exercise = Exercise.objects.get(language_subtopic=language_subtopic.id)
        question = ExerciseQuestion.objects.filter(exercise=exercise.id)
        serializer = ExerciseQuestionSerializer(question, many=True)
        return JSONResponse(serializer.data)

@csrf_exempt
def situational_video_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        situationalVideo = SituationalVideo.objects.get(pk=pk)
    except SituationalVideo.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = SituationalVideoSerializer(situationalVideo)
        return JSONResponse(serializer.data)

    elif request.method == 'DELETE':
        situationalVideo.delete()
        return HttpResponse(status=204)


def topic_list(request):
    topic_list = Topic.objects.all()
    return render(request, 'polls/topiclist.html', {'topic_list': topic_list})

