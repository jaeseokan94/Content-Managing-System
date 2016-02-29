from django.contrib import messages
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser

from polls.serializers import LanguageSerializer
from polls.serializers import SituationalVideoSerializer , GrammarVideoSerializer , ExerciseQuestionSerializer
from polls.serializers import SituationalVideo


from django.shortcuts import get_object_or_404, render, redirect
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

#from tutorial 3 for language_list()
from django.http import HttpResponse
from django.template import loader

from .models import Language, Topic, LanguageTopic, LanguageSubtopic, ExerciseQuestion, Exercise
from .forms import LanguageForm

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

@csrf_exempt
def grammar_video_list(request, language, level, topic_name, subtopic_name):

    if request.method == 'GET':
        subtopic = LanguageSubtopic.objects.filter(subtopic_name=subtopic_name)
        serializer = GrammarVideoSerializer(subtopic, many=True)
        return JSONResponse(serializer.data)
'''http://127.0.0.1:8000/polls/German/beginner/Bathroom/subtopic-test/grammarVideo/'''


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

def language_create(request):
    form = LanguageForm(request.POST or None)
    if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Successfully created")
            return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not successfully created")
    if request.method == "POST":
        print(request.POST)

    context = {
        "form": form,
    }
    return render(request, 'polls/language_form.html', context)

def language_update(request, language_name):
    instance = get_object_or_404(Language, name=language_name)
    form = LanguageForm(request.POST or None, instance=instance)
    if form.is_valid():
            instance = form.save(commit=False)
            instance.save()
            messages.success(request, "Saved")
            return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, "Not successfully saved")
    context = {
        "instance": instance,
        "form": form,
    }

    return render(request, 'polls/language_form.html', context)

def language_delete(request, language_name):
    instance = get_object_or_404(Language, name=language_name)
    instance.delete()
    messages.success(request, "Successfully deleted")
    return redirect("polls:language_list")

def language_detail(request, language_name):
    language = get_object_or_404(Language, name=language_name)
    context = {'language': language}
    return render(request, 'polls/language_detail.html', context)

def topic_detail(request, language_name, level, topic_name):
    language = Language.objects.get(name=language_name)
    topic = Topic.objects.get(topic_name=topic_name)

    languagetopic = LanguageTopic.objects.filter(topic=topic.id).get(language=language.id)

    #situational_video = SituationalVideo.objects.get(language_topic=languagetopic.id)
    language_subtopics = LanguageSubtopic.objects.filter(language_topic=languagetopic.id)

    context = {
        'language': language,
        'topic': topic,
        'languagetopic': languagetopic,
        #'situational_video': situational_video,
        'language_subtopics': language_subtopics,
    }

    return render(request, 'polls/languagetopic_detail.html', context)



