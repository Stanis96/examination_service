from django.contrib import admin

from .models import ListQuestion, OptionAnswer, SetQuestionnaire, Statistic

admin.site.register(SetQuestionnaire)
admin.site.register(ListQuestion)
admin.site.register(OptionAnswer)
admin.site.register(Statistic)
