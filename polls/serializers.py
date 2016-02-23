__author__ = 'JAESEOKAN'


from rest_framework import serializers
from polls.models import Language
from polls.models import SituationalVideo, LanguageSubtopic, ExerciseQuestion

'''
from polls.serializers import LanguageSerializer
serializer=LanguageSerializer(language)
print(repr(serializer))
'''

class LanguageSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    name2 = serializers.CharField(required=True)



    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return Language.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.name = validated_data.get('title', instance.name)
        instance.name2 = validated_data.get('code', instance.name2)
        instance.save()
        return instance



class SituationalVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituationalVideo
        fields = ('language_topic','situation_description','video_with_transcript','video_wihtout_transcript')

class GrammarVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageSubtopic
        fields = ('language_topic','subtopic_name','grammar_video_file')

class ExerciseQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseQuestion
        fields = ('exercise','question_text','choice_1','choice_2','choice_3','choice_4','choice_5','choice_6','correct_answer')


'''
  pk = serializers.IntegerField(read_only=True)
    language_topic = serializers.IntergerField(required=True)
    situational_description = serializers.CharField(required=True)
    video_with_transcript =serializers.FileField(required=True)
    video_without_transcript=serializers.FileField(required=True)

    def create(self, validated_data):
        """
        Create and return a new `Snippet` instance, given the validated data.
        """
        return SituationalVideo.objects.create(**validated_data)

    def update(self, instance, validated_data):
        """
        Update and return an existing `Snippet` instance, given the validated data.
        """
        instance.language_topic = validated_data.get('langTopic', instance.language_topic)
        instance.situational_description = validated_data.get('description', instance.situational_description)
        instance.video_with_transcript = validated_data.get('transcript',instance.video_with_transcript)
        instance.video_without_transcript = validated_data.get('noTranscript',instance.video_without_transcript)
        instance.save()
        return instance
'''
