from django.test import TestCase

from store.models import Book
from store.serializers import BookSerializer


class BookSerializerTestCase(TestCase):
    def test_ok(self):
        book_1 = Book.objects.create(name='Test book 1', price=25.2,
                                     author_name='Garry')
        book_2 = Book.objects.create(name='Test book 2', price=25.67,
                                     author_name='Marry')
        data = BookSerializer([book_1, book_2], many=True).data
        expect_data = [
            {
                'id': book_1.id,
                'name': 'Test book 1',
                'price': '25.20',
                'author_name': 'Garry',
            },
            {
                'id': book_2.id,
                'name': 'Test book 2',
                'price': '25.67',
                'author_name': 'Marry',
            }
        ]
        self.assertEqual(expect_data, data)
