"""
Django FAQ application url definition
"""

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from faq_app import views

router = DefaultRouter()
router.register(r'questions', views.QuestionViewSet, basename='question')
router.register(r'answers', views.AnswerViewSet, basename='answer')
router.register(r'users', views.UserViewSet, basename='user')

urlpatterns = [
    path('api/', include(router.urls))
]
