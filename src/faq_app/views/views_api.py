"""
Django views for FAQ application API
"""

from rest_framework import viewsets, mixins, permissions, filters
from django_filters.rest_framework import DjangoFilterBackend
from django.contrib.auth.models import User
from faq_app.models import Question, Answer
from faq_app.serializers import QuestionSerializer, AnswerSerializer, UserSerializer
from faq_app.permissions import IsOwnerOrReadOnly


# Create your views here.
class QuestionViewSet(mixins.CreateModelMixin,
                                mixins.ListModelMixin,
                                mixins.RetrieveModelMixin,
                                viewsets.GenericViewSet):
    """Question Model ViewSet definition"""

    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['question', 'author', 'created_at', 'updated_at']
    search_fields = ['question', 'author', 'created_at', 'updated_at']
    ordering_fields = ['question', 'author', 'created_at', 'updated_at']
    ordering = ['updated_at']


class AnswerViewSet(viewsets.ModelViewSet):
    """Question Model ViewSet definition"""

    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['question', 'answer', 'client', 'created_at', 'updated_at']
    search_fields = ['question', 'answer', 'client', 'created_at', 'updated_at']
    ordering_fields = ['question', 'answer', 'client', 'created_at', 'updated_at']
    ordering = ['updated_at']

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class UserViewSet(viewsets.ReadOnlyModelViewSet):
    """User Model ViewSet definition"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
