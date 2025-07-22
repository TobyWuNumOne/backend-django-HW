from rest_framework import viewsets, status
from rest_framework.decorators import api_view, action
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.shortcuts import get_object_or_404
from django.db.models import Q

from .models import User, Teacher, Student, Course, Booking, Review
from .serializers import (
    UserSerializer,
    TeacherSerializer,
    StudentSerializer,
    CourseSerializer,
    BookingSerializer,
    ReviewSerializer,
    TeacherListSerializer,
    CourseListSerializer,
)


# API 概覽視圖
@api_view(["GET"])
def api_overview(request):
    """API 概覽"""
    data = {
        "message": "歡迎使用教學平台 API",
        "version": "1.0",
        "endpoints": {
            "users": {
                "list": "GET /api/users/",
                "create": "POST /api/users/",
                "detail": "GET /api/users/{id}/",
                "update": "PUT /api/users/{id}/",
                "delete": "DELETE /api/users/{id}/",
            },
            "teachers": {
                "list": "GET /api/teachers/",
                "create": "POST /api/teachers/",
                "detail": "GET /api/teachers/{id}/",
                "update": "PUT /api/teachers/{id}/",
                "delete": "DELETE /api/teachers/{id}/",
                "search": "GET /api/teachers/search/?q=keyword",
            },
            "students": {
                "list": "GET /api/students/",
                "create": "POST /api/students/",
                "detail": "GET /api/students/{id}/",
                "update": "PUT /api/students/{id}/",
                "delete": "DELETE /api/students/{id}/",
            },
            "courses": {
                "list": "GET /api/courses/",
                "create": "POST /api/courses/",
                "detail": "GET /api/courses/{id}/",
                "update": "PUT /api/courses/{id}/",
                "delete": "DELETE /api/courses/{id}/",
                "by_teacher": "GET /api/courses/by_teacher/{teacher_id}/",
            },
            "bookings": {
                "list": "GET /api/bookings/",
                "create": "POST /api/bookings/",
                "detail": "GET /api/bookings/{id}/",
                "update": "PUT /api/bookings/{id}/",
                "delete": "DELETE /api/bookings/{id}/",
            },
            "reviews": {
                "list": "GET /api/reviews/",
                "create": "POST /api/reviews/",
                "detail": "GET /api/reviews/{id}/",
                "update": "PUT /api/reviews/{id}/",
                "delete": "DELETE /api/reviews/{id}/",
            },
        },
    }
    return Response(data)


class UserViewSet(viewsets.ModelViewSet):
    """使用者 CRUD ViewSet"""

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = User.objects.all()
        role = self.request.query_params.get("role", None)
        if role is not None:
            queryset = queryset.filter(role=role)
        return queryset.order_by("-created_at")


class TeacherViewSet(viewsets.ModelViewSet):
    """教師 CRUD ViewSet"""

    queryset = Teacher.objects.select_related("user").all()
    serializer_class = TeacherSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == "list":
            return TeacherListSerializer
        return TeacherSerializer

    def get_queryset(self):
        queryset = Teacher.objects.select_related("user").all()
        status_filter = self.request.query_params.get("status", None)
        if status_filter is not None:
            queryset = queryset.filter(status=status_filter)
        return queryset.order_by("name")

    @action(detail=False, methods=["get"])
    def search(self, request):
        """搜尋教師"""
        query = request.query_params.get("q", "")
        if query:
            teachers = Teacher.objects.filter(
                Q(name__icontains=query)
                | Q(email__icontains=query)
                | Q(intro__icontains=query)
            ).select_related("user")
            serializer = TeacherListSerializer(teachers, many=True)
            return Response(serializer.data)
        return Response([])


class StudentViewSet(viewsets.ModelViewSet):
    """學生 CRUD ViewSet"""

    queryset = Student.objects.select_related("user").all()
    serializer_class = StudentSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        return Student.objects.select_related("user").order_by("user__name")


class CourseViewSet(viewsets.ModelViewSet):
    """課程 CRUD ViewSet"""

    queryset = Course.objects.select_related("teacher").all()
    serializer_class = CourseSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == "list":
            return CourseListSerializer
        return CourseSerializer

    def get_queryset(self):
        queryset = Course.objects.select_related("teacher").all()
        teacher_id = self.request.query_params.get("teacher_id", None)
        if teacher_id is not None:
            queryset = queryset.filter(teacher_id=teacher_id)
        return queryset.order_by("-created_at")

    @action(detail=False, methods=["get"], url_path="by_teacher/(?P<teacher_id>[^/.]+)")
    def by_teacher(self, request, teacher_id=None):
        """根據教師 ID 獲取課程"""
        courses = Course.objects.filter(teacher_id=teacher_id).select_related("teacher")
        serializer = CourseListSerializer(courses, many=True)
        return Response(serializer.data)


class BookingViewSet(viewsets.ModelViewSet):
    """預約 CRUD ViewSet"""

    queryset = Booking.objects.select_related(
        "course", "student", "course__teacher"
    ).all()
    serializer_class = BookingSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Booking.objects.select_related(
            "course", "student", "course__teacher"
        ).all()
        status_filter = self.request.query_params.get("status", None)
        student_id = self.request.query_params.get("student_id", None)
        course_id = self.request.query_params.get("course_id", None)

        if status_filter is not None:
            queryset = queryset.filter(status=status_filter)
        if student_id is not None:
            queryset = queryset.filter(student_id=student_id)
        if course_id is not None:
            queryset = queryset.filter(course_id=course_id)

        return queryset.order_by("-created_at")


class ReviewViewSet(viewsets.ModelViewSet):
    """評價 CRUD ViewSet"""

    queryset = Review.objects.select_related("course", "course__teacher").all()
    serializer_class = ReviewSerializer
    permission_classes = [AllowAny]

    def get_queryset(self):
        queryset = Review.objects.select_related("course", "course__teacher").all()
        course_id = self.request.query_params.get("course_id", None)
        if course_id is not None:
            queryset = queryset.filter(course_id=course_id)
        return queryset.order_by("-created_at")

    def create(self, request, *args, **kwargs):
        """建立評價並更新課程平均評分"""
        response = super().create(request, *args, **kwargs)
        if response.status_code == status.HTTP_201_CREATED:
            # 更新課程平均評分
            course_id = request.data.get("course")
            if course_id:
                course = Course.objects.get(id=course_id)
                reviews = Review.objects.filter(course=course)
                if reviews.exists():
                    avg_rating = (
                        sum(float(review.rating) for review in reviews)
                        / reviews.count()
                    )
                    course.avg_rating = round(avg_rating, 2)
                    course.save()
        return response
