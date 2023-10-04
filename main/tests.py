from django.test import TestCase, Client
from main.models import Item

class mainTest(TestCase):
    # # test_main_url_is_exist: memastikan bahwa url /main/ ada
    # def test_main_url_is_exist(self):
    #     response = Client().get('')
    #     self.assertEqual(response.status_code, 200)
    
    # # test_main_using_main_template: memastikan bahwa url /main/ menggunakan template main.html
    # def test_main_using_main_template(self):
    #     response = Client().get('')
    #     self.assertTemplateUsed(response, 'main.html')

    # test_pokeball_item: memastikan bahwa item pokeball ada
    def test_pokeball_item(self):
        pokeBall = Item.objects.create(name='Pokeball', amount=10, description='Pokeball is a ball')
        field_label = pokeBall._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')

    # test_medicine_item: memastikan bahwa item medicine ada
    def test_medicine_item(self):
        pokeBall = Item.objects.create(name='Potion', amount=10, description='Potion is a medicine')
        field_label = pokeBall._meta.get_field('name').verbose_name
        self.assertEqual(field_label, 'name')