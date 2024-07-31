from django.test import TestCase, Client
from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from django.db import connection, reset_queries


class TestView(APITestCase):
    def test_my_api_view_query_count(self):
        url = reverse('list')

        with self.assertNumQueries(1):
            response = self.client.get(url)
        self.assertEqual(response.status_code, 200)

