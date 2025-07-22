# 教學平台 API 使用說明

## 🚀 API 概覽

您的教學平台現在支援完整的 CRUD (建立、讀取、更新、刪除) 操作！

**基礎 URL**: `http://127.0.0.1:8000/api/`

## 📋 可用端點

### 1. 使用者 (Users)

-   **獲取所有使用者**: `GET /api/users/`
-   **建立使用者**: `POST /api/users/`
-   **獲取特定使用者**: `GET /api/users/{id}/`
-   **更新使用者**: `PUT /api/users/{id}/`
-   **刪除使用者**: `DELETE /api/users/{id}/`
-   **按角色篩選**: `GET /api/users/?role=teacher`

### 2. 教師 (Teachers)

-   **獲取所有教師**: `GET /api/teachers/`
-   **建立教師**: `POST /api/teachers/`
-   **獲取特定教師**: `GET /api/teachers/{id}/`
-   **更新教師**: `PUT /api/teachers/{id}/`
-   **刪除教師**: `DELETE /api/teachers/{id}/`
-   **搜尋教師**: `GET /api/teachers/search/?q=關鍵字`
-   **按狀態篩選**: `GET /api/teachers/?status=active`

### 3. 學生 (Students)

-   **獲取所有學生**: `GET /api/students/`
-   **建立學生**: `POST /api/students/`
-   **獲取特定學生**: `GET /api/students/{id}/`
-   **更新學生**: `PUT /api/students/{id}/`
-   **刪除學生**: `DELETE /api/students/{id}/`

### 4. 課程 (Courses)

-   **獲取所有課程**: `GET /api/courses/`
-   **建立課程**: `POST /api/courses/`
-   **獲取特定課程**: `GET /api/courses/{id}/`
-   **更新課程**: `PUT /api/courses/{id}/`
-   **刪除課程**: `DELETE /api/courses/{id}/`
-   **按教師篩選**: `GET /api/courses/?teacher_id=1`
-   **按教師獲取課程**: `GET /api/courses/by_teacher/1/`

### 5. 預約 (Bookings)

-   **獲取所有預約**: `GET /api/bookings/`
-   **建立預約**: `POST /api/bookings/`
-   **獲取特定預約**: `GET /api/bookings/{id}/`
-   **更新預約**: `PUT /api/bookings/{id}/`
-   **刪除預約**: `DELETE /api/bookings/{id}/`
-   **按狀態篩選**: `GET /api/bookings/?status=confirmed`
-   **按學生篩選**: `GET /api/bookings/?student_id=1`
-   **按課程篩選**: `GET /api/bookings/?course_id=1`

### 6. 評價 (Reviews)

-   **獲取所有評價**: `GET /api/reviews/`
-   **建立評價**: `POST /api/reviews/`
-   **獲取特定評價**: `GET /api/reviews/{id}/`
-   **更新評價**: `PUT /api/reviews/{id}/`
-   **刪除評價**: `DELETE /api/reviews/{id}/`
-   **按課程篩選**: `GET /api/reviews/?course_id=1`

## 💾 資料格式範例

### 建立使用者

```json
POST /api/users/
{
  "name": "張老師",
  "account": "teacher_zhang",
  "password": "password123",
  "role": "teacher"
}
```

### 建立教師

```json
POST /api/teachers/
{
  "user": 1,
  "name": "張老師",
  "email": "zhang@example.com",
  "phone": "0912345678",
  "gender": "M",
  "age": "35",
  "education": "碩士",
  "intro": "資深數學老師",
  "status": "active",
  "blue_premium": true
}
```

### 建立課程

```json
POST /api/courses/
{
  "subject": "高中數學",
  "teacher": 1,
  "description": "專業高中數學輔導",
  "price": "800.00",
  "location": "台北市"
}
```

### 建立預約

```json
POST /api/bookings/
{
  "course": 1,
  "student": 1,
  "schedule_date": "2025-07-25 14:00",
  "status": "pending"
}
```

### 建立評價

```json
POST /api/reviews/
{
  "course": 1,
  "rating": "5",
  "comment": "老師教得很好！"
}
```

## 🛠️ 使用方式

### 方式 1: 使用 curl 命令

```bash
# 獲取所有教師
curl -X GET "http://127.0.0.1:8000/api/teachers/"

# 建立新教師
curl -X POST "http://127.0.0.1:8000/api/teachers/" \
  -H "Content-Type: application/json" \
  -d '{"user":1,"name":"李老師","email":"li@example.com","phone":"0987654321","gender":"F","age":"30","status":"active","blue_premium":false}'
```

### 方式 2: 使用 Python requests

```python
import requests

# 獲取所有教師
response = requests.get("http://127.0.0.1:8000/api/teachers/")
teachers = response.json()

# 建立新教師
teacher_data = {
    "user": 1,
    "name": "李老師",
    "email": "li@example.com",
    "phone": "0987654321",
    "gender": "F",
    "age": "30",
    "status": "active",
    "blue_premium": False
}
response = requests.post("http://127.0.0.1:8000/api/teachers/", json=teacher_data)
```

### 方式 3: 使用瀏覽器 (DRF 瀏覽式 API)

直接在瀏覽器中訪問：

-   `http://127.0.0.1:8000/api/teachers/` - 互動式教師 API
-   `http://127.0.0.1:8000/api/courses/` - 互動式課程 API

## 🔍 進階功能

### 分頁

API 回應會自動分頁，每頁 20 筆資料：

```json
{
  "count": 100,
  "next": "http://127.0.0.1:8000/api/teachers/?page=2",
  "previous": null,
  "results": [...]
}
```

### 搜尋

教師搜尋支援名稱、email 和介紹：

```
GET /api/teachers/search/?q=數學
```

### 篩選

大部分端點都支援基本篩選：

```
GET /api/teachers/?status=active
GET /api/courses/?teacher_id=1
GET /api/bookings/?status=confirmed
```

## ⚡ 特殊功能

1. **自動更新課程評分**: 當新增評價時，會自動重新計算課程平均評分
2. **關聯資料**: API 回應會包含相關資料的名稱和資訊
3. **CORS 支援**: 支援前端跨域請求
4. **錯誤處理**: 提供詳細的錯誤訊息

## 🎯 測試建議

1. 先建立使用者
2. 再建立教師/學生 (關聯到使用者)
3. 建立課程 (關聯到教師)
4. 建立預約 (關聯到課程和學生)
5. 建立評價 (關聯到課程)
