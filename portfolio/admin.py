from django.contrib import admin

from .models import ContactMessage, Project, Skill


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "year", "featured", "order")
    list_editable = ("featured", "order")
    prepopulated_fields = {"slug": ("title",)}
    search_fields = ("title", "summary", "tech")


@admin.register(Skill)
class SkillAdmin(admin.ModelAdmin):
    list_display = ("name", "category", "order")
    list_editable = ("order",)
    list_filter = ("category",)


@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "created")
    readonly_fields = ("name", "email", "message", "created")
