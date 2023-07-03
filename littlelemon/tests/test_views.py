from django.test import TestCase
from restaurant.models import MenuItem
from restaurant.serializers import MenuSerializer
from rest_framework.test import APIClient
from django.contrib.auth.models import User

# Create your tests here.

class MenuViewTest(TestCase):
  def setUp(self):
    self.client = APIClient()
    self.user = User.objects.create_user(username='tester', password='testpassword')
    self.items = MenuItem.objects.bulk_create([
      MenuItem(title="Pasta", price=80, inventory=100),
      MenuItem(title="Canoli", price=80, inventory=100)
    ])
  def test_getall(self):
    self.client.login(username='tester', password='testpassword')
    response = self.client.get('http://localhost:8000/restaurant/menu/')
    # print(response.data)
    self.assertEqual(response.status_code, 200)
    self.assertContains(response, 'Canoli')
    self.client.logout()
