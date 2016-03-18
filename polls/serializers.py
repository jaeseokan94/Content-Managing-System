__author__ = 'JAESEOKAN'


from rest_framework import serializers
from polls.models import Language, SituationalVideo, LanguageSubtopic, ExerciseQuestion, ResourceItem, ResourceItemPicture, Level

'''
from polls.serializers import LanguageSerializer
serializer=LanguageSerializer(language)
print(repr(serializer))
'''

class LanguageSerializer(serializers.Serializer):
    pk = serializers.IntegerField(read_only=True)
    name = serializers.CharField(required=True)
    name_in_language = serializers.CharField(required=True)

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
        instance.name_in_language = validated_data.get('code', instance.name2)
        instance.save()
        return instance

class SituationalVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = SituationalVideo
        fields = ('language_topic','situation_description','video_with_transcript','video_without_transcript')

class GrammarVideoSerializer(serializers.ModelSerializer):
    class Meta:
        model = LanguageSubtopic
        fields = ('language_topic','subtopic_name','grammar_video_file')

class ExerciseQuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExerciseQuestion
        fields = ('exercise','question_text','choice_1','choice_2','choice_3','choice_4','choice_5','choice_6','correct_answer')

class ResourceItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceItem
        fields = ('word','pronounciation_guide_or_date','audio_url')

class ResourceItemNumbersSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceItem
        fields = ('word','word_in_language','audio_url')

class ResourceItemPictureSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceItemPicture
        fields = ('phrase','phrase_in_language','picture_url','audio_url')

class LevelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Level
        fields = ('level',)
