from django.test import TestCase
from django.urls import reverse
from .models import Snack
from accounts.models import CustomUser

class SnacksViewsTests(TestCase):

    def setUp(self):
        # Create a test user
        self.user = CustomUser.objects.create_user(username='testuser', password='testpassword')

    def test_snack_detail_view(self):
        # Create a test Snack object
        snack = Snack.objects.create(name='Test Snack', desc='Test Description', purchaser=self.user)
        response = self.client.get(reverse('snack_detail', args=[snack.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "snacks/snack-detail.html")
        self.assertContains(response, "Test Snack")
        self.assertContains(response, "Test Description")
        self.assertContains(response, f"purcheser: {self.user}")  # Verify that the username is displayed in the response

