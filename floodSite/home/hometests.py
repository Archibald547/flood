from django.test import TestCase
from django.shortcuts import reverse, redirect
from .views import *

# Create your tests here.

class HomeTests(TestCase):
    def test_homePageLoad(self):
        response = self.client.get('')
        self.assertEquals(response.status_code, 200)
        self.assertTemplateUsed(response, 'home.html')

    def test_homePageIncorrect(self):
        response = self.client.get('home')
        self.assertEquals(response.status_code, 404)

    def test_homePageContent(self):
        response = self.client.get('')
        self.assertTemplateUsed(response, 'home.html')
        self.assertContains(response, '<h3>What We Do</h3><br>', status_code=200)

    def test_hometochat(self):
        response = self.client.get('/chat/', follow=True)
        self.assertRedirects(response, '/accounts/login/?next=/chat/')
        self.assertContains(response, "", status_code=200)


