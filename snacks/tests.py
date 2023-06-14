from django.test import TestCase
from django.urls import reverse
# Create your tests here.

class SnakesTestCase(TestCase):
    def test_snacks_list_status(self):
        url = reverse('snacks')
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code,200)


    def test_snacks_list_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        print(response)
        self.assertTemplateUsed(response,'snack_list.html')

    def test_snacks_detail_status(self):
        url = reverse('snacks')
        response = self.client.get(url)
        print(response)
        self.assertEqual(response.status_code,200)


    def test_snacks_detail_template(self):
        url = reverse('snacks')
        response = self.client.get(url)
        print(response)
        self.assertTemplateUsed(response,'snack_detail.html')


