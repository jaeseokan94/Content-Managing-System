from django.contrib import admin

from .models import Language, Topic, SituationalVideo, Exercise, LanguageTopic, LanguageSubtopic, ExerciseQuestion

admin.site.register(Language)

admin.site.register(Topic)
admin.site.register(LanguageTopic)
admin.site.register(LanguageSubtopic)
admin.site.register(SituationalVideo)
admin.site.register(Exercise)
admin.site.register(ExerciseQuestion)