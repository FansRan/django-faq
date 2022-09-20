"""
Django API test for the FAQ Application
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from faq_app.models import Question, Answer


class AuthTests(APITestCase):
    """API test for Authentication"""

    def test_registration_login(self):
        """
        Ensure we can register then authenticate
        """
        # Registration
        url = reverse('rest_registration:register')
        data = {'username': 'test', 'password': 'password_ex', 'password_confirm': 'password_ex'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        # Login
        logged = self.client.login(username='test', password='password_ex')
        self.assertTrue(logged)


class QuestionTests(APITestCase):
    """API test for Question model"""

    def test_create_question(self):
        """
        Ensure we can create a new Question object.
        """
        url = reverse('question-list')
        data = {'question': 'Est-il créer?'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Question.objects.count(), 1)
        self.assertEqual(Question.objects.get().question, 'Est-il créer?')

    def test_list_questions(self):
        """
        Ensure we can get a list of Question object.
        """
        url = reverse('question-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)


class AnswerTests(APITestCase):
    """API test for Answer model"""

    def test_create_answer(self):
        """
        Ensure we can create a new Answer object.
        """
        # Registration
        register_url = reverse('rest_registration:register')
        register_data = {'username': 'john', 'password': 'password_example', 'password_confirm': 'password_example'}
        self.client.post(register_url, register_data, format='json')

        # Login
        self.client.login(username='john', password='password_example')

        # Post new question
        question_url = reverse('question-list')
        question_data = {'question': 'Va-t-il créer une reponse?'}
        self.client.post(question_url, question_data, format='json')

        # Post new answer
        answer_url = reverse('answer-list')
        answer_data = {'answer': 'Oui', 'question': question_url + '1/'}
        response = self.client.post(answer_url, answer_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Answer.objects.count(), 1)
        self.assertEqual(Answer.objects.get().answer, 'Oui')

    def test_list_answers(self):
        """
        Ensure we can get a list of Answer object.
        """
        url = reverse('answer-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
