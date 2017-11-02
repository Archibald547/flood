from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import MyProfile
from .regbackend import MyRegistrationView
# Create your tests here.

class Test_user_login(TestCase):
    def setUp(self):
        self.credentials = {
            'username' : 'testcase',
            'password' : 'Teser123'
        }
        User.objects.create_user(**self.credentials)

    def test_loggedin(self):
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.assertRedirects(response, '/')

    def test_user_incorrect_password(self):
        # self.logout()
        response = self.client.post('/accounts/login/', 'testcase', 'wrongpass', follow=True)
        self.assertFalse(response.context['user'].is_authenticated)

