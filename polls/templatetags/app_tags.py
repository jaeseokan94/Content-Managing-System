from django import template
from polls.models import Topic

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return "Hi"

@register.inclusion_tag('sidebar.html')
def show_topics(language_name, level):
    #language = Language.objects.filter(name=language_name)
    topics = Topic.objects.all()

    return {'topics': topics}