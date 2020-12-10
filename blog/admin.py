from django.contrib import admin

from blog.models import TagName, Tag, NewsName, New


class TagInline(admin.TabularInline):
    model = TagName
    min_num = 2
    max_num = 2
    extra = 2


@admin.register(Tag)
class FieldAdmin(admin.ModelAdmin):
    model = Tag
    inlines = [
        TagInline,
    ]
# Register your models here.

class NewsLine(admin.TabularInline):
    model = NewsName
    min_num = 2
    max_num = 2
    extra = 2


@admin.register(New)
class FieldAdmin(admin.ModelAdmin):
    model = New
    readonly_fields = ["added_at"]
    inlines = [
        NewsLine,
    ]
