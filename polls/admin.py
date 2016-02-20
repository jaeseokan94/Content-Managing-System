from django.contrib import admin


from .models import Language, Topic, SituationalVideo, LectureVideo, Exercise, Dialect, Resource, ResourceItem, ResourceItemPicture, LanguageTopic, LanguageSubtopic, ExerciseQuestion

admin.site.register(Language)

admin.site.register(Topic)
admin.site.register(LanguageTopic)
admin.site.register(LanguageSubtopic)
admin.site.register(SituationalVideo)
admin.site.register(Exercise)
admin.site.register(ExerciseQuestion)
admin.site.register(LectureVideo)
admin.site.register(Exercise)
admin.site.register(Dialect)
admin.site.register(Resource)
admin.site.register(ResourceItem)
admin.site.register(ResourceItemPicture)
