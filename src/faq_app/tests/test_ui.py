"""
Django UI Views test for the FAQ Application
"""

from http import HTTPStatus

from django.test import TestCase
from django.urls import reverse


class UIViewTests(TestCase):
    """UI Views test"""

    def test_home_page(self):
        """
        Ensure get some home page contents
        """
        response = self.client.get(reverse("home_page"))
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTemplateUsed(response, "faq/index.html")
        self.assertContains(
            response, '<a href="#" class="navbar-brand">Devn<b>Go</b></a>', html=True
        )
        self.assertContains(response, "<h4>Django FAQ's</h4>", html=True)

    def test_signup_valid(self):
        """
        Ensure we can sign up
        """
        response = self.client.post(
            reverse("signup"),
            data={
                "username": "newuser",
                "email": "",
                "password": "test",
                "password_confirm": "test",
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], reverse("home_page"))

    def test_signup_invalid(self):
        """
        Ensure we can not sign up with password not matching
        """
        response = self.client.post(
            reverse("signup"),
            data={
                "username": "newuser",
                "email": "",
                "password": "test",
                "password_confirm": "test1",
            },
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertNotEqual(response["Location"], reverse("home_page"))
        self.assertEqual(response["Location"], reverse("signup"))

    def test_login_with_invalid_credentials(self):
        """
        Ensure we can not login with invalid credentials
        """
        response = self.client.post(
            reverse("sign_in"), data={"username": "notfound", "password": "test"}
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], reverse("sign_in"))

    def test_login_with_valid_credentials(self):
        """
        Ensure we can not login with invalid credentials
        """
        # Sign Up
        self.test_signup_valid()
        response = self.client.post(
            reverse("sign_in"), data={"username": "newuser", "password": "test"}
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], reverse("home_page"))

    def test_new_question_success(self):
        """
        Ensure we can post new question
        """
        response = self.client.post(
            reverse("new_question"),
            data={"question": "My first question?", "author": "test@test.fr"},
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertEqual(response["Location"], reverse("home_page"))

    def test_new_answer_without_login(self):
        """
        Ensure we can not post new answer without login
        """
        response = self.client.post(
            reverse("new_answer"), data={"answer": "My first answer"}
        )
        self.assertEqual(response.status_code, HTTPStatus.FOUND)
        self.assertNotEqual(response["Location"], reverse("home_page"))
        self.assertEqual(response["Location"], "/login?next=/answer")
