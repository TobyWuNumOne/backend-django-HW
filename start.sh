#!/bin/bash
# 教學平台後端啟動腳本

echo "🚀 教學平台後端啟動腳本"
echo "=========================="

# 檢查是否安裝 uv
if ! command -v uv &> /dev/null; then
    echo "❌ 錯誤: uv 尚未安裝"
    echo "請先安裝 uv: https://docs.astral.sh/uv/"
    exit 1
fi

echo "📦 同步專案依賴..."
uv sync

echo "🗄️ 檢查資料庫遷移..."
uv run python manage.py makemigrations
uv run python manage.py migrate

echo "🌐 啟動 Django 開發服務器..."
echo "服務器將在 http://127.0.0.1:8000/ 啟動"
echo ""
echo "可用端點:"
echo "- 管理後台: http://127.0.0.1:8000/admin/"
echo "- API 概覽: http://127.0.0.1:8000/api/"
echo "- API 文件: 請查看 API_GUIDE.md"
echo ""
echo "按 Ctrl+C 停止服務器"
echo "=========================="

uv run python manage.py runserver
