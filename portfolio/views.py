from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from .forms import ContactForm
from .models import Project, Skill


def home(request):
    skills_by_category = {}
    for skill in Skill.objects.all():
        skills_by_category.setdefault(skill.get_category_display(), []).append(skill)

    return render(
        request,
        "portfolio/home.html",
        {
            "projects": Project.objects.filter(featured=True),
            "skills_by_category": skills_by_category,
        },
    )


def project_detail(request, slug):
    project = get_object_or_404(Project, slug=slug)
    return render(request, "portfolio/project_detail.html", {"project": project})


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Message sent. I'll reply within a few days.")
            return redirect("portfolio:contact")
    else:
        form = ContactForm()
    return render(request, "portfolio/contact.html", {"form": form})
