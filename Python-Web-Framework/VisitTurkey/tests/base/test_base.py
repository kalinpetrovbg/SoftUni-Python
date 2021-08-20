from django.contrib.auth import get_user_model
from django.test import TestCase, Client

UserModel = get_user_model()


class PlacesTestCase(TestCase):
    email = 'kalin15@abv.bg'
    password = 'ZZgg105%1'

    def assertListEmpty(self, ll):
        return self.assertEqual([], ll, 'The list is not empty.')

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.email,
            password=self.password,
        )
        self.super_user = UserModel.objects.create_superuser(
            email='kalin16@abv.bg',
            password='ZZgg105%1',
        )


class MainTestCase(TestCase):
    EMAIL = 'kalin41494@gmail.com'
    PASSWORD = 'fas7qwe12987'

    def setUp(self):
        self.user = UserModel.objects.create_user(
            email=MainTestCase.EMAIL,
            password=MainTestCase.PASSWORD,
        )
        self.user.is_active = True
        self.user.save()

    def tearDown(self):
        self.user.delete()
