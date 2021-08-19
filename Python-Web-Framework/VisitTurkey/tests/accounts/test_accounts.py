from django.contrib.auth import get_user_model
from django.test import TestCase

from VisitTurkey.accounts.forms import SignUpForm

UserModel = get_user_model()


class RegisterUser(TestCase):

    def test_valid_userdata_creates_an_user(self):
        user_form = SignUpForm(
            {'email': 'kalin5@abv.bg',
             'password1': 'ZZgg105%1',
             'password2': 'ZZgg105%1', }
        )
        self.assertTrue(user_form.is_valid())

    def test_invalid_userdata_throws_an_error(self):
        user_form = SignUpForm(
            {'email': 'kalin5@abv.bg',
             'password1': 'ZZgg105%1',
             'password2': 'ZZgg105%16366', }
        )
        self.assertFalse(user_form.is_valid(), msg='Please enter same password twice.')

    def test_invalid_user_email_throws_an_error(self):
        user_form = SignUpForm(
            {'email': 'kalin',
             'password1': 'ZZgg105%1',
             'password2': 'ZZgg105%1', }
        )
        self.assertFalse(user_form.is_valid(), msg='Please enter a valid email address.')

    def test_too_short_user_password_throws_an_error(self):
        user_form = SignUpForm(
            {'email': 'kalin5@abv.bg',
             'password1': 'No1',
             'password2': 'No1', }
        )
        self.assertFalse(user_form.is_valid(), msg='This password is too short. It must contain at least 8 characters.')

    def test_numeric_only_user_password_throws_an_error(self):
        user_form = SignUpForm(
            {'email': 'kalin5@abv.bg',
             'password1': '00001111',
             'password2': '00001111', }
        )
        self.assertFalse(user_form.is_valid(), msg='This password is entirely numeric.')


class CreateUserPrivileges(TestCase):
    def test_valid_userdata_creates_normal_user(self):
        quote_user = UserModel.objects.create_user(email='kalin5@abv.bg', password='ZZgg105%1')

        self.assertEquals(False, quote_user.is_staff)
        self.assertEquals('kalin5@abv.bg', quote_user.email)

    def test_valid_userdata_creates_super_user(self):
        quote_user = UserModel.objects.create_superuser(email='kalin5@abv.bg', password='ZZgg105%1')

        self.assertEqual(True, quote_user.is_staff)
        self.assertEquals('kalin5@abv.bg', quote_user.email)
