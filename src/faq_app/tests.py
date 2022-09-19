"""
Django test for the FAQ Application
"""

from http import client
from django.test import TestCase
from django.contrib.auth.models import User
from faq_app.models import Answer, Question


# Create your tests here.
class QuestionTestCase(TestCase):
    """Unit test for Question Model"""

    def setUp(self):
        Question.objects.create(question="What's the most popular tech?")
        Question.objects.create(question="Is that the best at all?")

    def test_questions_is_correct(self):
        """Questions are correctly the expected"""
        tech_question = Question.objects.get(pk=1)
        best_question = Question.objects.get(pk=2)
        self.assertEqual(str(tech_question), "What's the most popular tech?")
        self.assertEqual(str(best_question), "Is that the best at all?")


class AnswerTestCase(TestCase):
    """Unit test for Answer Model"""

    def setUp(self):
        Question.objects.create(question="What's the most popular tech?")
        Question.objects.create(question="Is that the best at all?")
        user = User.objects.create_user('john', 'john@doe.com')
        Answer.objects.create(question_id=1, client=user, answer="Python the best")
        Answer.objects.create(question_id=2, client=user, answer="Yes, it is")

    def test_answers_is_correct(self):
        """Answers are correctly the expected"""
        tech_answer = Answer.objects.get(pk=1)
        best_answer = Answer.objects.get(pk=2)
        self.assertEqual(str(tech_answer), "Python the best")
        self.assertEqual(str(best_answer), "Yes, it is")

    def test_answers_client_is_not_null(self):
        """Answers are correctly have the expected client"""
        tech_answer = Answer.objects.get(pk=1)
        best_answer = Answer.objects.get(pk=2)
        self.assertNotEqual(tech_answer.client, None)
        self.assertNotEqual(best_answer.client, None)
