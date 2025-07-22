from rest_framework import serializers
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import User, Teacher, Student, Course, Booking, Review


class UserSerializer(serializers.ModelSerializer):
    """
    使用者序列化器

    用於處理使用者資料的序列化和反序列化。
    支援建立、讀取、更新使用者資訊。
    """

    class Meta:
        model = User
        fields = ["id", "name", "account", "role", "created_at"]
        extra_kwargs = {
            "password": {"write_only": True},  # 密碼只能寫入，不能讀取
            "name": {"help_text": "使用者的真實姓名"},
            "account": {"help_text": "使用者的登入帳號，必須唯一"},
            "role": {
                "help_text": "使用者角色：teacher(教師)、student(學生)、admin(管理員)"
            },
        }

    def create(self, validated_data):
        """建立使用者時加密密碼"""
        password = validated_data.pop("password", None)
        user = User.objects.create(**validated_data)
        if password:
            user.password = password  # 在實際專案中應該使用密碼哈希
        user.save()
        return user


class TeacherSerializer(serializers.ModelSerializer):
    """
    教師序列化器

    用於處理教師資料的序列化和反序列化。
    包含教師基本資訊、聯繫方式、教學經驗等完整資料。
    """

    user_name = serializers.CharField(
        source="user.name", read_only=True, help_text="關聯使用者的姓名"
    )
    user_account = serializers.CharField(
        source="user.account", read_only=True, help_text="關聯使用者的帳號"
    )

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
        extra_kwargs = {
            "user": {"help_text": "關聯的使用者 ID"},
            "avatar": {"help_text": "教師頭像圖片 URL"},
            "name": {"help_text": "教師姓名"},
            "email": {"help_text": "教師電子郵件地址"},
            "phone": {"help_text": "教師聯繫電話"},
            "gender": {"help_text": "性別：M(男性)、F(女性)、O(其他)"},
            "age": {"help_text": "教師年齡"},
            "education": {"help_text": "教師學歷背景"},
            "certifications": {"help_text": "教師相關證照"},
            "intro": {"help_text": "教師自我介紹"},
            "teaching_experience": {"help_text": "教學經驗詳細描述"},
            "status": {
                "help_text": "教師狀態：active(活躍)、inactive(非活躍)、suspended(暫停)"
            },
            "blue_premium": {"help_text": "是否為藍鑽會員"},
        }


class StudentSerializer(serializers.ModelSerializer):
    """
    學生序列化器

    用於處理學生資料的序列化和反序列化。
    包含學生基本資訊和聯繫方式。
    """

    user_name = serializers.CharField(
        source="user.name", read_only=True, help_text="關聯使用者的姓名"
    )
    user_account = serializers.CharField(
        source="user.account", read_only=True, help_text="關聯使用者的帳號"
    )

    class Meta:
        model = Student
        fields = ["id", "user", "user_name", "user_account", "email", "gender", "age"]
        extra_kwargs = {
            "user": {"help_text": "關聯的使用者 ID"},
            "email": {"help_text": "學生電子郵件地址"},
            "gender": {"help_text": "性別：M(男性)、F(女性)、O(其他)"},
            "age": {"help_text": "學生年齡"},
        }


class CourseSerializer(serializers.ModelSerializer):
    """
    課程序列化器

    用於處理課程資料的序列化和反序列化。
    包含課程資訊、教師資訊、價格和評分等。
    """

    teacher_name = serializers.CharField(
        source="teacher.name", read_only=True, help_text="授課教師姓名"
    )
    teacher_email = serializers.CharField(
        source="teacher.email", read_only=True, help_text="授課教師電子郵件"
    )

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
        extra_kwargs = {
            "teacher": {"help_text": "授課教師 ID"},
            "subject": {"help_text": "課程科目名稱"},
            "description": {"help_text": "課程詳細描述"},
            "price": {"help_text": "課程價格（新台幣）"},
            "location": {"help_text": "上課地點"},
            "avg_rating": {"help_text": "課程平均評分（自動計算）", "read_only": True},
        }


class BookingSerializer(serializers.ModelSerializer):
    """
    預約序列化器

    用於處理預約資料的序列化和反序列化。
    包含預約資訊、課程資訊、學生資訊等。
    """

    course_subject = serializers.CharField(
        source="course.subject", read_only=True, help_text="預約課程科目"
    )
    student_name = serializers.CharField(
        source="student.user.name", read_only=True, help_text="預約學生姓名"
    )
    teacher_name = serializers.CharField(
        source="course.teacher.name", read_only=True, help_text="授課教師姓名"
    )

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
        extra_kwargs = {
            "course": {"help_text": "預約的課程 ID"},
            "student": {"help_text": "預約的學生 ID"},
            "schedule_date": {"help_text": "預約的上課時間"},
            "status": {
                "help_text": "預約狀態：pending(待確認)、confirmed(已確認)、completed(已完成)、cancelled(已取消)"
            },
        }


class ReviewSerializer(serializers.ModelSerializer):
    """
    評價序列化器

    用於處理評價資料的序列化和反序列化。
    包含評價內容、評分、相關課程資訊等。
    """

    course_subject = serializers.CharField(
        source="course.subject", read_only=True, help_text="評價課程科目"
    )
    teacher_name = serializers.CharField(
        source="course.teacher.name", read_only=True, help_text="授課教師姓名"
    )

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
        extra_kwargs = {
            "course": {"help_text": "評價的課程 ID"},
            "rating": {"help_text": "評分（1-5 分）"},
            "comment": {"help_text": "評價內容"},
        }


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
