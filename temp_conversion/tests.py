from django.test import Client, TestCase
from django.urls import reverse

# Create your tests here.
class TempConversionTests(TestCase):

    def test_temp_text(self):
        client = Client()
        response = client.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your converted temperature of None in None is None in None.")

    def test_view_users_correct_templates(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_temp_form(self):
        client = Client()
        response = client.post('/', {'rd': 'F', 'temp': 32})
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Your converted temperature of 32 in F is 0.0 in C.")