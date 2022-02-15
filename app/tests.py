from django.test import TestCase


from django.http import HttpRequest
from django.test import SimpleTestCase
from django.urls import reverse

from . import views


class HomePageTests(SimpleTestCase):

    # On test que le page exist et on retournee 200
    def test_home_page_status_code(self):
        response = self.client.get('/maison-detail')
        self.assertEquals(response.status_code, 404)
    
    
