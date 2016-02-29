from django import forms

from .models import Language, LanguageTopic, SituationalVideo

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = [
            "name",
            "name_in_language",
        ]


class LanguageTopicForm(forms.ModelForm):
    class Meta:
        model = LanguageTopic
        fields = [
            "topic",
            "language",
            "topic_name_in_language",
        ]

class SituationalVideoForm(forms.ModelForm):
    class Meta:
        model = SituationalVideo
        fields = [
            "language_topic",
            "situation_description",
            "situation_description_in_language",
            "video_with_transcript",
            "video_without_transcript",
        ]