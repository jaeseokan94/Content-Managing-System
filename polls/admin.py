from django.contrib import admin

from .models import Language, Topic, SituationalVideo, Exercise, LanguageTopic, LanguageSubtopic, ExerciseQuestion, Resource, ResourceItem, ResourceItemPicture, Dialect

admin.site.register(Language)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
	list_filter = ('level',)

admin.site.register(LanguageTopic)
admin.site.register(LanguageSubtopic)
admin.site.register(SituationalVideo)
admin.site.register(Exercise)
admin.site.register(ExerciseQuestion)
admin.site.register(Dialect)
admin.site.register(Resource)
admin.site.register(ResourceItem)
admin.site.register(ResourceItemPicture)