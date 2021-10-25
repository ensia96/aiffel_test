from django.test import TestCase
from django.urls import reverse
from django.db import transaction
from .models import User

CONTENT_TYPE = "application/json"


class SignUpTest(TestCase):
    URL = reverse("sign-up")
    PAYLOAD = {"content_type": CONTENT_TYPE}

    def setUp(self):
        User.objects.create(
            username="test_id_1",
            password="test_password",
            nickname="test_user",
            email="email@for.test_1",
            age=20,
            phone="010-0000-0000",
        )

    def tearDown(self):
        User.objects.all().delete()

    def test_signup_success(self):
        self.PAYLOAD["data"] = {
            "username": "test_id",
            "password": "test_password",
            "nickname": "test_user",
            "email": "email@for.test",
            "age": 20,
            "phone": "010-0000-0000",
        }

        res = self.client.post(self.URL, **self.PAYLOAD)
        self.assertEqual(res.status_code, 201)

    def test_signup_without_certain_key(self):
        keys = ["username", "password", "nickname", "email", "age", "phone"]
        self.PAYLOAD["data"] = {
            "username": "test_id",
            "password": "test_password",
            "nickname": "test_user",
            "email": "email@for.test",
            "age": 20,
            "phone": "010-0000-0000",
        }

        for key in keys:
            value = self.PAYLOAD["data"].pop(key)

            res = self.client.post(self.URL, **self.PAYLOAD)
            self.assertEqual(res.json().get("message"), f"'{key}' is not provided.")
            self.assertEqual(res.status_code, 400)

            self.PAYLOAD["data"][key] = value

    def test_signup_with_duplicated_user_data(self):
        keys = ["username", "email"]
        self.PAYLOAD["data"] = {
            "username": "test_id",
            "password": "test_password",
            "nickname": "test_user",
            "email": "email@for.test",
            "age": 20,
            "phone": "010-0000-0000",
        }

        for key in keys:
            self.PAYLOAD["data"][key] += "_1"

            try:
                with transaction.atomic():
                    res = self.client.post(self.URL, **self.PAYLOAD)

                self.assertEqual(res.json().get("message"), f"{key} aleady exists.")
                self.assertEqual(res.status_code, 400)

                self.PAYLOAD["data"][key] = self.PAYLOAD["data"][key][:-2]
            except Exception:
                pass
