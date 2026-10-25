from django.core.management.base import BaseCommand

from portfolio.models import Project, Skill

PROJECTS = [
    {
        "slug": "ledgerly",
        "title": "Ledgerly",
        "summary": "Expense splitting for shared flats, with monthly settle-up.",
        "tech": "Django, PostgreSQL, HTMX",
        "year": 2025,
        "order": 1,
        "description": (
            "Housemates kept losing track of who paid for what. Ledgerly records shared "
            "expenses and works out the smallest set of payments that settles everyone up.\n\n"
            "The settle-up logic is a plain Python module with full test coverage, so it can be "
            "reused outside Django. Pages update with HTMX, so there is almost no custom JavaScript."
        ),
    },
    {
        "slug": "fieldnotes",
        "title": "Fieldnotes",
        "summary": "Markdown notes with fast full-text search.",
        "tech": "Django, SQLite FTS5, Alpine.js",
        "year": 2024,
        "order": 2,
        "description": (
            "A personal notes app that stays fast with thousands of entries. Search uses SQLite's "
            "FTS5 index, kept in sync with database triggers.\n\n"
            "Notes are stored as Markdown and rendered on the server, then sanitized before display."
        ),
    },
    {
        "slug": "queue-board",
        "title": "Queue Board",
        "summary": "A triage dashboard for support tickets.",
        "tech": "Django REST framework, Celery, Redis",
        "year": 2024,
        "order": 3,
        "description": (
            "Support leads needed to see which tickets were about to breach their response time. "
            "Queue Board pulls tickets from a helpdesk API on a schedule and ranks them by urgency.\n\n"
            "Background jobs run on Celery, and a small REST API feeds the dashboard."
        ),
    },
    {
        "slug": "trailhead-api",
        "title": "Trailhead API",
        "summary": "A public REST API for hiking trail data.",
        "tech": "Django REST framework, PostGIS",
        "year": 2023,
        "order": 4,
        "description": (
            "An open API that returns trails near a point, filtered by length and difficulty. "
            "Geographic queries run in PostGIS.\n\n"
            "The API is versioned, rate limited, and documented with an OpenAPI schema."
        ),
    },
]

SKILLS = [
    ("Python", "backend"), ("Django", "backend"), ("Django REST framework", "backend"),
    ("PostgreSQL", "backend"), ("Celery", "backend"),
    ("HTML and CSS", "frontend"), ("HTMX", "frontend"), ("JavaScript", "frontend"),
    ("Git", "tooling"), ("Docker", "tooling"), ("pytest", "tooling"), ("GitHub Actions", "tooling"),
]


class Command(BaseCommand):
    help = "Load sample projects and skills. Safe to run more than once."

    def handle(self, *args, **options):
        for data in PROJECTS:
            slug = data.pop("slug")
            Project.objects.update_or_create(slug=slug, defaults=data)
            data["slug"] = slug

        for order, (name, category) in enumerate(SKILLS):
            Skill.objects.update_or_create(name=name, defaults={"category": category, "order": order})

        self.stdout.write(self.style.SUCCESS(f"Loaded {len(PROJECTS)} projects and {len(SKILLS)} skills."))
