import datetime

from django.db import models
from django.utils import timezone


# fs = FileSystemStorage(location='/media/videos')

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text

    def was_published_recently(self):
        return self.pub_date <= timezone.now() - datetime.timedelta(days=1)


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text


class Language(models.Model):
    name = models.CharField(max_length=200)
    name2 = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Topic(models.Model):
    language = models.ForeignKey(Language, on_delete=models.CASCADE, blank=True)
    topic_name = models.CharField(max_length=200)

    def __str__(self):
        return self.topic_name


class SituationalVideo(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    situation_description = models.CharField(max_length=200)

    # video_file = models.FileField(storage=fs, blank=True)

    def __str__(self):
        return self.situation_description


class LectureVideo(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    lecture_topic = models.CharField(max_length=200)
    video_url = models.CharField(max_length=200)

    def __str__(self):
        return self.lecture_topic


class Exercise(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE, null=True)
    question_type = models.CharField(max_length=200)
    question_text = models.CharField(max_length=200)
    choice_answers = models.CharField(max_length=200)
    correct_answer = models.CharField(max_length=200)

    def __str__(self):
        return self.question_text

class Dialect(models.Model):
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    name_in_language = models.CharField(max_length=200)

class Resource(models.Model):
    dialect_id = models.ForeignKey(Dialect, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    name_in_language = models.CharField(max_length=200)
    instructions = models.CharField(max_length=200)
    instructions_in_language = models.CharField(max_length=200)

class ResourceItem(models.Model):
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    word = models.CharField(max_length=200)
    word_in_language = models.CharField(max_length=200)
    pronounciation_guide_or_date = models.CharField(max_length=200)
    audio_url = models.FileField(null=True, blank=True)

class ResourceItemPicture(models.Model):
    resource_id = models.ForeignKey(Resource, on_delete=models.CASCADE)
    phrase = models.CharField(max_length=200)
    phrase_in_language = models.CharField(max_length=200)
    picture_url = models.FileField(null=True, blank=True)
    audio_url = models.FileField(null=True, blank=True)