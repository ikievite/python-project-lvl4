from django.contrib.auth import authenticate, get_user_model
from django.test import TestCase
from django.urls import reverse


class UsersViewTests(TestCase):
    def test_is_url_exists(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)


class CreateViewTest(TestCase):
    def test_create_user(self):
        user_data = {
            'username': 'test',
            'password1': '12test12',
            'password2': '12test12',
            'first_name': 'John',
            'last_name': 'Smith',
        }
        response = self.client.post(reverse('create-user'), user_data)
        user = authenticate(username='test', password='12test12')
        self.assertTrue(user.is_authenticated)


class UserUpdateViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            password='12test12',
            email='test@example.com',
            first_name='John',
            last_name='Smith',
        )
        self.user.save()

    def test_update_user(self):
        user_updated_data = {
            'username': 'new_test',
            'first_name': 'John2',
            'last_name': 'Smith2',
        }
        self.client.login(username='test', password='12test12')
        response = self.client.post(reverse('update-user', kwargs={'pk': 1}), user_updated_data)
        user = authenticate(username='new_test', password='12test12')
        self.assertTrue(user.is_authenticated)


class UserDeleteViewTest(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='test',
            password='12test12',
            email='test@example.com',
            first_name='John',
            last_name='Smith',
        )
        self.user.save()

    def test_delete_user(self):
        self.client.login(username='test', password='12test12')
        response = self.client.post(reverse('delete-user', kwargs={'pk': 1}))
        user = authenticate(username='test', password='12test12')
        self.assertTrue(user is None)
