__author__ = 'JAESEOKAN'


from rest_framework import serializers
from polls.models import Language
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