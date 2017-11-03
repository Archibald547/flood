from django.urls import resolve
from django.test import TestCase
from django.http import HttpRequest
from .views import home 

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