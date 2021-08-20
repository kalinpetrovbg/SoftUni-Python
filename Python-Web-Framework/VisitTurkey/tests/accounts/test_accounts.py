from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse

from VisitTurkey.accounts.forms import SignUpForm
from tests.base.test_base import MainTestCase

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


class LogOutViewTest(MainTestCase):
    def tearDown(self):
        self.user.delete()

    def test_send_to_index_after_successful_sign_out(self):
        is_logged_in = self.client.login(username=self.EMAIL, password=self.PASSWORD)
        self.assertTrue(is_logged_in)
        response = self.client.get(reverse('log out'), follow=False)
        self.assertEqual(302, response.status_code)
        self.assertEqual(reverse('home page'), response.headers['location'])


class SignInViewTest(MainTestCase):
    def test_successful_log_in_should_redirect_to_home_page(self):
        response = self.client.post(reverse('log in'), data={'username': 'kalin41494@gmail.com', 'password': 'fas7qwe12987'})
        self.assertEqual(302, response.status_code)
        self.assertEqual('/', response.headers['location'])

    def test_wrong_username(self):
        response = self.client.post(reverse('log in'), {'username': 'wrong', 'password': 'fas7qwe12987'})
        self.assertEqual(200, response.status_code)
        errors = response.context_data['form'].errors['password']
        default_error = 'Please enter a correct email and password. Note that both fields may be case-sensitive.'
        self.assertIn(default_error, errors)

    def test_wrong_password(self):
        response = self.client.post(reverse('log in'), {'username': 'kalin41494@gmail.com', 'password': 'wrong'})
        self.assertEqual(200, response.status_code)
        errors = response.context_data['form'].errors['password']
        default_error = 'Please enter a correct email and password. Note that both fields may be case-sensitive.'
        self.assertIn(default_error, errors)


class RegisterViewTest(TestCase):
    def test_register_should_render_correct_template_and_form(self):
        response = self.client.get(reverse('register'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='accounts/register.html')
        self.assertIsInstance(response.context_data['form'], SignUpForm)
