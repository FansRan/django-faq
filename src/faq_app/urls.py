"""
Django FAQ application url definition
"""

from django.urls import include, path
from rest_framework.routers import DefaultRouter

from faq_app import views

router = DefaultRouter()
router.register(r"questions", views.QuestionViewSet, basename="question")
router.register(r"answers", views.AnswerViewSet, basename="answer")
router.register(r"users", views.UserViewSet, basename="user")

urlpatterns = [
    path("", views.index, name="home_page"),
    path("signup", views.signup, name="signup"),
    path("login", views.sign_in, name="sign_in"),
    path("logout", views.logout, name="logout"),
    path("question", views.question, name="new_question"),
    path("answer", views.answer, name="new_answer"),
    path("api/", include(router.urls)),
]
