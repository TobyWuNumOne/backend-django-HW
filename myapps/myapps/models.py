from django.db import models
from django.contrib.auth.models import AbstractUser
from decimal import Decimal


class User(models.Model):
    """使用者基礎資料表"""

    name = models.CharField(max_length=100, verbose_name="姓名")
    account = models.CharField(max_length=50, unique=True, verbose_name="帳號")
    password = models.CharField(max_length=255, verbose_name="密碼")

    ROLE_CHOICES = [
        ("teacher", "教師"),
        ("student", "學生"),
        ("admin", "管理員"),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, verbose_name="角色")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")

    class Meta:
        verbose_name = "使用者"
        verbose_name_plural = "使用者"
        db_table = "users"

    def __str__(self):
        return f"{self.name} ({self.account})"


class Teacher(models.Model):
    """教師資料表"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="使用者")
    avatar = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="頭像"
    )
    name = models.CharField(max_length=100, verbose_name="姓名")
    email = models.EmailField(verbose_name="電子郵件")
    phone = models.CharField(max_length=20, verbose_name="電話")

    GENDER_CHOICES = [
        ("M", "男性"),
        ("F", "女性"),
        ("O", "其他"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="性別")
    age = models.CharField(max_length=10, verbose_name="年齡")
    education = models.CharField(
        max_length=255, blank=True, null=True, verbose_name="學歷"
    )
    certifications = models.CharField(
        max_length=500, blank=True, null=True, verbose_name="證照"
    )
    intro = models.CharField(
        max_length=1000, blank=True, null=True, verbose_name="自我介紹"
    )
    teaching_experience = models.TextField(
        blank=True, null=True, verbose_name="教學經驗"
    )

    STATUS_CHOICES = [
        ("active", "活躍"),
        ("inactive", "非活躍"),
        ("suspended", "暫停"),
    ]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, verbose_name="狀態"
    )
    blue_premium = models.BooleanField(default=False, verbose_name="藍鑽會員")

    class Meta:
        verbose_name = "教師"
        verbose_name_plural = "教師"
        db_table = "teachers"

    def __str__(self):
        return self.name


class Student(models.Model):
    """學生資料表"""

    user = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name="使用者")
    email = models.EmailField(verbose_name="電子郵件")

    GENDER_CHOICES = [
        ("M", "男性"),
        ("F", "女性"),
        ("O", "其他"),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, verbose_name="性別")
    age = models.CharField(max_length=10, verbose_name="年齡")

    class Meta:
        verbose_name = "學生"
        verbose_name_plural = "學生"
        db_table = "students"

    def __str__(self):
        return f"{self.user.name} (學生)"


class Course(models.Model):
    """課程資料表"""

    subject = models.CharField(max_length=200, verbose_name="科目")
    teacher = models.ForeignKey(Teacher, on_delete=models.CASCADE, verbose_name="教師")
    description = models.TextField(blank=True, null=True, verbose_name="課程描述")
    price = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="價格")
    location = models.CharField(max_length=255, verbose_name="上課地點")
    avg_rating = models.FloatField(
        default=0.0, blank=True, null=True, verbose_name="平均評分"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")

    class Meta:
        verbose_name = "課程"
        verbose_name_plural = "課程"
        db_table = "courses"

    def __str__(self):
        return f"{self.subject} - {self.teacher.name}"


class Booking(models.Model):
    """預約資料表"""

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="課程")
    student = models.ForeignKey(Student, on_delete=models.CASCADE, verbose_name="學生")
    schedule_date = models.CharField(max_length=100, verbose_name="預約時間")

    STATUS_CHOICES = [
        ("pending", "待確認"),
        ("confirmed", "已確認"),
        ("completed", "已完成"),
        ("cancelled", "已取消"),
    ]
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, verbose_name="狀態"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")

    class Meta:
        verbose_name = "預約"
        verbose_name_plural = "預約"
        db_table = "bookings"

    def __str__(self):
        return f"{self.student.user.name} - {self.course.subject}"


class Review(models.Model):
    """評價資料表"""

    course = models.ForeignKey(Course, on_delete=models.CASCADE, verbose_name="課程")
    rating = models.CharField(max_length=10, verbose_name="評分")
    comment = models.CharField(
        max_length=1000, blank=True, null=True, verbose_name="評論"
    )
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="建立時間")

    class Meta:
        verbose_name = "評價"
        verbose_name_plural = "評價"
        db_table = "reviews"

    def __str__(self):
        return f"{self.course.subject} - 評分: {self.rating}"
