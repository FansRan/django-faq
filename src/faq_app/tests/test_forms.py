"""
Django Form test for the FAQ Application
"""

from django.test import TestCase
from django.contrib.auth.models import User
from faq_app.forms import QuestionForm, AnswerForm


class QuestionFormTest(TestCase):
    """Form test for Question"""

    def test_question_without_question_mark(self):
        """
        Ensure question error without ending with question mark
        """
        form = QuestionForm(data={"question": "without question mark"})
        self.assertEqual(form.errors["question"], ["Must end with question mark"])

    def test_question_missing_author(self):
        """
        Ensure question error with missing author
        """
        form = QuestionForm(data={"question": "with question mark?"})
        self.assertEqual(form.errors["author"], ['This field is required.'])

    def test_question_end_with_question_mark(self):
        """
        Ensure question ending with question mark
        """
        form = QuestionForm(data={"question": "with question mark?"})
        self.assertFalse("question" in form.errors)

    def test_question_have_author(self):
        """
        Ensure question have author
        """
        form = QuestionForm(data={"question": "with question mark?", "author": "test@test.fr"})
        self.assertFalse("author" in form.errors)


class AnswerFormTest(TestCase):
    """Form test for Answer"""

    def test_answer_without_client_and_question(self):
        """
        Ensure answer error with missing client, question
        """
        form = AnswerForm(data={"answer": "test answer"})
        self.assertEqual(form.errors["question"], ['This field is required.'])
        self.assertEqual(form.errors["client"], ['This field is required.'])

    def test_answer_with_not_exist_client_question(self):
        """
        Ensure answer error with not exist client and answer
        """
        form = AnswerForm(data={"client": "0", "question": "0"})
        self.assertEqual(form.errors["question"], ['Select a valid choice. That choice is not one of the available choices.'])
        self.assertEqual(form.errors["client"], ['Select a valid choice. That choice is not one of the available choices.'])

    def test_answer_with_valid_data(self):
        """
        Ensure answer valid
        """
        QuestionForm(data={"question": "with question mark?", "author": "test@test.fr"}).save()        
        user = User.objects.create_user('john', 'john@doe.com')
        form = AnswerForm(data={"answer": "test answer", "client": user.id, "question": "1"})
        self.assertTrue(form.is_valid())
