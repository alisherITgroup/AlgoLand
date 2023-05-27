from django.contrib import admin
from .models import Lesson, Problem

@admin.register(Problem)
class ProblemModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]

@admin.register(Lesson)
class LessonModelAdmin(admin.ModelAdmin):
    list_display = ["name", "created_at", "updated_at"]
