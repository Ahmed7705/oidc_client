# tests.py
from django.test import TestCase
from django.urls import reverse

class OIDCViewTests(TestCase):
    def test_oidc_login_redirects(self):
        response = self.client.get(reverse('oidc_login'))
        self.assertEqual(response.status_code, 302)
        self.assertIn('authorization', response['Location'])

    def test_oidc_callback_missing_state(self):
        response = self.client.get(reverse('oidc_callback'))
        self.assertEqual(response.status_code, 400)
        self.assertJSONEqual(response.content, {'error': 'State is missing'})

