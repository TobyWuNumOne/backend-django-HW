from rest_framework import serializers
from .models import User, Teacher, Student, Course, Booking, Review


class UserSerializer(serializers.ModelSerializer):
    """使用者序列化器"""

    class Meta:
        model = User
        fields = ["id", "name", "account", "role", "created_at"]
        extra_kwargs = {"password": {"write_only": True}}  # 密碼只能寫入，不能讀取

    def create(self, validated_data):
        """建立使用者時加密密碼"""
        password = validated_data.pop("password", None)
        user = User.objects.create(**validated_data)
        if password:
            user.password = password  # 在實際專案中應該使用密碼哈希
        user.save()
        return user


class TeacherSerializer(serializers.ModelSerializer):
    """教師序列化器"""

    user_name = serializers.CharField(source="user.name", read_only=True)
    user_account = serializers.CharField(source="user.account", read_only=True)

    class Meta:
        model = Teacher
        fields = [
            "id",
            "user",
            "user_name",
            "user_account",
            "avatar",
            "name",
            "email",
            "phone",
            "gender",
            "age",
            "education",
            "certifications",
            "intro",
            "teaching_experience",
            "status",
            "blue_premium",
        ]


class StudentSerializer(serializers.ModelSerializer):
    """學生序列化器"""

    user_name = serializers.CharField(source="user.name", read_only=True)
    user_account = serializers.CharField(source="user.account", read_only=True)

    class Meta:
        model = Student
        fields = ["id", "user", "user_name", "user_account", "email", "gender", "age"]


class CourseSerializer(serializers.ModelSerializer):
    """課程序列化器"""

    teacher_name = serializers.CharField(source="teacher.name", read_only=True)
    teacher_email = serializers.CharField(source="teacher.email", read_only=True)

    class Meta:
        model = Course
        fields = [
            "id",
            "subject",
            "teacher",
            "teacher_name",
            "teacher_email",
            "description",
            "price",
            "location",
            "avg_rating",
            "created_at",
        ]


class BookingSerializer(serializers.ModelSerializer):
    """預約序列化器"""

    course_subject = serializers.CharField(source="course.subject", read_only=True)
    student_name = serializers.CharField(source="student.user.name", read_only=True)
    teacher_name = serializers.CharField(source="course.teacher.name", read_only=True)

    class Meta:
        model = Booking
        fields = [
            "id",
            "course",
            "course_subject",
            "student",
            "student_name",
            "teacher_name",
            "schedule_date",
            "status",
            "created_at",
        ]


class ReviewSerializer(serializers.ModelSerializer):
    """評價序列化器"""

    course_subject = serializers.CharField(source="course.subject", read_only=True)
    teacher_name = serializers.CharField(source="course.teacher.name", read_only=True)

    class Meta:
        model = Review
        fields = [
            "id",
            "course",
            "course_subject",
            "teacher_name",
            "rating",
            "comment",
            "created_at",
        ]


# 簡化版序列化器 (用於列表顯示)
class TeacherListSerializer(serializers.ModelSerializer):
    """教師列表序列化器 (簡化版)"""

    class Meta:
        model = Teacher
        fields = ["id", "name", "email", "phone", "status", "blue_premium"]


class CourseListSerializer(serializers.ModelSerializer):
    """課程列表序列化器 (簡化版)"""

    teacher_name = serializers.CharField(source="teacher.name", read_only=True)

    class Meta:
        model = Course
        fields = ["id", "subject", "teacher_name", "price", "location", "avg_rating"]
