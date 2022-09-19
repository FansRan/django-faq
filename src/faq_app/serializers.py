"""
Django serializers definition
"""

from rest_framework import serializers
from faq_app.models import Answer, Question


class QuestionSerializer(serializers.ModelSerializer):
    """Serializers for Question Model"""

    class Meta:
        """Meta definition for Question Serializer."""

        model = Question
        fields = '__all__'

class AnswerSerializer(serializers.ModelSerializer):
    """Serializers for Answer Model"""

    class Meta:
        """Meta definition for Question Serializer."""

        model = Answer
        fields = '__all__'