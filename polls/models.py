import datetime

from django.db import models
from django.utils import timezone


RESOURCES = (
    ('Alphabet', 'Alphabet'),
    ('Numbers', 'Numbers'),
    ('Days of the Week', 'Days of the Week'),
    ('Holidays', 'Holidays'),
    ('Seasons and Months', 'Seasons and Months'),
    ('Time', 'Time'),
)

LEVEL = (
    ('b', 'Beginner'),
    ('i', 'Intermediate'),
)


class Language(models.Model):
    name = models.CharField(max_length=200)
    name_in_language = models.CharField(max_length=200)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Topic(models.Model):
    level = models.CharField(max_length=1, choices=LEVEL, default=LEVEL[0][0])
    topic_name = models.CharField(max_length=200)

    def __str__(self):
        return self.topic_name

class LanguageTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    topic_name_in_language = models.CharField(max_length=200, blank=True)
 
    def __str__(self):
        return self.topic_name_in_language


class SituationalVideo(models.Model):
    language_topic = models.ForeignKey(LanguageTopic, on_delete=models.CASCADE, null=True)
    situation_description = models.CharField(max_length=200)
    situation_description_in_language = models.CharField(max_length=200, blank=True)
    video_with_transcript = models.FileField(null=True, blank=True)
    video_wihtout_transcript =  models.FileField(null=True, blank=True)

    def __str__(self):
        return self.situation_description

class LanguageSubtopic(models.Model):
    language_topic = models.ForeignKey(LanguageTopic, on_delete=models.CASCADE, null=True)
    subtopic_name = models.CharField(max_length=200, null=True)
    grammar_video_file = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.subtopic_name

class Exercise(models.Model):
    language_subtopic = models.ForeignKey(LanguageSubtopic, on_delete=models.CASCADE, null=True)
    instructions = models.CharField(max_length=500, null=True)

    def __str__(self):
        return self.language_subtopic.subtopic_name

class ExerciseQuestion(models.Model):
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, null=True)
    question_text = models.CharField(max_length=200)
    choice_answers = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.exercise.language_subtopic.subtopic_name + "," + self.question_text

class Dialect(models.Model):
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    name_in_language = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Resource(models.Model):
    dialect_id = models.ForeignKey(Dialect, on_delete=models.CASCADE)
    name = models.CharField(max_length=200, choices=RESOURCES, default=[0][0])
    name_in_language = models.CharField(max_length=200)
    instructions = models.CharField(max_length=200)
    instructions_in_language = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class ResourceItem(models.Model):
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    word_in_language = models.CharField(max_length=200)
    pronounciation_guide_or_date = models.CharField(max_length=200)
    audio_url = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.word

class ResourceItemPicture(models.Model):
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    phrase = models.CharField(max_length=200)
    phrase_in_language = models.CharField(max_length=200)
    picture_url = models.FileField(null=True, blank=True)
    audio_url = models.FileField(null=True, blank=True)

    def __str__(self):
        return self.phrase
