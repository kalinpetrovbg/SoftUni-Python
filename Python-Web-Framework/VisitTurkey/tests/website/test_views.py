from tests.base.test_base import PlacesTestCase


class HomePageTests(PlacesTestCase):

    def test_if_home_page_opens_with_200_code(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateNotUsed(response, 'testing/home_page.html')
