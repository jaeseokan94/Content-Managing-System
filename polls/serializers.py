__author__ = 'JAESEOKAN'


from rest_framework import serializers
from polls.models import Language, Topic
'''
from polls.serializers import LanguageSerializer
serializer=LanguageSerializer(language)
print(repr(serializer))
'''
class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = ('pk', 'name', 'name2')

class TopicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Topic
        fields = ('pk', 'level', 'topic_name')

