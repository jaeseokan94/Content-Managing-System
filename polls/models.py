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
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name


class Topic(models.Model):
    LEVEL = (
        ('b', 'Beginner'),
        ('i', 'Intermediate')
    )

    level = models.CharField(max_length=1, choices=LEVEL, default=LEVEL[0][0])
    topic_name = models.CharField(max_length=200)

    def __str__(self):
        return self.topic_name

class LanguageTopic(models.Model):
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    topic_name_in_language = models.CharField(max_length=200, default="Saludo")
 
    def __str__(self):
        return self.topic_name_in_language


class SituationalVideo(models.Model):
    language_topic = models.ForeignKey(LanguageTopic, on_delete=models.CASCADE, null=True)
    situation_description = models.CharField(max_length=200)
    video_with_transcript = models.FileField(null=True, blank=True)
    video_wihtout_transcript =  models.FileField(null=True, blank=True)

    # video_file = models.FileField(storage=fs, blank=True)

    def __str__(self):
        return self.situation_description

class LanguageSubtopic(models.Model):
    language_topic = models.ForeignKey(LanguageTopic, on_delete=models.CASCADE, null=True)
    subtopic_name = models.CharField(max_length=200, null=True)
    video_url = models.FileField(null=True, blank=True)

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

