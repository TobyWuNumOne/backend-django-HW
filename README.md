# 教學平台後端 API 專案

這是一個使用 Django + Django REST Framework 開發的教學平台後端 API，提供完整的 CRUD 操作功能。

## 🚀 快速開始

### 先決條件

-   Python 3.12+
-   [uv](https://docs.astral.sh/uv/) 套件管理工具

### 方式一：使用啟動腳本（推薦）

```bash
# 直接執行啟動腳本（自動處理所有設置）
./start.sh
```

### 方式二：手動設置

#### 1. 安裝依賴

```bash
# 同步專案依賴
uv sync
```

#### 2. 資料庫設置

```bash
# 建立資料庫遷移檔案 (如果尚未建立)
uv run python manage.py makemigrations

# 執行資料庫遷移
uv run python manage.py migrate

# 建立超級使用者 (可選)
uv run python manage.py createsuperuser
```

#### 3. 啟動開發服務器

```bash
# 啟動 Django 開發服務器
uv run python manage.py runserver
```

服務器將在 `http://127.0.0.1:8000/` 啟動。

## 📊 資料庫模型

### 已建立的資料表模型：

-   **Users** - 使用者基礎資料表
-   **Teachers** - 教師詳細資料表
-   **Students** - 學生資料表
-   **Courses** - 課程資料表
-   **Bookings** - 預約資料表
-   **Reviews** - 評價資料表

### 關聯關係：

-   `User` ↔ `Teacher` (一對一關係)
-   `User` ↔ `Student` (一對一關係)
-   `Teacher` ↔ `Course` (一對多關係)
-   `Course` ↔ `Booking` (一對多關係)
-   `Student` ↔ `Booking` (一對多關係)
-   `Course` ↔ `Review` (一對多關係)

## 🌐 API 端點

### 基本端點：

-   **管理後台**: `http://127.0.0.1:8000/admin/`
-   **API 概覽**: `http://127.0.0.1:8000/api/`
-   **瀏覽式 API**: `http://127.0.0.1:8000/api/{endpoint}/`

### 完整 CRUD 端點：

-   **使用者**: `/api/users/`
-   **教師**: `/api/teachers/`
-   **學生**: `/api/students/`
-   **課程**: `/api/courses/`
-   **預約**: `/api/bookings/`
-   **評價**: `/api/reviews/`

每個端點都支援：

-   `GET` - 獲取資料列表或單筆資料
-   `POST` - 建立新資料
-   `PUT` - 更新現有資料
-   `DELETE` - 刪除資料

## 📖 API 使用說明

詳細的 API 使用說明和範例，請參考：

### 👉 [完整 API 使用指南](./API_GUIDE.md)

API 指南包含：

-   📋 所有可用端點說明
-   💾 資料格式範例
-   🛠️ 使用方式 (curl、Python、瀏覽器)
-   🔍 進階功能 (搜尋、篩選、分頁)
-   🎯 測試建議

## 🧪 API 測試

### 使用測試腳本：

```bash
# 執行 API 測試腳本
uv run python test_api.py
```

### 手動測試：

1. 訪問 `http://127.0.0.1:8000/api/` 查看 API 概覽
2. 使用瀏覽器訪問各個端點進行互動式測試
3. 使用 curl 或 Postman 進行程式化測試

## 🔧 主要功能

### ✅ 已實現功能：

-   🗄️ **完整資料庫模型** - 6 個相互關聯的資料表
-   � **RESTful API** - 支援完整 CRUD 操作
-   🔍 **搜尋與篩選** - 教師搜尋、狀態篩選等
-   📄 **自動分頁** - 每頁 20 筆資料
-   🌐 **CORS 支援** - 允許前端跨域請求
-   🛡️ **錯誤處理** - 詳細錯誤訊息
-   📊 **管理介面** - Django Admin 後台管理
-   ⚡ **自動評分** - 新增評價時自動更新課程平均評分

### 🛠️ 技術棧：

-   **框架**: Django 5.2.4
-   **API**: Django REST Framework 3.16.0
-   **資料庫**: SQLite (開發環境)
-   **套件管理**: uv
-   **CORS**: django-cors-headers

## 📁 專案結構

```
backend-django-HW/
├── myapps/                 # Django 專案目錄
│   ├── settings.py         # 專案設定
│   ├── urls.py            # URL 路由
│   └── myapps/            # 應用程式目錄
│       ├── models.py      # 資料模型
│       ├── views.py       # API 視圖
│       ├── serializers.py # 序列化器
│       └── admin.py       # 管理介面
├── db.sqlite3             # SQLite 資料庫
├── manage.py              # Django 管理命令
├── test_api.py           # API 測試腳本
├── API_GUIDE.md          # API 使用指南
└── pyproject.toml        # 專案依賴
```

## 📝 下一步建議

1. **加入認證系統** - 實作 JWT 或 Token 認證
2. **權限控制** - 設定不同角色的存取權限
3. **檔案上傳** - 支援教師頭像上傳
4. **前端整合** - 與 React/Vue 前端框架整合
5. **部署準備** - 配置生產環境設定

## 🎯 開發者提示

-   使用 `uv run python manage.py shell` 進入 Django shell 進行資料操作
-   修改模型後記得執行 `makemigrations` 和 `migrate`
-   在 `settings.py` 中的 `DEBUG = False` 用於生產環境
-   查看 `API_GUIDE.md` 了解詳細的 API 使用方式

---

🎉 **您的教學平台後端 API 已準備就緒！**
