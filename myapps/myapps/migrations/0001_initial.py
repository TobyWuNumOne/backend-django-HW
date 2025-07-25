# Generated by Django 5.2.4 on 2025-07-22 13:09

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Course",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("subject", models.CharField(max_length=200, verbose_name="科目")),
                (
                    "description",
                    models.TextField(blank=True, null=True, verbose_name="課程描述"),
                ),
                (
                    "price",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="價格"
                    ),
                ),
                ("location", models.CharField(max_length=255, verbose_name="上課地點")),
                (
                    "avg_rating",
                    models.FloatField(
                        blank=True, default=0.0, null=True, verbose_name="平均評分"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="建立時間"),
                ),
            ],
            options={
                "verbose_name": "課程",
                "verbose_name_plural": "課程",
                "db_table": "courses",
            },
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("email", models.EmailField(max_length=254, verbose_name="電子郵件")),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "男性"), ("F", "女性"), ("O", "其他")],
                        max_length=1,
                        verbose_name="性別",
                    ),
                ),
                ("age", models.CharField(max_length=10, verbose_name="年齡")),
            ],
            options={
                "verbose_name": "學生",
                "verbose_name_plural": "學生",
                "db_table": "students",
            },
        ),
        migrations.CreateModel(
            name="Teacher",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "avatar",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="頭像"
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="姓名")),
                ("email", models.EmailField(max_length=254, verbose_name="電子郵件")),
                ("phone", models.CharField(max_length=20, verbose_name="電話")),
                (
                    "gender",
                    models.CharField(
                        choices=[("M", "男性"), ("F", "女性"), ("O", "其他")],
                        max_length=1,
                        verbose_name="性別",
                    ),
                ),
                ("age", models.CharField(max_length=10, verbose_name="年齡")),
                (
                    "education",
                    models.CharField(
                        blank=True, max_length=255, null=True, verbose_name="學歷"
                    ),
                ),
                (
                    "certifications",
                    models.CharField(
                        blank=True, max_length=500, null=True, verbose_name="證照"
                    ),
                ),
                (
                    "intro",
                    models.CharField(
                        blank=True, max_length=1000, null=True, verbose_name="自我介紹"
                    ),
                ),
                (
                    "teaching_experience",
                    models.TextField(blank=True, null=True, verbose_name="教學經驗"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("active", "活躍"),
                            ("inactive", "非活躍"),
                            ("suspended", "暫停"),
                        ],
                        max_length=20,
                        verbose_name="狀態",
                    ),
                ),
                (
                    "blue_premium",
                    models.BooleanField(default=False, verbose_name="藍鑽會員"),
                ),
            ],
            options={
                "verbose_name": "教師",
                "verbose_name_plural": "教師",
                "db_table": "teachers",
            },
        ),
        migrations.CreateModel(
            name="User",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100, verbose_name="姓名")),
                (
                    "account",
                    models.CharField(max_length=50, unique=True, verbose_name="帳號"),
                ),
                ("password", models.CharField(max_length=255, verbose_name="密碼")),
                (
                    "role",
                    models.CharField(
                        choices=[
                            ("teacher", "教師"),
                            ("student", "學生"),
                            ("admin", "管理員"),
                        ],
                        max_length=20,
                        verbose_name="角色",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="建立時間"),
                ),
            ],
            options={
                "verbose_name": "使用者",
                "verbose_name_plural": "使用者",
                "db_table": "users",
            },
        ),
        migrations.CreateModel(
            name="Review",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("rating", models.CharField(max_length=10, verbose_name="評分")),
                (
                    "comment",
                    models.CharField(
                        blank=True, max_length=1000, null=True, verbose_name="評論"
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="建立時間"),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapps.course",
                        verbose_name="課程",
                    ),
                ),
            ],
            options={
                "verbose_name": "評價",
                "verbose_name_plural": "評價",
                "db_table": "reviews",
            },
        ),
        migrations.CreateModel(
            name="Booking",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "schedule_date",
                    models.CharField(max_length=100, verbose_name="預約時間"),
                ),
                (
                    "status",
                    models.CharField(
                        choices=[
                            ("pending", "待確認"),
                            ("confirmed", "已確認"),
                            ("completed", "已完成"),
                            ("cancelled", "已取消"),
                        ],
                        max_length=20,
                        verbose_name="狀態",
                    ),
                ),
                (
                    "created_at",
                    models.DateTimeField(auto_now_add=True, verbose_name="建立時間"),
                ),
                (
                    "course",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapps.course",
                        verbose_name="課程",
                    ),
                ),
                (
                    "student",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="myapps.student",
                        verbose_name="學生",
                    ),
                ),
            ],
            options={
                "verbose_name": "預約",
                "verbose_name_plural": "預約",
                "db_table": "bookings",
            },
        ),
        migrations.AddField(
            model_name="course",
            name="teacher",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="myapps.teacher",
                verbose_name="教師",
            ),
        ),
        migrations.AddField(
            model_name="teacher",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="myapps.user",
                verbose_name="使用者",
            ),
        ),
        migrations.AddField(
            model_name="student",
            name="user",
            field=models.OneToOneField(
                on_delete=django.db.models.deletion.CASCADE,
                to="myapps.user",
                verbose_name="使用者",
            ),
        ),
    ]
