from django.test import TestCase, Client
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.db import connection, reset_queries
from django.conf import settings


class TestView(APITestCase):
    fixtures = ['sample.json']
    def test_my_api_view_query_count(self):
        url = reverse('test')
        with self.assertNumQueriesLess(1):
            response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

