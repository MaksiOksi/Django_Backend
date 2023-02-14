from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse

from store.models import Book
from store.serializers import BookSerializer


class BooksApiTestCase(APITestCase):
    def setUp(self):
        self.book_1 = Book.objects.create(name='Test book 1', price=25.2,
                                          author_name='author1')
        self.book_2 = Book.objects.create(name='Test book 2', price=25.67,
                                          author_name='author4')
        self.book_3 = Book.objects.create(name='Test book author1', price=25.67,
                                          author_name='author2')

    def test_get(self):
        # For getting a list url instead
        url = reverse('book-list')
        response = self.client.get(url)
        serializer_data = BookSerializer([self.book_1, self.book_2, self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)

    def test_get_search(self):
        url = reverse('book-list')
        response = self.client.get(url, data={'search': 'author1'})
        serializer_data = BookSerializer([self.book_1,self.book_3], many=True).data
        self.assertEqual(status.HTTP_200_OK, response.status_code)
        self.assertEqual(serializer_data, response.data)
