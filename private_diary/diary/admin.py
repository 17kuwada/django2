from django.contrib import admin

# Register your models here.

# from ファイル名　import クラス名
from.models import Diary

# 日記テーブルを管理サイトで編集できるように登録する
admin.site.register(Diary)
