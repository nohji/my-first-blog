from django.contrib import admin
from .models import Post, Comment

# 관리자 페이지에서 만든 모델을 보기위해 등록.
admin.site.register(Post)
admin.site.register(Comment)