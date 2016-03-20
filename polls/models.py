import datetime

from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
from django.core.exceptions import ValidationError
import os

RESOURCES = (
    ('Alphabet', 'Alphabet'),
    ('Numbers', 'Numbers'),
    ('Days', 'Days of the Week'),
    ('Holidays', 'Holidays'),
    ('Months', 'Seasons and Months'),
    ('Time', 'Time'),
)
LEVEL = (
    ('b', 'Beginner'),
    ('i', 'Intermediate'),
)

CHOICES = [
    ("1", "1"),
    ("2", "2"),
    ("3", "3"),
    ("4", "4"),
    ("5", "5"),
    ("6", "6")
]

QUESTION_TYPE = [
    ("ty", "Typing"),
    ("tf", "True or False"),
    ("dd", "Drag and Drop"),
    ("mc", "Multiple Choice"),
]


def validate_movie_extension(value):
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.mp4']
        if not ext in valid_extensions:
            raise ValidationError(u'File not supported! Only .mp4 is allowed.')

def validate_audio_extension(value):
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.mp3']
        if not ext in valid_extensions:
            raise ValidationError(u'File not supported! Only .mp3 is allowed.')

def validate_picture_extension(value):
        ext = os.path.splitext(value.name)[1]
        valid_extensions = ['.jpeg', '.jpg', '.png']
        if not ext in valid_extensions:
            raise ValidationError(u'File not supported! Only .mp3 is allowed.')

class Language(models.Model):
    name = models.CharField(max_length=200)
    name_in_language = models.CharField(max_length=200)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("polls:language_detail", kwargs={"language_name": self.name})

    def get_absolute_url_create(self):
        return reverse("polls:dashboard", kwargs={})


class Dialect(models.Model):
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    name_in_language = models.CharField(max_length=200)

    '''
        name must be unique for urls to work
    '''

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("polls:choose_dialect", kwargs={"language_name": self.language_id.name})

class Level(models.Model):
    level = models.CharField(max_length=200)

    def __str__(self):
        return self.level

class LevelLanguage(models.Model):
    level = models.ForeignKey(Level, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)

    def __str__(self):
        return self.level.level

class Topic(models.Model):
    topic_name = models.CharField(max_length=200)
    level = models.ForeignKey(LevelLanguage, on_delete=models.CASCADE)

    def __str__(self):
        return self.topic_name

    def get_absolute_url(self):
        return reverse("polls:level_detail", kwargs={"level": self.level})




class LanguageTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    topic_name_in_language = models.CharField(max_length=200, blank=True)
 
    def __str__(self):
        return self.topic_name_in_language

    def get_absolute_url(self):
        return reverse("polls:topic_detail", kwargs={"language_name": self.language.name, "level": self.topic.level, "topic_name": self.topic.topic_name})

    def get_absolute_url_create(self):
        return reverse("polls:topic_list", kwargs={"language_name": self.language.name, "level": self.topic.level})

class SituationalVideo(models.Model):
    language_topic = models.ForeignKey(LanguageTopic, on_delete=models.CASCADE, null=True)
    situation_description = models.CharField(max_length=200)
    situation_description_in_language = models.CharField(max_length=200, blank=True)
    video_with_transcript = models.FileField(null=True, blank=True, validators=[validate_movie_extension])
    video_without_transcript =  models.FileField(null=True, blank=True, validators=[validate_movie_extension])
    question_text = models.CharField(max_length=200)
    choice_1 = models.CharField(max_length=200, blank=True)
    choice_2 = models.CharField(max_length=200, blank=True)
    choice_3 = models.CharField(max_length=200, blank=True)
    choice_4 = models.CharField(max_length=200, blank=True)
    choice_5 = models.CharField(max_length=200, blank=True)
    choice_6 = models.CharField(max_length=200, blank=True)
    correct_answers = models.CharField(max_length=200)

    def __str__(self):
        return self.situation_description

    def get_absolute_url(self):
        return reverse("polls:topic_detail", kwargs={"language_name": self.language_topic.language.name, "level": self.language_topic.topic.level, "topic_name": self.language_topic.topic.topic_name})



class LanguageSubtopic(models.Model):
    language_topic = models.ForeignKey(LanguageTopic, on_delete=models.CASCADE, null=True)
    subtopic_name = models.CharField(max_length=200, null=True)
    subtopic_name_in_language = models.CharField(max_length=200, null=True)
    grammar_video_file = models.FileField(null=True, blank=True, validators=[validate_movie_extension])

    def __str__(self):
        return self.language_topic. topic_name_in_language + "|" + self.subtopic_name

    def get_absolute_url(self):
        return reverse("polls:subtopic_detail", kwargs={"language_name": self.language_topic.language.name, "level": self.language_topic.topic.level, "topic_name": self.language_topic.topic.topic_name, "subtopic_name": self.subtopic_name})

