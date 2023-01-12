from django.contrib import admin

from .models import Question, OptionAnswer, Questionnaire, Statistic

admin.site.register(Questionnaire)
admin.site.register(Question)
admin.site.register(OptionAnswer)
admin.site.register(Statistic)
