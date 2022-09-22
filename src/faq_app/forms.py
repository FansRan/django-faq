"""
Django form definition
"""

from django import forms

from faq_app.models import Answer, Question


class QuestionForm(forms.ModelForm):
    """Form definition for Question."""

    class Meta:
        """Meta definition for Question Form."""

        model = Question
        fields = "__all__"


class AnswerForm(forms.ModelForm):
    """Form definition for Answer."""

    class Meta:
        """Meta definition for Answer Form."""

        model = Answer
        fields = "__all__"