class Exercise(models.Model):
    exercise_name = models.CharField(max_length=200, null=True)
    language_subtopic = models.ForeignKey(LanguageSubtopic, on_delete=models.CASCADE, null=True)
    instructions = models.CharField(max_length=500, null=True)
    instructions_in_language = models.CharField(max_length=500, null=True)
    question_type = models.CharField(max_length=3, choices=QUESTION_TYPE, default=QUESTION_TYPE[0])

    def __str__(self):
        return self.language_subtopic.subtopic_name + "|" + self.instructions

    def get_absolute_url(self):
        return reverse("polls:subtopic_detail", kwargs={"language_name": self.language_subtopic.language_topic.language.name, "level": self.language_subtopic.language_topic.topic.level, "topic_name": self.language_subtopic.language_topic.topic.topic_name, "subtopic_name": self.language_subtopic.subtopic_name})


class ExerciseQuestion(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=200)
    choice_1 = models.CharField(max_length=200, blank=True)
    choice_2 = models.CharField(max_length=200, blank=True)
    choice_3 = models.CharField(max_length=200, blank=True)
    choice_4 = models.CharField(max_length=200, blank=True)
    choice_5 = models.CharField(max_length=200, blank=True)
    choice_6 = models.CharField(max_length=200, blank=True)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.exercise.language_subtopic.subtopic_name + "|" + self.question_text

    def get_absolute_url(self):
        return reverse("polls:subtopic_detail", kwargs={"language_name": self.exercise.language_subtopic.language_topic.language.name, "level": self.exercise.language_subtopic.language_topic.topic.level, "topic_name": self.exercise.language_subtopic.language_topic.topic.topic_name, "subtopic_name": self.exercise.language_subtopic.subtopic_name})


class ExerciseVocabularyQuestion(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=200)
    choice_1 = models.FileField(null=True, blank=True, validators=[validate_picture_extension])
    choice_2 = models.FileField(null=True, blank=True, validators=[validate_picture_extension])
    choice_3 = models.FileField(null=True, blank=True, validators=[validate_picture_extension])
    choice_4 = models.FileField(null=True, blank=True, validators=[validate_picture_extension])
    choice_5 = models.FileField(null=True, blank=True, validators=[validate_picture_extension])
    choice_6 = models.FileField(null=True, blank=True, validators=[validate_picture_extension])
    correct_answer = models.CharField(max_length=1, choices=CHOICES, default=CHOICES[0])

    def __str__(self):
        return self.exercise.language_subtopic.subtopic_name + "|" + self.question_text

    def get_absolute_url(self):
        return reverse("polls:subtopic_detail", kwargs={"language_name": self.exercise.language_subtopic.language_topic.language.name, "level": self.exercise.language_subtopic.language_topic.topic.level, "topic_name": self.exercise.language_subtopic.language_topic.topic.topic_name, "subtopic_name": self.exercise.language_subtopic.subtopic_name})


class Resource(models.Model):
    dialect_id = models.ForeignKey(Dialect, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, choices=RESOURCES, default=[0][0])
    name_in_language = models.CharField(max_length=200)
    instructions = models.CharField(max_length=200)
    instructions_in_language = models.CharField(max_length=200)

    def get_absolute_url(self):
        namespace = ""
        if self.name == "Alphabet":
            namespace = "polls:resources_alphabet"
        elif self.name == "Numbers":
            namespace = "polls:resources_numbers"
        elif self.name == "Days":
            namespace = "polls:resources_days"
        elif self.name == "Months":
            namespace = "polls:resources_months"
        return reverse(namespace, kwargs={"language_name": self.dialect_id.language_id.name, "dialect": self.dialect_id.name})


    def __str__(self):
        return self.name


class ResourceItem(models.Model):
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    word_in_language = models.CharField(max_length=200, blank=True, default="")
    pronounciation_guide_or_date = models.CharField(max_length=200, blank=True)
    audio_url = models.FileField(null=True, blank=True, validators=[validate_audio_extension])

    '''
        Months resource: word only accepts {Spring,Summer,Autumn,Winter,January,}
    '''

    def __str__(self):
        return self.word

    def get_absolute_url(self):
        namespace = ""
        if self.resource_id.name == "Alphabet":
            namespace = "polls:resources_alphabet"
        elif self.resource_id.name == "Numbers":
            namespace = "polls:resources_numbers"
        elif self.resource_id.name == "Days":
            namespace = "polls:resources_days"
        elif self.resource_id.name == "Months":
            namespace = "polls:resources_months"
        return reverse(namespace, kwargs={"language_name": self.resource_id.dialect_id.language_id.name, "dialect": self.resource_id.dialect_id.name})

class ResourceItemPicture(models.Model):
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    phrase = models.CharField(max_length=200)
    phrase_in_language = models.CharField(max_length=200)
    picture_url = models.FileField(null=True, blank=True, validators=[validate_picture_extension])
    audio_url = models.FileField(null=True, blank=True, validators=[validate_audio_extension])

    def __str__(self):
        return self.phrase

    def get_absolute_url(self):
        namespace = ""
        if self.resource_id.name == "Time":
            namespace = "polls:resources_time"
        elif self.resource_id.name == "Holidays":
            namespace = "polls:resources_holidays"
        return reverse(namespace, kwargs={"language_name": self.resource_id.dialect_id.language_id.name, "dialect": self.resource_id.dialect_id.name})

