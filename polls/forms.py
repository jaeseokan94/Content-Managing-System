from django import forms

from .models import (
    Language, LanguageTopic, SituationalVideo, LanguageSubtopic, Exercise, ExerciseQuestion,
    ExerciseVocabularyQuestion, ResourceItem, ResourceItemPicture, Topic, Dialect, Resource,
    LevelLanguage, Level, Glossary, ResourceDialectItem
)

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
            "topic_name_in_language",
        ]

class SituationalVideoForm(forms.ModelForm):
    class Meta:
        model = SituationalVideo
        fields = [
            "situation_description",
            "situation_description_in_language",
            "video_with_transcript",
            "video_without_transcript",
        ]

class ListeningComprehensionForm(forms.ModelForm):
    class Meta:
        model = SituationalVideo
        fields = [
            "choice_1",
            "choice_2",
            "choice_3",
            "choice_4",
            "choice_5",
            "choice_6",
            "correct_answers",
        ]


class LanguageSubtopicForm(forms.ModelForm):
    class Meta:
        model = LanguageSubtopic
        fields = [
            "subtopic_name",
            "subtopic_name_in_language",
            "grammar_video_file",
        ]

class VocabularyForm(forms.ModelForm):
    class Meta:
        model = LanguageSubtopic
        fields = [
            "subtopic_name_in_language",
            "grammar_video_file",
        ]

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = Exercise
        fields = [
            "exercise_name",
        ]

class ExerciseQuestionForm(forms.ModelForm):
    class Meta:
        model = ExerciseQuestion
        fields = [
            "question_text",
            "choice_1",
            "choice_2",
            "choice_3",
            "choice_4",
            "choice_5",
            "choice_6",
            "correct_answer",
        ]

class ExerciseQuestionMultipleChoiceForm(forms.ModelForm):
    class Meta:
        model = ExerciseQuestion
        fields = [
            "question_type",
            "question_text",
            "choice_1",
            "choice_2",
            "choice_3",
            "choice_4",
            "choice_5",
            "choice_6",
            "correct_answer",
        ]


class ExerciseQuestionTypeTruefalseForm(forms.ModelForm):
    class Meta:
        model = ExerciseQuestion
        fields = [
            "question_text",
            "correct_answer",
        ]


class ExerciseVocabularyQuestionForm(forms.ModelForm):
    class Meta:
        model = ExerciseVocabularyQuestion
        fields = [
            "question_text",
            "choice_1",
            "choice_2",
            "choice_3",
            "choice_4",
            "choice_5",
            "choice_6",
            "correct_answer",
        ]

class LetterResourceForm(forms.ModelForm):
    class Meta:
        model = ResourceItem
        fields = [
            "word",
            "pronounciation_guide_or_date",
            "audio_url",
        ]

class ResourceDialectItemForm(forms.ModelForm):
    class Meta:
        model = ResourceDialectItem
        fields = [
            "audio_url",
        ]

class NumberResourceForm(forms.ModelForm):
    class Meta:
        model = ResourceItem
        fields = [
            "word",
            "word_in_language",
            "audio_url",
        ]

class HolidaysResourceForm(forms.ModelForm):
    class Meta:
        model = ResourceItemPicture
        fields = [
            "phrase",
            "phrase_in_language",
            "picture_url",
            "audio_url",
        ]

class TopicForm(forms.ModelForm):
    class Meta:
        model = Topic
        fields = [
            "topic_name",
        ]

class DialectForm(forms.ModelForm):
    class Meta:
        model = Dialect
        fields = [
            "name",
            "name_in_language",
        ]

class ResourceForm(forms.ModelForm):
    class Meta:
        model = Resource
        fields = [
            "name",
            "name_in_language",
            "instructions",
            "instructions_in_language",
        ]

class LevelLanguageForm(forms.ModelForm):
    class Meta:
        model = LevelLanguage
        fields = [
            "level",
        ]

class LevelForm(forms.ModelForm):
    class Meta:
        model = Level
        fields = [
            "level",
        ]

class GlossaryForm(forms.ModelForm):
    class Meta:
        model = Glossary
        fields = [
            "word",
            "word_in_lang"
        ]