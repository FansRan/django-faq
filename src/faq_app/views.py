"""
Django views for FAQ application
"""

from rest_framework import viewsets, permissions, authentication
from django.contrib.auth.models import User
from faq_app.models import Question, Answer
from faq_app.serializers import QuestionSerializer, AnswerSerializer, UserSerializer
from faq_app.permissions import IsOwnerOrReadOnly


# Create your views here.
class QuestionViewSet(viewsets.ModelViewSet):
    """Question Model ViewSet definition"""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = [permissions.AllowAny]


class AnswerViewSet(viewsets.ModelViewSet):
    """Question Model ViewSet definition"""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """User Model ViewSet definition"""

    queryset = User.objects.all()
    serializer_class = UserSerializer