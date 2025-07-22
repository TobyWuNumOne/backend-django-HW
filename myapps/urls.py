"""
URL configuration for myapps project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include, re_path
from rest_framework.routers import DefaultRouter
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from myapps.myapps import views

# 建立 Swagger 文檔配置
schema_view = get_schema_view(
    openapi.Info(
        title="教學平台 API",
        default_version="v1",
        description="""
# 教學平台後端 API 文檔

這是一個功能完整的教學平台後端 API，提供以下主要功能：

## 🎯 主要功能
- 👤 **使用者管理**: 完整的使用者 CRUD 操作
- 👨‍🏫 **教師管理**: 教師資料管理、搜尋與篩選
- 👨‍🎓 **學生管理**: 學生資料管理
- 📚 **課程管理**: 課程建立、更新、查詢
- 📝 **預約系統**: 學生課程預約管理
- ⭐ **評價系統**: 課程評價與自動評分

## 🔧 技術特色
- RESTful API 設計
- 自動分頁功能
- 智能搜尋與篩選
- CORS 跨域支援
- 完整的錯誤處理
- 關聯資料自動載入

## 🚀 快速開始
1. 建立使用者 (Users)
2. 建立教師/學生資料
3. 建立課程
4. 進行預約
5. 新增評價
        """,
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(
            name="API 支援團隊",
            email="support@example.com",
            url="https://www.example.com/contact/",
        ),
        license=openapi.License(
            name="MIT License", url="https://opensource.org/licenses/MIT"
        ),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

# 建立 DRF 路由器
router = DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"teachers", views.TeacherViewSet)
router.register(r"students", views.StudentViewSet)
router.register(r"courses", views.CourseViewSet)
router.register(r"bookings", views.BookingViewSet)
router.register(r"reviews", views.ReviewViewSet)

urlpatterns = [
    # 管理介面
    path("admin/", admin.site.urls),
    # API 文檔 - Swagger
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    path(
        "swagger/",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    # API 端點
    path("api/", views.api_overview, name="api_overview"),
    path("api/", include(router.urls)),
    # DRF 瀏覽式 API 認證
    path("api-auth/", include("rest_framework.urls")),
]
