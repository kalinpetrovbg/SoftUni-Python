from django.contrib.auth import get_user_model
from django.test import Client
from django.urls import reverse

from tests.website.test_views import PlaceTestCase

UserModel = get_user_model()
from VisitTurkey.profiles.models import Profile


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
