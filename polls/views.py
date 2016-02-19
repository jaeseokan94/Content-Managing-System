from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from polls.models import Language
from polls.serializers import LanguageSerializer
from polls.serializers import SituationalVideoSerializer
from polls.serializers import SituationalVideo

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

#from tutorial 3 for language_list()
from django.http import HttpResponse
from django.template import loader

from .models import Choice, Question, Language, Topic


class JSONResponse(HttpResponse):
    """
    An HttpResponse that renders its content into JSON.
    """
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@csrf_exempt
def snippet_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        language = Language.objects.all()
        serializer = LanguageSerializer(language, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = LanguageSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

@csrf_exempt
def snippet_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        language = Language.objects.get(pk=pk)
    except Language.DoesNotExist:
        return HttpResponse(status=404)

    if request.method == 'GET':
        serializer = LanguageSerializer(language)
        return JSONResponse(serializer.data)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = LanguageSerializer(language, data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data)
        return JSONResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        language.delete()
        return HttpResponse(status=204)



class IndexView(generic.ListView):
	template_name = 'polls/index.html'
	context_object_name = 'latest_question_list'

	def get_queryset(self):
		"""Return the last five published questions."""
		return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
	model = Question
	template_name = 'polls/detail.html'
	
	def get_queryset(self):
		"""
		Excludes any questions that aren't published yet.
		"""
		return Question.objects.filter(pub_date__lte=timezone.now())


class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'


def vote(request, question_id):
	question = get_object_or_404(Question, pk=question_id)
	try:
		selected_choice = question.choice_set.get(pk=request.POST['choice'])
	except (KeyError, Choice.DoesNotExist):
		# Redisplay the question voting form.
		return render(request, 'polls/detail.html', {
			'question': question,
			'error_message': "You didn't select a choice.",
		})
	else:
		selected_choice.votes += 1
		selected_choice.save()
		# Always return an HttpResponseRedirect after successfully dealing
		# with POST data. This prevents data from being posted twice if a
		# user hits the Back button.
		return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


def language_list(request):
	language_list = Language.objects.all()
	context = {'language_list': language_list,}
	return render(request, 'polls/languagelist.html', context)


def language_detail(request, language_name):
	language = get_object_or_404(Language, name=language_name)
	return render(request, 'polls/languagedetail.html', {'language': language})


@csrf_exempt
def situational_video_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        video = SituationalVideo.objects.all()
        serializer = SituationalVideoSerializer(video, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SituationalVideoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializer.errors, status=400)

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

