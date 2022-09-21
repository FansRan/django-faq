"""
Django Model test for the FAQ Application
"""

from django.test import TestCase
from django.contrib.auth.models import User
from faq_app.models import Answer, Question


# Create your tests here.
class QuestionTestCase(TestCase):
    """Unit test for Question Model"""

    @classmethod
    def setup_data(cls):
        """Questions test data"""
        Question.objects.create(question="What's the most popular tech?")

    def test_questions_is_correct(self):
        """Questions are correctly the expected"""
        self.setup_data()
        tech_question = Question.objects.get(pk=1)
        self.assertTrue(isinstance(tech_question, Question))
        self.assertEqual(str(tech_question), "What's the most popular tech?")
        self.assertNotEqual(str(tech_question), "Is that the best at all?")


class AnswerTestCase(TestCase):
    """Unit test for Answer Model"""

    def setUp(self):
        user = User.objects.create_user('john', 'john@doe.com')
        QuestionTestCase.setup_data()
        Answer.objects.create(question_id=1, client=user, answer="Python the best")

    def test_answers_is_correct(self):
        """Answers are correctly the expected"""
        tech_answer = Answer.objects.get(pk=1)
        self.assertEqual(str(tech_answer), "Python the best")
        self.assertNotEqual(str(tech_answer), "Yes, it is")

    def test_answers_client_is_not_null(self):
        """Answers are correctly have the expected client"""
        tech_answer = Answer.objects.get(pk=1)
        self.assertTrue(isinstance(tech_answer.client, User))
        self.assertNotEqual(tech_answer.client, None)
