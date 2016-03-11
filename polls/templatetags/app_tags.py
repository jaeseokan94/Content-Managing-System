from django import template
from polls.models import LanguageTopic, Language

register = template.Library()

@register.simple_tag
def current_time(format_string):
    return "Hi"

@register.inclusion_tag('sidebar.html')
def show_topics(url):
    languages = Language.objects.all()

    found_language = False

    lang_id = -1

    for language in languages:
        if language.name in url:
            lang_id = language.id
            found_language = True

    if found_language:
        language = Language.objects.get(id=lang_id)

    topics = []
    if lang_id != -1:
        topics = LanguageTopic.objects.filter(language=lang_id)

    context = {
        'topics': topics,
        'language': language,
        'found_language': found_language,
    }

    return context