from django.conf import settings
from django.test import SimpleTestCase
from django.urls import reverse

from tailwind import get_config


class TailwindSetupTests(SimpleTestCase):
    def test_uses_django_tailwind_in_standalone_mode(self):
        # The theme app has no package.json, so Node.js must never be required.
        self.assertEqual(get_config("TAILWIND_APP_NAME"), "theme")
        self.assertTrue(get_config("TAILWIND_USE_STANDALONE_BINARY"))

    def test_home_links_generated_stylesheet(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(
            response,
            f'href="{settings.STATIC_URL}css/dist/styles.css',
        )
