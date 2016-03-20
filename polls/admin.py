from django.contrib import admin

from .models import Language, Topic, SituationalVideo, Exercise, LanguageTopic, LanguageSubtopic, ExerciseQuestion, \
	ExerciseVocabularyQuestion, Resource, ResourceItem, ResourceItemPicture, Dialect, LevelLanguage, Level, Glossary

admin.site.register(Language)
admin.site.register(Level)
admin.site.register(Glossary)
'''
 glossary need to be filtered according to lang
'''

@admin.register(LevelLanguage)
class LevelAdmin(admin.ModelAdmin):
	list_filter = ('language',)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
	list_filter = ('level',)

@admin.register(LanguageTopic)
class LanguageTopicAdmin(admin.ModelAdmin):
	list_filter = ('language',)

@admin.register(ExerciseQuestion)
class ExerciseQuestionAdmin(admin.ModelAdmin):
	list_filter = ('exercise',)

@admin.register(ExerciseVocabularyQuestion)
class ExerciseVocabularyQuestionAdmin(admin.ModelAdmin):
	list_filter = ('exercise',)

@admin.register(Dialect)
class DialectAdmin(admin.ModelAdmin):
	list_filter = ('language_id',)

@admin.register(LanguageSubtopic)
class LanguageSubtopicAdmin(admin.ModelAdmin):
	list_filter = ('language_topic',)

@admin.register(Resource)
class ResourceAdmin(admin.ModelAdmin):
	list_filter = ('dialect_id',)

@admin.register(ResourceItem)
class ResourceItemAdmin(admin.ModelAdmin):
	list_filter = ('resource_id',)

@admin.register(ResourceItemPicture)
class ResourceItemPictureAdmin(admin.ModelAdmin):
	list_filter = ('resource_id',)




admin.site.register(Exercise)
admin.site.register(SituationalVideo)