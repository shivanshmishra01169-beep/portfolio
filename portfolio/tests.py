from django.test import TestCase
from django.urls import reverse

from .models import ContactMessage, Project


class PortfolioTests(TestCase):
    def setUp(self):
        self.project = Project.objects.create(
            title="Demo", slug="demo", summary="A demo.", description="Line one.\n\nLine two.",
            tech="Django, HTMX", year=2025,
        )

    def test_home_lists_featured_projects(self):
        response = self.client.get(reverse("portfolio:home"))
        self.assertContains(response, "Demo")

    def test_project_detail(self):
        response = self.client.get(self.project.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "HTMX")

    def test_missing_project_is_404(self):
        response = self.client.get(reverse("portfolio:project_detail", args=["nope"]))
        self.assertEqual(response.status_code, 404)

    def test_contact_saves_message(self):
        response = self.client.post(
            reverse("portfolio:contact"),
            {"name": "Sam", "email": "sam@example.com", "message": "Hello"},
        )
        self.assertRedirects(response, reverse("portfolio:contact"))
        self.assertEqual(ContactMessage.objects.count(), 1)

    def test_contact_rejects_bad_email(self):
        response = self.client.post(
            reverse("portfolio:contact"), {"name": "Sam", "email": "nope", "message": "Hi"}
        )
        self.assertEqual(response.status_code, 200)
        self.assertEqual(ContactMessage.objects.count(), 0)

    def test_tech_list(self):
        self.assertEqual(self.project.tech_list, ["Django", "HTMX"])
