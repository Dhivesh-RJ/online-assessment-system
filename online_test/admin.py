from django.contrib import admin
from .models import Subject, Question, Test, Result

admin.site.register(Subject)
admin.site.register(Question)
admin.site.register(Test)
admin.site.register(Result)
