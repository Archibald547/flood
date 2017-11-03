from django.test import TestCase, RequestFactory
from django.contrib.auth.models import User
from .models import MyProfile
from .regbackend import MyRegistrationView
from django.urls import resolve
from django.http import HttpRequest
from .views import home 

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

class HomePageTest(TestCase):

    #tests that the root url directs the user to the correct view in home.views
    def test_root_url_directs_to_home_page_view(self):
        found = resolve('/')  
        self.assertEqual(found.func, home)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()  
        response = home(request)  
        html = response.content.decode('utf8')  
        self.assertTrue(html.startswith('<!DOCTYPE html>'))  
        self.assertIn('<title>Before The Flood</title>', html);
