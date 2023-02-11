from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from store.models import Book
from store.serializers import BookSerializer


class BooksApiTestCase(APITestCase):
    def test_get(self):
        book_1 = Book.objects.create(name='Test book 1', price=25.2)
        book_2 = Book.objects.create(name='Test book 2', price=25.67)
        # For getting a list url instead
        url = reverse('book-list')
        response = self.client.get(url)
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        serializer_data = BookSerializer([book_1, book_2], many=True).data
        self.assertEqual(serializer_data, response.data)
