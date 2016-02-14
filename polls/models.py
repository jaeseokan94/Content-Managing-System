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


class Learn(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
