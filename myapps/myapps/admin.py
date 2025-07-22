from django.contrib import admin
from .models import User, Teacher, Student, Course, Booking, Review


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["name", "account", "role", "created_at"]
    list_filter = ["role", "created_at"]
    search_fields = ["name", "account"]
    ordering = ["-created_at"]


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ["name", "email", "phone", "gender", "status", "blue_premium"]
    list_filter = ["gender", "status", "blue_premium"]
    search_fields = ["name", "email"]
    ordering = ["name"]


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ["user", "email", "gender", "age"]
    list_filter = ["gender"]
    search_fields = ["user__name", "email"]
    ordering = ["user__name"]


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = [
        "subject",
        "teacher",
        "price",
        "location",
        "avg_rating",
        "created_at",
    ]
    list_filter = ["teacher", "created_at"]
    search_fields = ["subject", "teacher__name"]
    ordering = ["-created_at"]


@admin.register(Booking)
class BookingAdmin(admin.ModelAdmin):
    list_display = ["course", "student", "schedule_date", "status", "created_at"]
    list_filter = ["status", "created_at"]
    search_fields = ["course__subject", "student__user__name"]
    ordering = ["-created_at"]


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ["course", "rating", "created_at"]
    list_filter = ["rating", "created_at"]
    search_fields = ["course__subject", "comment"]
    ordering = ["-created_at"]
