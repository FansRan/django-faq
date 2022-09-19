from django.contrib import admin
from .models import Answer, Question

# Register your models here.

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    '''Admin View for Question'''

    list_display = ('question',)
    list_filter = ('question',)


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    '''Admin View for Answer'''

    list_display = ('question', 'answer',)
    list_filter = ('question', 'answer',)