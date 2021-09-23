from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from statuses.models import Status


class StatusListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
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


class StatusCreateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='testuser',
            password='superpass',
        )
        test_user.save()

    def test_create_status(self):
        login = self.client.login(username='testuser', password='superpass')
        response = self.client.post(reverse('create-status'), {'name': 'test_status2'})
        self.assertEqual(response.status_code, 302)

    def test_uses_correct_template(self):
        login = self.client.login(username='testuser', password='superpass')
        response = self.client.get(reverse('create-status'))
        self.assertTemplateUsed(response, 'statuses/create.html')


class StatusUpdateViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        test_user = User.objects.create_user(
            username='testuser',
            password='superpass',
        )
        test_user.save()
        new_status = Status.objects.create(name='another_status')
        new_status.save()

    def test_update_status(self):
        login = self.client.login(username='testuser', password='superpass')
        response = self.client.post(
            reverse('update-status', kwargs={'pk': 1}),
            {'name': 'yet_another_status'},
        )
        self.assertEqual(Status.objects.get(pk=1).name, 'yet_another_status')
