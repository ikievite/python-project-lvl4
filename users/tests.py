from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import authenticate


class UsersViewTests(TestCase):
    def test_is_url_exists(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)


class CreateViewTest(TestCase):
    def test_create_user(self):
        create_user_url = '/users/create/'
        user = {
            'username': 'test',
            'password1': '12test12',
            'password2': '12test12',
            'first_name': 'fname',
            'last_name': 'lname'
        }
        response = self.client.post(create_user_url, user)
        user = authenticate(username='test', password='12test12')
        self.assertTrue(user.is_authenticated)
