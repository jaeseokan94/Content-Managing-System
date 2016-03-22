from django import template

register = template.Library()

@register.filter(name="get_at_index")
def get_at_index(list, index):
    return list[index]

@register.filter(name="get_word")
def get_word(list, word):
    for item in list:
        if item.word == word:
            return item.word_in_language
    return "None"

#TODO this
@register.filter(name="get_1_to_31")
def get_1_to_31(list):
    for item in list:
        if item.word == word:
            return item.word_in_language
    return "None"

@register.filter(name="filter_vocabulary")
def filter_vocabulary(subtopics):
    return subtopics.exclude(subtopic_name="Vocabulary")

@register.filter(name="filter_original_dialect")
def filter_original_dialect(dialects, original):
    return dialects.exclude(name=original.name)