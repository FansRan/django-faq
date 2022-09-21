"""
Django API test for the FAQ Application
"""

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from faq_app.models import Question, Answer


class AuthTests(APITestCase):
    """API test for Authentication"""

    def register(self):
        """
        Ensure we can register
        """
        url = reverse('register')
        data = {'username': 'test', 'password': 'password_ex', 'password_confirm': 'password_ex'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login(self):
        """
        Ensure we can authenticate
        """
        # Registration
        self.register()
        # Login
        logged = self.client.login(username='test', password='password_ex')
        self.assertTrue(logged)

    def test_get_token(self):
        """
        Ensure we can get the token authentication
        """
        # Registration
        self.register()
        # Login
        url = reverse('token_obtain_pair')
        data = {'username': 'test', 'password': 'password_ex'}
        response = self.client.post(url, data, format='json')
        self.assertTrue('access' in response.data)
        self.assertTrue('refresh' in response.data)


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
        self.test_create_question()
        url = reverse('question-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)


class AnswerTests(APITestCase):
    """API test for Answer model"""

    def test_create_answer(self):
        """
        Ensure we can create a new Answer object.
        """
        # Register
        register_data = {'username': 'john', 'password': 'password_ex', 'password_confirm': 'password_ex'}
        self.client.post(reverse('register'), register_data, format='json')
        # Login
        self.client.login(username='john', password='password_ex')
        # Post new question
        question_url = reverse('question-list')
        question_data = {'question': 'Va-t-il créer une réponse?'}
        self.client.post(question_url, question_data, format='json')
        # Post new answer
        url = reverse('answer-list')
        data = {'answer': 'Oui', 'question': question_url + '1/'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Answer.objects.count(), 1)
        self.assertEqual(Answer.objects.get().answer, 'Oui')

    def test_list_answers(self):
        """
        Ensure we can get a list of Answer object.
        """
        self.test_create_answer()
        url = reverse('answer-list')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)
