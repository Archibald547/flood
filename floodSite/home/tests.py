from django.test import TestCase
from django.contrib.auth.models import User

class HomeTestCase(TestCase):
    def setUp(self):
        User.objects.create_user(username='jacob', password='top_secret')

    def test_redirect_to_dashboard(self):
        """Check if the redirection works"""
        response = self.client.get('/dashboard', follow=True)
        self.assertRedirects(response, '/chatroom')

        response = self.client.get('/chatroom')
        self.assertEqual(response.status_code, 301)
