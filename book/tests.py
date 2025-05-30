from django.test import TestCase
from http.client import responses

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework_simplejwt.tokens import RefreshToken

from book.models import Book
from users.models import MyUser


class BookAPITestCase(APITestCase):
    def setUp(self):
        self.user = MyUser.objects.create_superuser(username = 'testusername', password='testpassword')
        refresh = RefreshToken.for_user(self.user)
        access_token = str(refresh.access_token)
        self.client = APIClient()
        self.client.credentials(HTTP_AUTHORIZATION = 'Bearer ' + access_token)
        self.item = Book.objects.create(title = 'Dunyo', author = 'Salom', published = '2025-12-12')

    def test_get_books(self):
        response = self.client.get('/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_create_book(self):
        data = {
            'title': 'Shaptoli',
            'author': 'Olma',
            'published': '2023-12-12'
        }
        response = self.client.post('/books/', data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Pomidor')

    def test_update_book(self):
        data = {
            'title': 'Shaptoli',
            'author': 'Olma',
            'published': '2023-12-12'
        }
        response = self.client.put(f"/books/{self.item.id}/", data, format = 'json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], 'Pomidor')

    def test_delete_book(self):
        response = self.client.delete(f"/books/{self.item.id}/")
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


    def test_validation_error(self):
        data = {
            'name': 'Shaptoli',
            'author': 'Olma',
            'published': '2023-12-12'
        }
        response = self.client.post('/books/', data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('title', response.data)