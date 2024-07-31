from django.test import TestCase, Client
from django.urls import reverse
from django.db import connection, reset_queries


class TestView(TestCase):
    def test_order_list(self):
        client = Client()
        reset_queries()

        response = client.get(reverse('list'))
        print(len(connection.queries))


