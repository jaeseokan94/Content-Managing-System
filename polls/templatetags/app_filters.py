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

