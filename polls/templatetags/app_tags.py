from django import template
from polls.models import LanguageTopic, Language

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return "Hi"

@register.inclusion_tag('sidebar.html')
def show_topics(url):
    languages = Language.objects.all()

    print(url)

    lang_id = -1

    for language in languages:
        if language.name in url:
            lang_id = language.id
            print(language.name + "AAAAAAAA")

    topics = []
    if lang_id != -1:
        topics = LanguageTopic.objects.filter(language=lang_id)


    return {'topics': topics}