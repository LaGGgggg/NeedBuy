from django.test import TestCase
from django.test.client import Client

# Create your tests here.


class HomePageAppTestCase(TestCase):

    def setUp(self):

        self.client = Client()

    def test_main_page_requests(self):

        # index.html

        request = self.client.get('/')

        self.assertTemplateUsed(request, 'home_page_app/index.html')
        self.assertEqual(request.status_code, 200)

        # error.html

        request = self.client.get('/bad-address/')

        self.assertTemplateUsed(request, 'error.html')
        self.assertEqual(request.status_code, 200)
