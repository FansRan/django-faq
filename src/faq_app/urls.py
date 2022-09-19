"""
Django FAQ application url definition
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from faq_app.views import QuestionViewSet, AnswerViewSet

router = DefaultRouter()
router.register('questions', QuestionViewSet, basename='questions')
router.register('answers', AnswerViewSet, basename='answers')

urlpatterns = [
    path('api/', include(router.urls))
]