from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.test import Client
from django.urls import reverse

from VisitTurkey.profiles.models import Profile
from tests.base.test_base import PlacesTestCase

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

    def test__if_profile_exists(self):
        self.assertIsNotNone(self.profile)

    def test_getDetails_whenLoggedInUser_shouldGetDetails(self):
        self.client.force_login(self.user)
        self.my_regular_group = Group.objects.get(name="Regular user")
        self.profile = Profile.objects.get(pk=self.user.id)

        response = self.client.get(reverse('profile info'))

        profile = response.context['profile']
        self.assertEqual(self.user.id, profile.user_id)
