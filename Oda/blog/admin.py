from django.contrib import admin
from blog.models import Post

# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'modify_dt', 'image', 'tag_list')
    list_filter = ('modify_dt',)
    search_fields = ('title', 'content')
    prepopulated_fields = {'slug': ('title',)}


    # 두 메소드 추가
    def get_queryset(self, request):
        return super().get_queryset(request).prefetch_related('tags')

    # obj
    def tag_list(self, obj):
        return ', '.join(o.name for o in obj.tags.all())