"""
Django UI Views test for the FAQ Application
"""

from http import HTTPStatus
from django.urls import reverse
from django.test import TestCase


class UIViewTests(TestCase):
    """UI Views test"""

    def test_home_page(self):
        """
        Ensure we can register
        """
        response = self.client.get(reverse('home_page'))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, 'faq/index.html')
        self.assertContains(response, '<a href="#" class="navbar-brand">Devn<b>Go</b></a>', html=True)
        self.assertContains(response, "<h4>Django FAQ's</h4>", html=True)

    def test_new_question_success(self):
        """
        Ensure we can post new question
        """
        response = self.client.post(reverse('new_question'), \
            data={"question": "My first question?", "author": "test@test.fr"})
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], reverse('home_page'))

    def test_new_answer_without_login(self):
        """
        Ensure we can not post new answer without login
        """
        response = self.client.post(reverse('new_answer'), \
            data={"answer": "My first answer"})
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertNotEqual(response["Location"], reverse('home_page'))
        self.assertEqual(response["Location"], '/login?next=/answer')
        