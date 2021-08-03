from django.test import TestCase
from django.urls import reverse


class UsersViewTests(TestCase):
    def test_is_url_exists(self):
        response = self.client.get(reverse('users'))
        self.assertEqual(response.status_code, 200)
