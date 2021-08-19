from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from tests.base.test_base import PlacesTestCase

UserModel = get_user_model()
from VisitTurkey.profiles.models import Profile


class HomePageTests(PlacesTestCase):

    def test_if_home_page_opens_with_200_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'testing/home_page.html')


class PlaceTestCase(TestCase):
    logged_in_user_email = 'kalin33q5@abv.bg'
    logged_in_user_password = 'bb24fasa4'

    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )
        profile = Profile(
            user=self.user,
        )
        profile.save()


class ProfileDetailsTest(PlaceTestCase):
    def setUp(self):
        self.client = Client()
        self.user = UserModel.objects.create_user(
            email=self.logged_in_user_email,
            password=self.logged_in_user_password,
        )
        profile = Profile(
            user=self.user,
        )
        profile.save()

    def test_see_profile_details_when_logged_in(self):
        self.client.force_login(self.user)
        response = self.client.get(reverse('profile info'))
        self.assertEqual(self.user.id, response.context['profile'].user_id)

