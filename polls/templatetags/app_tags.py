from django import template
from polls.models import LanguageTopic, Language, LevelLanguage, Dialect, LanguageSubtopic
import re

register = template.Library()

#TODO remove this tag
@register.simple_tag
def current_time(format_string):
    return "Hi"

@register.simple_tag
def get_vocabulary(language_subtopics):
    try:
        language_subtopics.get(subtopic_name="Vocabulary")
    except LanguageSubtopic.DoesNotExist:
        return False
    return language_subtopics.get(subtopic_name="Vocabulary")

@register.simple_tag
def get_original_dialect(dialects, original):
    try:
        dialects.filter(language_id=original).get(name=original.name)
    except Dialect.DoesNotExist:
        return False
    return dialects.filter(language_id=original).get(name=original.name)


@register.simple_tag
def has_vocabulary(language_subtopics):
    try:
        language_subtopics.get(subtopic_name="Vocabulary")
        print("asdfasdfasdfasdfa" + language_subtopics.get(subtopic_name="Vocabulary"))
        return True
    except LanguageSubtopic.DoesNotExist:
        return False
    return True

@register.simple_tag
def is_vocabulary(language_subtopic):
    if language_subtopic.subtopic_name == "Vocabulary":
        return True
    return False

@register.simple_tag
def is_main_dialect(language_name, dialect):
    if language_name == dialect.name:
        return True
    return False


@register.simple_tag
def has_three_subtopics(language_subtopics):
    '''
        Checks if topic has more than three subtopics that are not Vocabulary
        :param topic: Topic
        :param language_subtopics: QuerySet of language_subtopics
        :return: True or False
    '''

    if len(language_subtopics.exclude(subtopic_name="Vocabulary")) > 2:
        return True
    return False

@register.inclusion_tag('sidebar.html')
def show_topics(url):
    '''
        Tag for creating topics according to language and level
    '''
    languages = Language.objects.all()

    found_language = False

    lang_id = -1

    language = Language.objects.none()

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
    dialects = []

    #if language exists
    if lang_id != -1:
        levelLangs = LevelLanguage.objects.filter(language=lang_id)
        dialects = Dialect.objects.filter(language_id=lang_id)


    context = {
        'topics': topics,
        'language': language,
        'levelLangs': levelLangs,
        'dialects': dialects,
        'found_language': found_language,
    }

    return context