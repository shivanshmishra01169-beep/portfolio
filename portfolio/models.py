from django.db import models
from django.urls import reverse


class Skill(models.Model):
    class Category(models.TextChoices):
        BACKEND = "backend", "Backend"
        FRONTEND = "frontend", "Frontend"
        TOOLING = "tooling", "Tooling"

    name = models.CharField(max_length=60)
    category = models.CharField(max_length=20, choices=Category.choices)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["category", "order", "name"]

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    summary = models.CharField(max_length=200, help_text="One line shown in the project list.")
    description = models.TextField(help_text="Shown on the project page. Blank lines start new paragraphs.")
    tech = models.CharField(max_length=200, help_text="Comma-separated, e.g. Django, PostgreSQL, HTMX")
    year = models.PositiveSmallIntegerField()
    repo_url = models.URLField(blank=True)
    live_url = models.URLField(blank=True)
    featured = models.BooleanField(default=True)
    order = models.PositiveSmallIntegerField(default=0)

    class Meta:
        ordering = ["order", "-year"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("portfolio:project_detail", args=[self.slug])

    @property
    def tech_list(self):
        return [t.strip() for t in self.tech.split(",") if t.strip()]


class ContactMessage(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField(max_length=4000)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.name} ({self.created:%Y-%m-%d})"
