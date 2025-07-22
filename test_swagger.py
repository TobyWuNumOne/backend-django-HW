#!/usr/bin/env python3
"""
測試 Swagger API 文檔是否正常工作
"""

import requests
import json

BASE_URL = "http://127.0.0.1:8000"


def test_swagger_endpoints():
    """測試 Swagger 相關端點"""

    endpoints = [
        ("/swagger/", "Swagger UI"),
        ("/redoc/", "ReDoc"),
        ("/swagger.json", "Swagger JSON Schema"),
        ("/api/", "API 概覽"),
        ("/api/teachers/", "教師 API"),
    ]

    print("🧪 測試 API 端點...")
    print("=" * 50)

    for endpoint, description in endpoints:
        try:
            response = requests.get(f"{BASE_URL}{endpoint}", timeout=5)
            status = (
                "✅ 正常"
                if response.status_code == 200
                else f"❌ 錯誤 ({response.status_code})"
            )
            print(f"{description:20} | {endpoint:20} | {status}")

            # 如果是 JSON 端點，檢查內容
            if endpoint.endswith(".json"):
                try:
                    data = response.json()
                    print(f"   └─ JSON 包含 {len(data.get('paths', {}))} 個 API 路徑")
                except:
                    print(f"   └─ 非 JSON 格式回應")

        except requests.exceptions.RequestException as e:
            print(f"{description:20} | {endpoint:20} | ❌ 連線錯誤: {e}")

    print("\n🌐 可用的 API 文檔:")
    print("-" * 30)
    print(f"• Swagger UI: {BASE_URL}/swagger/")
    print(f"• ReDoc:     {BASE_URL}/redoc/")
    print(f"• API 概覽:  {BASE_URL}/api/")


if __name__ == "__main__":
    test_swagger_endpoints()
