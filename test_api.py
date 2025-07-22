#!/usr/bin/env python3
"""
API 測試腳本
展示如何使用 CRUD API
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000/api"


def print_response(response, title):
    """美化打印 API 回應"""
    print(f"\n{'='*50}")
    print(f"{title}")
    print(f"{'='*50}")
    print(f"狀態碼: {response.status_code}")
    if response.status_code < 400:
        try:
            data = response.json()
            print(f"回應內容:\n{json.dumps(data, indent=2, ensure_ascii=False)}")
        except:
            print(f"回應內容: {response.text}")
    else:
        print(f"錯誤: {response.text}")


def test_crud_operations():
    """測試 CRUD 操作"""

    # 1. 測試 API 概覽
    print("🚀 開始測試 API...")
    response = requests.get(f"{BASE_URL}/")
    print_response(response, "📋 API 概覽")

    # 2. 建立使用者 (CREATE)
    user_data = {
        "name": "張老師",
        "account": "teacher_zhang",
        "password": "password123",
        "role": "teacher",
    }
    response = requests.post(f"{BASE_URL}/users/", json=user_data)
    print_response(response, "👤 建立使用者")

    if response.status_code == 201:
        user_id = response.json()["id"]

        # 3. 建立教師 (CREATE)
        teacher_data = {
            "user": user_id,
            "name": "張老師",
            "email": "zhang@example.com",
            "phone": "0912345678",
            "gender": "M",
            "age": "35",
            "education": "碩士",
            "intro": "資深數學老師",
            "status": "active",
            "blue_premium": True,
        }
        response = requests.post(f"{BASE_URL}/teachers/", json=teacher_data)
        print_response(response, "👨‍🏫 建立教師")

        if response.status_code == 201:
            teacher_id = response.json()["id"]

            # 4. 建立課程 (CREATE)
            course_data = {
                "subject": "高中數學",
                "teacher": teacher_id,
                "description": "專業高中數學輔導",
                "price": "800.00",
                "location": "台北市",
            }
            response = requests.post(f"{BASE_URL}/courses/", json=course_data)
            print_response(response, "📚 建立課程")

    # 5. 獲取所有教師 (READ)
    response = requests.get(f"{BASE_URL}/teachers/")
    print_response(response, "📋 獲取所有教師")

    # 6. 獲取所有課程 (READ)
    response = requests.get(f"{BASE_URL}/courses/")
    print_response(response, "📋 獲取所有課程")

    # 7. 搜尋教師
    response = requests.get(f"{BASE_URL}/teachers/search/?q=張")
    print_response(response, "🔍 搜尋教師")


if __name__ == "__main__":
    try:
        test_crud_operations()
        print("\n✅ API 測試完成！")
    except requests.exceptions.ConnectionError:
        print("❌ 無法連接到服務器，請確保 Django 服務器正在運行")
    except Exception as e:
        print(f"❌ 測試過程中發生錯誤: {e}")
