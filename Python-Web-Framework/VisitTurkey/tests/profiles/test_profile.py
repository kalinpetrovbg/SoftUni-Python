from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import Client, TestCase
from django.urls import reverse

from VisitTurkey.profiles.forms import ProfileForm
from VisitTurkey.profiles.models import Profile
from tests.base.test_base import PlacesTestCase, MainTestCase

UserModel = get_user_model()


class ProfileDetailsTest(PlacesTestCase):
    def setUp(self) -> None:
        group_name = "Regular user"
        self.my_regular_group = Group(name=group_name)
        self.my_regular_group.save()

        self.client = Client()
        self.user = UserModel.objects.create_user(email='kalin22@abv.bg', password='4124kaslf')
        self.my_regular_group = Group.objects.get(name="Regular user")
        self.profile = Profile.objects.get(pk=self.user.id)

    def test_if_profile_exists(self):
        self.assertIsNotNone(self.profile)

    def test_exist_group(self):
        self.assertIsNotNone(self.my_regular_group)

    def test_user_not_in_group(self):
        self.assertIsNotNone(self.my_regular_group.user_set)
        is_in_group = self.user.groups.filter(name="Regular user").exists()
        self.assertFalse(is_in_group)

    def test_get_profile_details(self):
        self.client.force_login(self.user)
        self.my_regular_group = Group.objects.get(name="Regular user")
        self.profile = Profile.objects.get(pk=self.user.id)

        response = self.client.get(reverse('profile info'))
        profile = response.context['profile']
        self.assertEqual(self.user.id, profile.user_id)


class ProfileModelTest(TestCase):
    def create_regular_user(self):
        user = UserModel.objects.create_user(email='kalin194@gmail.com')
        user.set_password = '4gg5das90251'
        user.save()
        return user

    def test_profile_created_with_user_creation(self):
        user = self.create_regular_user()
        profile = user.profile
        profile_db = Profile.objects.first()
        self.assertEqual(profile_db.pk, profile.pk)
        self.assertIn(profile.first_name, user.email)
        self.assertEqual('', profile.first_name)
        self.assertEqual('', profile.last_name)


class ProfileDetailsTestSecond(MainTestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.EMAIL,
            password=self.PASSWORD,
        )
        profile = Profile(
            user=self.user,
        )
        profile.save()

    def test_get_correct_profile_details(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile info'))
        self.assertEqual(self.user.id, response.context['profile'].user_id)


class ProfileModelTestSecond(TestCase):

    def test_profile_model_when_valid_expect_nothing(self):
        user = UserModel.objects.create(email='kalin491@gmail.com', password='41f2fs23f4')
        profile = Profile(
            user=user,
        )

        profile.save()
        self.assertEqual(profile.first_name, '')
        self.assertEqual(profile.last_name, '')
        self.assertEqual(profile.age, None)
        self.assertEqual(profile.is_complete, False)

    def test_when_profile_age_is_negative_raise_error(self):
        user = UserModel.objects.create(email='kalin491@gmail.com', password='41f2fs23f4')
        profile = Profile(
            user=user,
        )
        profile.save()
        profile_form = ProfileForm(
            {'first_name': 'Kalin',
             'last_name': 'Petrov',
             'age': '-30',
             'city': 'Sofia',
             }
        )
        self.assertFalse(profile_form.is_valid())


class TestDeleteProfile(MainTestCase):
    def test_delete_account_view(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('delete profile'))
        self.assertEqual(response.status_code, 200)

    def test_successful_delete_account(self):
        self.client.force_login(self.user)
        response = self.client.post(reverse('home page'))
        self.assertEqual(response.status_code, 200)