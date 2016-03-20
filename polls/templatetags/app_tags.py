from django import template
from polls.models import LanguageTopic, Language, LevelLanguage
import re

register = template.Library()

#TODO remove this tag
@register.simple_tag
def current_time(format_string):
    return "Hi"

@register.inclusion_tag('sidebar.html')
def show_topics(url):
    '''
        Tag for creating topics according to language and level
    '''
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
    '''
    if lang_id != -1:
        topics = LanguageTopic.objects.filter(language=lang_id)
    '''

    levelLangs = []

    if lang_id != -1:
        levelLangs = LevelLanguage.objects.filter(language=lang_id)

    context = {
        'topics': topics,
        'language': language,
        'levelLangs': levelLangs,
        'found_language': found_language,
    }

    return context