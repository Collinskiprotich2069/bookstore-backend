from rest_framework.test import APIClient
import unittest
from django.test import TestCase
from rest_framework import status
from django.urls  import reverse
from .views import BookListView
class BookListViewTestCase(unittest.TestCase):
    def set(self):
        self.client = APIClient()
        self.api_url = reverse('BookListView')
        
        def test_api_get_request(self):
            response = self.client.get(self.api_url)
            self.asertEqual(response.status_code, status.HTTP_200_OK    )


