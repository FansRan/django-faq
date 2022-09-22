"""
Django admin registration
"""

from django.contrib import admin

from faq_app.models import Answer, Question


# Register your models here.
@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    """Admin View for Question"""

    list_display = ("question", "author")
    list_filter = ("question", "author")


@admin.register(Answer)
class AnswerAdmin(admin.ModelAdmin):
    """Admin View for Answer"""

    list_display = (
        "answer",
        "question",
        "client",
    )
    list_filter = (
        "answer",
        "question",
        "client",
    )
