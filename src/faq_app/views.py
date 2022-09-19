"""
Django views for FAQ application
"""

from rest_framework import viewsets
from faq_app.models import Question, Answer
from faq_app.serializers import QuestionSerializer, AnswerSerializer


# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    """Question Model ViewSet definition"""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer


class AnswerViewSet(viewsets.ModelViewSet):
    """Question Model ViewSet definition"""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
