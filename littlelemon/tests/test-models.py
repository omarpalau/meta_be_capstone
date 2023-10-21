from django.test import TestCase
from restaurant.models import *
from restaurant.serializers import MenuItemSerializer

class MenuItemTest(TestCase):
    def test_get_item(self):
        item = MenuItem.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.assertEqual(item, "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):

        MenuItem.objects.create(title="Dish1", price=10.0)
        MenuItem.objects.create(title="Dish2", price=15.0)

    def test_getall(self):

        response = self.client.get('/restaurant/menu/')

        menus = MenuItem.objects.all()
        serializer = MenuItemSerializer(menus, many=True)

        self.assertEqual(response.data, serializer.data)
