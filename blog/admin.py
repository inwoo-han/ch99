from django.contrib import admin
from blog.models import Post
# Register your models here.

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt')
    list_filter = ('modify_dt',)
    search_fields = ('title','content')
    prepopulated_fields = {'slug': ('title',)}  # 포스트 추가할때 타이틀에 맞춰 자동완성 되는 필드