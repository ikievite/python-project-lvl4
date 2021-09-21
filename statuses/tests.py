from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse


class StatusListViewTest(TestCase):
    def setUp(self):
        test_user = User.objects.create_user(
            username='testuser',
            password='superpass',
        )
        test_user.save()

    def test_redirect_if_not_logged(self):
        response = self.client.get(reverse('statuses'))
        self.assertRedirects(response, '/login/')

    def test_logged_in(self):
        login = self.client.login(username='testuser', password='superpass')
        response = self.client.get(reverse('statuses'))
        self.assertEqual(str(response.context['user']), 'testuser')

    def test_show_statuses(self):
        login = self.client.login(username='testuser', password='superpass')
        response = self.client.get(reverse('statuses'))
        self.assertEqual(response.status_code, 200)

    def test_uses_correct_template(self):
        login = self.client.login(username='testuser', password='superpass')
        response = self.client.get(reverse('statuses'))
        self.assertTemplateUsed(response, 'statuses/statuses.html')
