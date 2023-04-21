from django.test import TestCase, Client
from .models import Url
import random, string


class UrlShortenerTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_home_view(self):
        response = self.client.get("/")

        self.assertTemplateUsed(response, "main_app/home.html")
        self.assertEqual(response.status_code, 200)

    def test_url_created_view(self):
        url = "http://127.0.0.1:8000/"

        new_url = Url(
            url=url,
            slug="".join(random.choice(string.ascii_letters) for x in range(10)),
        )
        new_url.save()
        response = self.client.get("/url_created/")

        self.assertTemplateUsed(response, "main_app/short_url.html")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, url)
