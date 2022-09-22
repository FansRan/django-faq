"""
Django serializers definition
"""

from django.contrib.auth.models import User
from rest_framework import serializers

from faq_app.models import Answer, Question


class QuestionSerializer(serializers.HyperlinkedModelSerializer):
    """Serializers for Question Model"""

    answers = serializers.HyperlinkedRelatedField(
        many=True, view_name="answer-detail", read_only=True
    )

    class Meta:
        """Meta definition for Question Serializer."""

        model = Question
        fields = ["id", "author", "question", "answers", "created_at", "updated_at"]


class AnswerSerializer(serializers.HyperlinkedModelSerializer):
    """Serializers for Answer Model"""

    client = serializers.ReadOnlyField(source="client.get_full_name")

    class Meta:
        """Meta definition for Question Serializer."""

        model = Answer
        fields = ["id", "answer", "client", "question", "created_at", "updated_at"]


class UserSerializer(serializers.HyperlinkedModelSerializer):
    """Serializers for User Model"""

    answers = serializers.HyperlinkedRelatedField(
        many=True, view_name="answer-detail", read_only=True
    )
    full_name = serializers.CharField(source="get_full_name")

    class Meta:
        """Meta definition for User Serializer."""

        model = User
        fields = ["id", "full_name", "answers"]
