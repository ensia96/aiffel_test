from django.test import TestCase
from django.urls import reverse
from .models import User

CONTENT_TYPE = "application/json"


class SignUpTest(TestCase):
    URL = reverse("sign-up")

    def tearDown(self):
        User.objects.all().delete()

    def test_signup_success(self):
        data = {
            "username": "test_id",
            "password": "test_password",
            "nickname": "test_user",
            "email": "email@for.test",
            "age": 20,
            "phone": "010-0000-0000",
        }

        res = self.client.post(self.URL, data=data, content_type=CONTENT_TYPE)
        self.assertEqual(res.status_code, 201)

    def test_signup_without_certain_key(self):
        keys = ["username", "password", "nickname", "email", "age", "phone"]
        data = {
            "username": "test_id",
            "password": "test_password",
            "nickname": "test_user",
            "email": "email@for.test",
            "age": 20,
            "phone": "010-0000-0000",
        }

        for key in keys:
            value = data.pop(key)

            res = self.client.post(self.URL, data=data, content_type=CONTENT_TYPE)
            self.assertEqual(res.json().get("message"), f"'{key}' is not provided.")
            self.assertEqual(res.status_code, 400)

            data[key] = value
