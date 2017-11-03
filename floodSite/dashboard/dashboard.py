from django.test import TestCase
from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from home.models import MyProfile
import datetime

# Create your tests here.

class ProfileTests(TestCase):
    def setUp(self):
        self.credentials = {
            'username': 'testupdate',
            'password': 'Testme123'
        }
        User.objects.create_user(**self.credentials)
        response = self.client.post('/accounts/login/', self.credentials, follow=True)
        self.assertTrue(response.context['user'].is_active)
        self.assertRedirects(response, '/')

    def test_dashboardLoad(self):
        response = self.client.get('/dashboard/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'dashboard.html')

    def test_dashboardIncorrect(self):
        response = self.client.get('home')
        self.assertEquals(response.status_code, 404)

    def test_GetProfile(self):
        response = self.client.get('/profile/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')

    def test_UpdateProfile(self):
        response = self.client.get('/profile/')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'profile.html')




