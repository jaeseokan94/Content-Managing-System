from django.contrib import admin

from .models import Language, Topic, SituationalVideo, LectureVideo, Exercise

admin.site.register(Language)

@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
	pass

admin.site.register(SituationalVideo)
admin.site.register(LectureVideo)
admin.site.register(Exercise)